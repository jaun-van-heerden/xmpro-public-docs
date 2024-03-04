import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_and_export(url, folder_path):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        with requests.Session() as session:
            response = session.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for bad status codes
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the main content area
            main_content = soup.find('main', id='main', class_='')
            if main_content:
                page_title = soup.title.string.strip()[:20]  # Truncate title to a maximum of 20 characters

                # Ensure the title is not empty after truncation
                if page_title.strip():
                    filename = os.path.join(folder_path, f"{page_title}.md")
                else:
                    filename = os.path.join(folder_path, "Untitled.md")

                with open(filename, 'w', encoding='utf-8') as file:
                    # Write page title as main heading
                    file.write(f"# {page_title}\n\n")

                    # Write page URL in the specified format
                    file.write(f"URL: {url}\n\n")

                    # Find all text, image, and video elements within the main content area
                    for element in main_content.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6", "img", "iframe"]):
                        if element.name == "img":
                            prop = "src"
                            if "data-src" in element.attrs:
                                prop = "data-src"
                            w = element.get("width")
                            h = element.get("height")
                            file.write(f'<img src="{element[prop]}" width="{w * 2}" height="{h * 2}">\n\n')  # Increase image dimensions
                        elif element.name == "iframe" and "youtube.com" in element["src"]:
                            youtube_id = element["src"].split("/")[-1].split("?")[0]
                            file.write(f'[![Watch the video](https://img.youtube.com/vi/{youtube_id}/default.jpg)](https://youtu.be/{youtube_id})\n\n')  # Embed YouTube video thumbnail
                        else:
                            if element.name.startswith("h"):
                                heading_level = int(element.name[1])
                                file.write(f"{'#' * heading_level} {element.get_text().strip()}\n\n")
                            else:
                                file.write(f"{element.get_text().strip()}\n\n")

                print(f"Content saved to {filename}")
            else:
                print("Main content area not found.")
    except requests.RequestException as e:
        print(f"Failed to retrieve content from {url}: {e}")
    except Exception as e:
        print(f"Error occurred while fetching content from {url}: {e}")

# Define the URLs to scrape
urls = [
    "https://xmpro.com/intelligent-integration/",
    "https://xmpro.com/xmpro-ai/",
    "https://xmpro.com/interactive-3d-models/",
    "https://xmpro.com/pricing/"
]

# Define the folder path
folder_path = "XMPro Platform"
os.makedirs(folder_path, exist_ok=True)

# Scrape and export content for each URL
for url in urls:
    scrape_and_export(url, folder_path)
