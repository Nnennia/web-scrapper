import urllib.error
import json
import urllib.request

def get_page_content(url):
    """
    Fetches the content of a webpage using its URL and returns it as a string in UTF-8 format.
    
    Args:
        url (str): The URL of the webpage to be fetched.
        
    Returns:
        str: The content of the webpage in UTF-8 format.
        None: If there is an error in fetching the webpage.
    """
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode("utf-8")
    except urllib.error.URLError as e:
        print(f"Error fetching this page: {e}")
        return None


def extract_html_content(html_content):
    """
    Extracts the title and paragraphs from an HTML content.

    Args:
    - html_content: a string containing the HTML content from which the title and paragraphs need to be extracted.

    Returns:
    - A dictionary with the following keys:
        - "title": a string containing the title extracted from the HTML content.
        - "paragraphs": a list of strings containing the paragraphs extracted from the HTML content.
    """

    # title and paragraph
    start_title = html_content.find('<title>')
    if start_title == -1:
        title = 'No title found'
    else:
        start_title += len('<title>')
        end_title = html_content.find('</title>')
        title = html_content[start_title:end_title]
    
    paragraphs = []
    start_paragraph = 0
    
    while True:
        start_paragraph = html_content.find("<p", start_paragraph)
        if start_paragraph == -1:
            break
        
        end_paragraph = html_content.find("</p>", start_paragraph)
        if end_paragraph == -1:
            break

        start_paragraph_tag = html_content.find(">", start_paragraph)
        end_paragraph_tag = html_content.find(">", start_paragraph_tag + 1)
        end_paragraph = html_content.find("</p>", end_paragraph_tag)

        paragraph = html_content[end_paragraph_tag + 1:end_paragraph]
        paragraphs.append(paragraph)

        start_paragraph = end_paragraph + len("</p>")
    


    return {"title": title, "paragraphs": paragraphs}

if __name__ == "__main__":
    url = input("Enter the URL you want to scrape: ")
    page_content = get_page_content(url)

    if page_content:
        data = extract_html_content(page_content)

        # Save data in a JSON file
        output_filename = "scraped_data.json"
        with open(output_filename, "w") as file:
            json.dump(data, file)

        print("Data has been scraped and saved to 'scraped_data.json'")
