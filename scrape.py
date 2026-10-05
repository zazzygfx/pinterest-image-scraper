from playwright.sync_api import sync_playwright
import os
from urllib.parse import quote

keyword = input("What do you want to search Pinterest for? ")
number = int(input("How many images do you want? "))

output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

user_data_dir = os.path.abspath("pinterest_browser_profile")

with sync_playwright() as p:

    print("\nOpening Pinterest...")

    context = p.chromium.launch_persistent_context(
        user_data_dir,
        headless=False
    )

    page = context.pages[0] if context.pages else context.new_page()

    search_url = (
        "https://www.pinterest.com/search/pins/?q="
        + quote(keyword)
        + "&rs=typed"
    )

    page.goto(
        search_url,
        wait_until="domcontentloaded",
        timeout=60000
    )

    page.wait_for_timeout(6000)

    print("Loading pins...")

    pin_urls = []
    previous_count = 0
    no_new_pins = 0

    while len(pin_urls) < number:

        links = page.locator('a[href*="/pin/"]').evaluate_all("""
            links => links
                .map(a => a.href)
                .filter(href => href.includes("/pin/"))
        """)

        for url in links:
            if url not in pin_urls:
                pin_urls.append(url)

        print(f"Found {len(pin_urls)}/{number} pins...")

        if len(pin_urls) >= number:
            break

        if len(pin_urls) == previous_count:
            no_new_pins += 1
        else:
            no_new_pins = 0

        previous_count = len(pin_urls)

        if no_new_pins >= 8:
            print("\nPinterest isn't loading any more Pins.")
            break

        page.mouse.wheel(0, 2000)
        page.wait_for_timeout(2000)

    print(f"\nCollected {len(pin_urls)} Pin links.")

    if not pin_urls:
        print("No Pins found.")
        input("Press ENTER to close...")
        context.close()
        exit()

    downloaded = 0

    for pin_url in pin_urls:

        if downloaded >= number:
            break

        try:

            print(f"\nOpening pin {downloaded + 1}/{number}...")

            pin_page = context.new_page()

            pin_page.goto(
                pin_url,
                wait_until="domcontentloaded",
                timeout=60000
            )

            pin_page.wait_for_timeout(3500)

            images = pin_page.locator("img").evaluate_all("""
                imgs => imgs
                    .map(img => ({
                        src: img.currentSrc || img.src,
                        width: img.naturalWidth,
                        height: img.naturalHeight
                    }))
                    .filter(x =>
                        x.src &&
                        x.src.includes("pinimg.com") &&
                        x.width > 300 &&
                        x.height > 300
                    )
                    .sort((a,b) =>
                        (b.width * b.height) -
                        (a.width * a.height)
                    )
            """)

            if not images:
                print("No large image found.")
                pin_page.close()
                continue

            image_url = images[0]["src"]

            print(
                f"Image found: "
                f"{images[0]['width']}x{images[0]['height']}"
            )

            response = context.request.get(
                image_url,
                headers={
                    "Referer": pin_url,
                    "User-Agent": "Mozilla/5.0"
                },
                timeout=30000
            )

            if not response.ok:
                print("Download failed.")
                pin_page.close()
                continue

            data = response.body()

            if data.startswith(b"\xff\xd8\xff"):
                extension = ".jpg"
            elif data.startswith(b"\x89PNG"):
                extension = ".png"
            elif data.startswith(b"RIFF"):
                extension = ".webp"
            else:
                print("Downloaded data is not a valid image.")
                pin_page.close()
                continue

            downloaded += 1

            filename = os.path.join(
                output_folder,
                f"pinterest_{downloaded}{extension}"
            )

            with open(filename, "wb") as f:
                f.write(data)

            size_mb = len(data) / (1024 * 1024)

            print(
                f"Downloaded {downloaded}/{number} "
                f"| {images[0]['width']}x{images[0]['height']} "
                f"| {size_mb:.2f} MB"
            )

            pin_page.close()

        except Exception as e:
            print(f"Error: {e}")

    print("\n================================")
    print(f"Done! Downloaded {downloaded} images.")
    print(f"Folder: {os.path.abspath(output_folder)}")
    print("================================")

    input("\nPress ENTER to close the browser...")

    context.close()
