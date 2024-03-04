import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json

# Function to truncate title
def truncate_title(title, max_chars=20):
    return title[:max_chars]

# Function to scrape content and export as Markdown file
def scrape_and_export(url, folder_path):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find the div element with id "portfolio-content"
        portfolio_content_div = soup.find("div", id="portfolio-content")
        
        # Check if the div element exists and has a child div with class "portfolio-inner"
        if portfolio_content_div and portfolio_content_div.find("div", class_="portfolio-inner"):
            # Extract page title
            title = soup.title.string.strip()
            # Truncate title if it exceeds maximum characters
            truncated_title = truncate_title(title)
            filename = f"{folder_path}/{truncated_title}.md"
            
            # Create directory if it doesn't exist
            os.makedirs(folder_path, exist_ok=True)
            
            # Open file in write mode
            with open(filename, "w", encoding="utf-8") as file:
                # Write page title as main heading
                file.write(f"# {title}\n\n")
                # Write URL under the main heading
                file.write(f"URL: {url}\n\n")
                
                # Find all text and image elements within the portfolio-inner div
                for element in portfolio_content_div.find_all(["p", "h1", "h2", "h3", "h4", "img"]):
                   
                    if element.name == "img":
                        prop = "src"
                        if "data-src" in element.attrs:
                            prop = "data-src"
                        w =    element["width"]
                        h =   element["height"]

                        # Write image HTML with width and height attributes
                        file.write(f'<img src="{element[prop]}" width="{w}" height="{h}">\n\n')
                    else:
                        # Write text with appropriate heading markdown
                        if element.name.startswith("h"):
                            heading_level = int(element.name[1])
                            file.write(f"{'#' * heading_level} {element.get_text().strip()}\n\n")
                        else:
                            file.write(f"{element.get_text().strip()}\n\n")
                print(f"Scraped content from {title} and saved to {filename}")
        else:
            print("Div elements 'portfolio-content' or 'portfolio-inner' not found.")
    else:
        print(f"Failed to retrieve {url}. Status code:", response.status_code)

# Define the path to the config file
config_file_path = 'scripts\XMPRO Website Scrape Scripts\scrape-xmpro-website-solutions-config.json'

# Load JSON config file
with open(config_file_path) as json_file:
    config_data = json.load(json_file)
    folder_path = config_data.get("folderPath")

# URL of the webpage
base_url = "https://xmpro.com"
url = "https://xmpro.com/solutions-library/"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find the div element with id "portfolio-1816263738"
    div_element = soup.find("div", id="portfolio-1816263738")
    
    # Check if the div element exists
    if div_element:
        # Find all hyperlinks (a tags) within the div element
        hyperlinks = div_element.find_all("a")
        
        # Extract and scrape content from each hyperlink
        for hyperlink in hyperlinks:
            href = hyperlink.get("href")
            if href:
                full_url = urljoin(base_url, href)
                scrape_and_export(full_url, folder_path)
    else:
        print("Div element not found.")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
