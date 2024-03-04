import os
import requests
from bs4 import BeautifulSoup
from pathvalidate import sanitize_filename

# Function to save content to Markdown file
def save_to_md(title, content, url, folder_path):
    try:
        # Sanitize the title to ensure it's suitable for use as a filename
        sanitized_title = sanitize_filename(title.strip().replace("&", ""))
        
        # Truncate the filename to a maximum of 20 characters
        truncated_title = sanitized_title[:20]
        
        filename = os.path.join(folder_path, f"{truncated_title}.md")

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"# {title}\n\n")
            file.write(f"URL: {url}\n\n")
            file.write(content)
        print(f"Content saved to {filename}")
    except Exception as e:
        print(f"Error occurred while saving to file: {e}")

# Function to scrape content from each page
def scrape_page(url, folder_path):
    try:
        # Send a GET request to the page URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Find the title of the page
            title_elem = soup.find("title")
            if title_elem:
                title = title_elem.text.strip()

                # Find the portfolio-inner div
                portfolio_inner_div = soup.find("div", class_="portfolio-inner")

                if portfolio_inner_div:
                    # Find all content elements within the portfolio-inner div
                    content_elements = portfolio_inner_div.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "p", "img"])

                    # Initialize markdown content
                    markdown_content = ""

                    # Append content to the markdown content preserving order
                    for element in content_elements:
                        if element.name.startswith("h"):  # Heading elements
                            heading_level = int(element.name[1])
                            markdown_content += f"{'#' * heading_level} {element.text.strip()}\n\n"
                        elif element.name == "img":  # Image elements
                            if element.has_attr("src"):  # Check if "src" attribute exists
                                image_url = element["src"]
                                markdown_content += f"![Image]({image_url})\n\n"
                        else:  # Paragraph elements
                            markdown_content += f"{element.get_text().strip()}\n\n"

                    # Save content to a Markdown file
                    save_to_md(title, markdown_content, url, folder_path)
                else:
                    print("Portfolio inner div not found.")
            else:
                print("Title element not found.")
        else:
            print(f"Failed to retrieve page {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error occurred while scraping page {url}: {e}")


# Main function
def main():
    # Define the URL
    url = "https://xmpro.com/solutions-library/use-cases/"
    
    # Define the folder path
    folder_path = "Use Cases"
    os.makedirs(folder_path, exist_ok=True)

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find all page hyperlinks within the specified div
        content_div = soup.find("div", id="content", class_="page-wrapper")
        if content_div:
            hyperlinks = content_div.find_all("a", href=True)

            # Iterate over each hyperlink
            for hyperlink in hyperlinks:
                page_url = hyperlink["href"]
                scrape_page(page_url, folder_path)
        else:
            print("Content div not found.")
    else:
        print(f"Failed to retrieve page {url}. Status code: {response.status_code}")

if __name__ == "__main__":
    main()
