```markdown
# Pinterest Image Scraper

> A Windows-based Python tool that searches Pinterest for a keyword and automatically downloads the number of images you request.

Built with **Python + Playwright**.

Created and maintained by **Zazzy** — [@zazzygfx on X](https://x.com/zazzygfx).

---

## 📌 Table of Contents

- [What Is This?](#-what-is-this)
- [Origin & Development](#-origin--development)
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Before You Start](#-before-you-start)
- [Installation](#-installation)
  - [1. Download the Project](#1-download-the-project)
  - [2. Install Python](#2-install-python)
  - [3. Verify Python](#3-verify-python)
  - [4. Open the Project Folder](#4-open-the-project-folder)
  - [5. Install Playwright](#5-install-playwright)
  - [6. Install Chromium](#6-install-chromium)
- [Using the Scraper](#-using-the-scraper)
  - [1. Start the Scraper](#1-start-the-scraper)
  - [2. Log Into Pinterest](#2-log-into-pinterest)
  - [3. Enter Your Search](#3-enter-your-search)
  - [4. Choose the Number of Images](#4-choose-the-number-of-images)
  - [5. Wait for the Scraper](#5-wait-for-the-scraper)
- [Where Are My Images?](#-where-are-my-images)
- [Running It Again](#-running-it-again)
- [Project Structure](#-project-structure)
- [Browser Profile](#-browser-profile)
- [Troubleshooting](#-troubleshooting)
- [Important Notes](#-important-notes)
- [Responsible Use](#-responsible-use)
- [Contributing](#-contributing)
- [License](#-license)

---

# 🔎 What Is This?

**Pinterest Image Scraper** is a Python tool that automates the process of finding and downloading images from Pinterest.

Instead of manually searching Pinterest, opening Pins one by one, and saving images individually, you can simply tell the scraper:

```text
What do you want to search Pinterest for?
How many images do you want?
```

For example:

```text
What do you want to search Pinterest for? futuristic cars
How many images do you want? 50
```

The scraper then opens Pinterest, searches for the keyword, collects Pin links, opens the individual Pin pages, finds a large usable image, and downloads the images automatically.

---

# 🧭 Origin & Development

This project was developed by **Zazzy** by taking an existing Pinterest-scraping approach and iterating on it through testing, debugging, and improvement.

The initial approach had several practical problems, including:

- Pinterest returning low-resolution thumbnail images
- Difficulty reliably collecting enough Pins
- Downloads returning images that were not suitable for the intended use
- Browser and profile issues during automated browsing
- Scraping search results without reliably reaching individual Pin pages

The project was then **corrected and improved** into the current workflow.

The current version:

1. Searches Pinterest using a keyword.
2. Scrolls through Pinterest search results.
3. Collects individual Pin URLs.
4. Opens each Pin page.
5. Looks for large usable `pinimg.com` images.
6. Selects the largest suitable image found.
7. Downloads the image.
8. Saves the result locally.

The goal was to make the existing approach **more reliable and practical for actually downloading usable Pinterest images**.

The current version was built and tested on **Windows**.

> **Transparency:** This project builds on an existing scraping approach rather than claiming that every underlying scraping technique was invented from scratch. The corrections, improvements, debugging, implementation, and tested workflow are maintained in this repository.

---

# ✨ Features

- 🔎 Search Pinterest using any keyword
- 🔢 Choose how many images to download
- 🌐 Automatically open Pinterest
- 📜 Automatically scroll through search results
- 📌 Collect individual Pin URLs
- 🖼️ Open individual Pin pages
- 🔍 Find the largest usable image available
- ⬇️ Download images automatically
- 📁 Save downloaded images in an `output` folder
- 🔐 Keep your Pinterest browser session locally
- 💻 Built and tested on Windows

---

# ⚙️ How It Works

The scraper follows this process:

```text
Enter a Pinterest keyword
          ↓
Enter the number of images
          ↓
Open Pinterest
          ↓
Search Pinterest
          ↓
Scroll through results
          ↓
Collect Pin URLs
          ↓
Open individual Pins
          ↓
Find a large usable image
          ↓
Download the image
          ↓
