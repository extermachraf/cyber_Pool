import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import argparse


class ImageDownloader:
    def __init__(self, base_url, max_depth=5, output_dir='./data', allowed_extensions=None):
        self.base_url = base_url
        self.max_depth = max_depth
        self.output_dir = output_dir
        self.visited_urls = set()  # Track visited URLs to avoid revisits
        self.downloaded_images = set()  # Track downloaded image URLs to avoid duplicates
        self.allowed_extensions = allowed_extensions or [
            '.jpg', '.jpeg', '.png', '.gif', '.bmp']
        os.makedirs(self.output_dir, exist_ok=True)

    def download_images_from_url(self, url, depth=0):
        # Base case: limit recursion depth
        if depth > self.max_depth:
            return

        # Skip URL if already visited
        if url in self.visited_urls:
            return
        self.visited_urls.add(url)

        try:
            response = requests.get(url)
            if response.status_code != 200:
                print(f"Failed to access {url}, status code: {
                      response.status_code}")
                return

            print(f"Visiting {url}, depth: {depth}")
            soup = BeautifulSoup(response.text, 'html.parser')

            # Download images on this page
            self._download_images(soup, url)

            # Recursively find and process linked pages if recursion is enabled
            self._crawl_links(soup, url, depth)

        except Exception as e:
            print(f"Error visiting {url}: {e}")

    def _download_images(self, soup, url):
        images = soup.find_all('img')
        image_links = [img.get('src') for img in images if img.get('src')]

        for i, img_url in enumerate(image_links):
            try:
                full_img_url = urljoin(url, img_url)  # Handle relative URLs
                if not self._is_valid_extension(full_img_url):
                    continue  # Skip files that don't match allowed extensions

                # Check if the image has already been downloaded
                if full_img_url in self.downloaded_images:
                    print(f"Already downloaded: {full_img_url}")
                    continue

                # Mark this image as downloaded
                self.downloaded_images.add(full_img_url)

                # Extract filename from the image URL
                # Get the original filename
                img_name = os.path.basename(full_img_url)
                # Full path to save the image
                img_path = os.path.join(self.output_dir, img_name)

                # Ensure unique filename if it already exists
                counter = 1
                while os.path.exists(img_path):
                    # Split name and extension
                    name, ext = os.path.splitext(img_name)
                    # Rename file to avoid overwrite
                    img_name = f"{name}_{counter}{ext}"
                    img_path = os.path.join(
                        self.output_dir, img_name)  # Update full path

                img_data = requests.get(full_img_url).content
                with open(img_path, 'wb') as img_file:
                    img_file.write(img_data)
                print(f"Downloaded: {img_path}")
            except Exception as e:
                print(f"Error downloading {full_img_url}: {e}")

    def _crawl_links(self, soup, url, depth):
        # Find all links and visit them recursively if -r option is used
        for link in soup.find_all('a', href=True):
            next_url = urljoin(url, link['href'])
            # Visit only URLs from the same domain as the base URL
            if urlparse(next_url).netloc == urlparse(self.base_url).netloc:
                self.download_images_from_url(next_url, depth + 1)

    def _is_valid_extension(self, url):
        # Check if the URL ends with an allowed image extension
        return any(url.lower().endswith(ext) for ext in self.allowed_extensions)

    def start(self):
        # Start the recursive download from the base URL
        self.download_images_from_url(self.base_url)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Spider to download images from a URL.")
    parser.add_argument("url", help="URL to download images from")
    parser.add_argument("-r", action="store_true",
                        help="Enable recursive download")
    parser.add_argument("-l", type=int, default=5,
                        help="Maximum depth level for recursive download (default: 5)")
    parser.add_argument("-p", type=str, default="./data",
                        help="Path to save downloaded files (default: ./data)")
    return parser.parse_args()


def main():
    args = parse_args()
    downloader = ImageDownloader(
        base_url=args.url, max_depth=args.l, output_dir=args.p)
    downloader.start()


if __name__ == "__main__":
    main()
