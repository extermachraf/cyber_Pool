# Spider: Image Downloader

## Overview
The **Spider** program is a command-line tool that downloads images from a given URL. It supports recursive downloading, depth control, and customizable save paths. The **Scorpion** program is a command-line tool that extracts and displays EXIF metadata and other information from image files.

---

## Usage
To use the `spider` program, pass the URL and additional options for recursion, depth, and save path.

To use the `scorpion` program, provide one or more image files as arguments.

### Spider Command
```bash
python spider.py [-r] [-l N] [-p PATH] URL