Save it inside output/
```

---

# 🪟 Before You Start

This project has been **tested on Windows**.

You will need:

- Windows 10 or Windows 11
- An internet connection
- A Pinterest account
- Python 3.12 or newer
- Basic ability to download files and open folders

You do **not** need to know how to program Python to use this project.

---

# 🚀 Installation

Follow these steps **in order**.

If you have never used Python before, don't worry. The steps below explain what to download, what to click, and what commands to run.

---

## 1. Download the Project

Go to the GitHub repository:

**https://github.com/zazzygfx/pinterest-image-scraper**

On the repository page:

1. Click the green **Code** button.
2. Click **Download ZIP**.
3. Wait for the ZIP file to download.
4. Open your **Downloads** folder.
5. Find the downloaded ZIP file.
6. Right-click the ZIP file.
7. Select **Extract All...**
8. Click **Extract**.

You should now have a folder called something similar to:

```text
pinterest-image-scraper
```

Open that folder.

You should see:

```text
scrape.py
requirements.txt
README.md
.gitignore
```

---

## 2. Install Python

The scraper is written in Python, so Python must be installed on your computer.

Go to:

**https://www.python.org/downloads/**

Download **Python 3.12 or newer for Windows**.

### ⚠️ Important

When the Python installer opens, look near the bottom of the installer.

You should see an option similar to:

```text
☐ Add python.exe to PATH
```

Make sure it is checked:

```text
☑ Add python.exe to PATH
```

Then click:

**Install Now**

Wait for Python to finish installing.

---

## 3. Verify Python

After Python has finished installing, we need to check that Windows can find it.

### Open Command Prompt

Press:

```text
Windows + R
```

A small **Run** window will appear.

Type:

```text
cmd
```

Then press **Enter**.

A black Command Prompt window will open.

Type:

```bash
py --version
```

Then press **Enter**.

You should see something similar to:

```text
Python 3.12.10
```

The exact version may be different.

If you see a Python version, Python is installed correctly.

---

## 4. Open the Project Folder in Command Prompt

Open the `pinterest-image-scraper` folder you extracted earlier.

You should see:

```text
scrape.py
requirements.txt
README.md
.gitignore
```

Now click the **address bar** at the top of File Explorer.

It may look similar to:

```text
C:\Users\YourName\Downloads\pinterest-image-scraper
```

Click inside the address bar.

Type:

```text
cmd
```

Press **Enter**.

Command Prompt should now open directly inside your project folder.

You should see a path similar to:

```text
C:\Users\YourName\Downloads\pinterest-image-scraper>
```

---

## 5. Install Playwright

### What is Playwright?

Playwright is a browser automation tool.

It allows the Python program to control a real web browser.

This scraper uses Playwright to:

- Open Pinterest
- Search Pinterest
- Scroll through results
- Open Pin pages
- Find images
- Download images

The required package is already listed in:

```text
requirements.txt
```

Install it by running:

```bash
py -3.12 -m pip install -r requirements.txt
```

Press **Enter**.

Wait for the installation to finish.

---

## 6. Install Chromium

Playwright also needs a browser to control.

This project uses **Chromium**.

Install it by running:

```bash
py -3.12 -m playwright install chromium
```

Press **Enter**.

Wait for the installation to finish.

You normally only need to do this once.

---

# 🖼️ Using the Scraper

Once installation is complete, you're ready to use the scraper.

---

## 1. Start the Scraper

Make sure Command Prompt is still inside the project folder.

Run:

```bash
py -3.12 scrape.py
```

Press **Enter**.

The program will start.

You should see:

```text
What do you want to search Pinterest for?
```

---

## 2. Log Into Pinterest

A Chromium browser window will open.

Pinterest may ask you to log in.

Log into your Pinterest account normally.

### Important

The scraper uses a separate browser profile on your computer to keep your Pinterest session.

More information about this is available in the [Browser Profile](#-browser-profile) section.

---

## 3. Enter Your Search

The terminal will ask:

```text
What do you want to search Pinterest for?
```

Type what you want to search for.

For example:

```text
futuristic cars
```

Then press **Enter**.

Other examples:

```text
product photography
```

```text
fashion campaign
```

```text
minimalist interior design
```

```text
african fashion
```

---

## 4. Choose the Number of Images

The program will then ask:

```text
How many images do you want?
```

Enter the number you want.

For example:

```text
50
```

Then press **Enter**.

The scraper will begin collecting Pinterest Pins.

---

## 5. Let the Scraper Work

You will see progress in Command Prompt.

For example:

```text
Found 10/50 pins...
Found 20/50 pins...
Found 30/50 pins...
Found 40/50 pins...
Found 50/50 pins...
```

The scraper will then open individual Pin pages.

You may see:

```text
Opening pin 1/50...
Image found: 1000x1500
Downloaded 1/50
```

It will continue until it finishes.

### ⚠️ Do not close the browser while the scraper is running.

---

# 📁 Where Are My Images?

The scraper automatically creates an:

```text
output
```

folder.

Your downloaded images are saved there.

For example:

```text
pinterest-image-scraper/
│
├── scrape.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── output/
    ├── pinterest_1.jpg
    ├── pinterest_2.jpg
    ├── pinterest_3.jpg
    └── ...
