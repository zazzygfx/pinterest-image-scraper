Paste **this entire block** into the big README editor:

```markdown
# Pinterest Image Scraper

A simple Python tool that searches Pinterest for a keyword and downloads the requested number of images automatically.

## What it does

- Search Pinterest using any keyword
- Collect Pinterest Pin links
- Open individual Pins
- Find the largest usable image on each Pin
- Download the images automatically
- Save the images inside an `output` folder

## Requirements

- Python 3.12+
- A Pinterest account
- Internet connection
- Windows, macOS, or Linux

## Installation

Install the required Python package:

```bash
pip install -r requirements.txt
```

Install Playwright's Chromium browser:

```bash
playwright install chromium
```

## Usage

Run:

```bash
python scrape.py
```

The scraper will ask:

```text
What do you want to search for?
How many images do you want?
```

For example:

```text
What do you want to search Pinterest for? futuristic cars
How many images do you want? 50
```

The scraper will open Pinterest, collect the requested Pins, and download the images.

Downloaded images are saved in:

```text
output/
```

## First-time use

The scraper uses a separate browser profile called:

```text
pinterest_browser_profile/
```

On the first run, Pinterest may require you to log in.

Your Pinterest login session is stored locally in this browser profile and is not included in this repository.

## Notes

Pinterest may not always expose the original full-resolution image. The scraper attempts to find the largest usable image available on the individual Pin page.

The number of images downloaded may be lower than requested if some Pins do not contain a suitable downloadable image.

## Responsible use

Use this tool responsibly.

Respect Pinterest's terms of service, copyright, and the rights of image creators. Only download or use images when you have the appropriate permission or rights to do so.

This project is provided for educational and personal use.

## License

MIT License
```

**After pasting, don't change anything.** Scroll down to **Commit changes** and we'll do that next.