```

Open the `output` folder to see your downloaded images.

---

# 🖼️ Image Formats

Depending on what Pinterest provides, images may be saved as:

```text
.jpg
.png
.webp
```

For example:

```text
pinterest_1.jpg
pinterest_2.jpg
pinterest_3.webp
```

---

# 🔁 Running the Scraper Again

After the initial installation, you do **not** need to reinstall everything every time.

To run it again:

1. Open the `pinterest-image-scraper` folder.
2. Open Command Prompt inside the folder.
3. Run:

```bash
py -3.12 scrape.py
```

4. Enter your keyword.
5. Enter the number of images.
6. Let it run.

---

# 📂 Project Structure

The GitHub repository contains:

```text
pinterest-image-scraper/
│
├── scrape.py
├── requirements.txt
├── README.md
└── .gitignore
```

### `scrape.py`

The main Python program.

This contains the scraper.

### `requirements.txt`

Contains the Python package required by the project:

```text
playwright
```

### `README.md`

The project documentation and installation guide.

### `.gitignore`

Prevents local/private files and generated files from being uploaded to GitHub.

---

# 🔐 Browser Profile

When the scraper runs, it creates a folder called:

```text
pinterest_browser_profile
```

This is a local browser profile used by Playwright.

It allows your Pinterest session to remain available between runs.

### ⚠️ Do NOT upload this folder to GitHub.

It may contain private browser session information.

The project includes it in `.gitignore`:

```text
pinterest_browser_profile/
```

so Git ignores it.

---

# 📦 Output Folder

The scraper creates:

```text
output/
```

to store downloaded images.

This folder is also ignored by Git.

Your downloaded images therefore remain on your computer instead of being uploaded to the GitHub repository.

---

# 🛠️ Troubleshooting

## `'py' is not recognized`

If Windows shows an error such as:

```text
'py' is not recognized as an internal or external command
```

Python may not have been installed correctly.

### Fix

Reinstall Python from:

**https://www.python.org/downloads/**

During installation, make sure:

```text
☑ Add python.exe to PATH
```

is enabled.

Then close and reopen Command Prompt.

Check again:

```bash
py --version
```

---

## `ModuleNotFoundError: No module named 'playwright'`

Run:

```bash
py -3.12 -m pip install -r requirements.txt
```

Then run:

```bash
py -3.12 scrape.py
```

again.

---

## Chromium is missing

Run:

```bash
py -3.12 -m playwright install chromium
```

Then start the scraper again:

```bash
py -3.12 scrape.py
```

---

## Pinterest does not load

Check:

- Your internet connection.
- Pinterest is accessible.
- You are logged into Pinterest.
- The browser window is still open.
- You did not close the browser while the scraper was running.

Try running the scraper again if necessary.

---

## I requested 100 images but received fewer

The requested number is the **target**, not a guarantee.

Some Pins may not be downloadable by the scraper.

Possible reasons include:

- A Pin does not contain a suitable image.
- An image fails to load.
- Pinterest stops loading additional Pins.
- A Pin page does not expose a sufficiently large image.
- A download fails.

The scraper skips Pins it cannot process and continues.

---

## Pinterest stops loading new Pins

The scraper will stop after Pinterest stops providing new Pin links for several attempts.

If this happens, try:

- A different search keyword.
- A smaller number of images.
- Running the scraper again.

---

# ⚠️ Important Notes

## Image Quality

The scraper attempts to find the **largest usable image available on each individual Pin page**.

Pinterest does not always expose the original source image or its original resolution.

Because of this, image quality can vary.

## Pinterest Changes

Pinterest can change its website structure and behavior.

If Pinterest changes how its pages work, this scraper may require updates.

## Internet Connection

The scraper requires an active internet connection because it needs to access Pinterest and download images.

---

# ⚖️ Responsible Use

This project is provided for educational and personal use.

Pinterest images may be protected by copyright.

Before downloading, modifying, publishing, or commercially using an image, make sure you have the appropriate rights or permission.

Please respect:

- Pinterest's terms of service
- Copyright laws
- Photographers
- Artists
- Designers
- Other content creators

Do not use this tool to infringe copyright or misuse someone else's work.

---

# 🤝 Contributing

Found a bug?

Have an idea for improving the scraper?

You can open an **Issue** or submit a **Pull Request** on GitHub.

Possible future improvements include:

- Duplicate image detection
- Better image filtering
- Image quality selection
- Better filename generation
- Download folders based on keywords
- A graphical user interface
- Additional export options

---

# ⭐ Support the Project

If you find this project useful:

- ⭐ Star the repository
- Share it with other designers and developers
- Report bugs
- Suggest improvements
- Contribute to the project

---

# 📜 License

This project is released under the **MIT License**.

---

## Made by Zazzy

**Zazzy Graphics**  
X: [@zazzygfx](https://x.com/zazzygfx)  
GitHub: [@zazzygfx](https://github.com/zazzygfx)

Built with **Python + Playwright**.
```
