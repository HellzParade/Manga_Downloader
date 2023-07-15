from stringhelpers import *  # String utility helpers
from settings import *  # Global constants
import requests  # Library to make HTTP requests
import shutil  # Do advanced file operations
import os  # To operate with directories


# Send a request via HTTP
def send_request(url, binary = False):
    try:
        request = requests.get(url, stream = binary)  # HTTP request
    except:  # What to do if something happens
        print(REQUEST_ERROR)  # Print a message before exiting
        exit()
    return request  # If successful, return the request


# Check to see if the episode was released or not
def not_available(seriesName, episodeNum):
    manga_url = get_page_url(seriesName, episodeNum)
    html = send_request(manga_url).text

    return NOT_AVAILABLE in html

# Check to see if the manga name is correct or wrong
def not_found(seriesName, episodeNum):
    manga_url = get_page_url(seriesName, episodeNum)
    html = send_request(manga_url).text

    return NOT_FOUND in html


# Download the image to the hard drive
def download_img(url, download_path, page):
    # Create the download path if it doesn't exist
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # Assemble the page's image file path
    img_name = add_zeros(str(page)) + FILE_EXT
    img_path = download_path + img_name

    # Make a request but get binary data
    # Also, wait until it finishes downloading
    request = send_request(url, True)

    # Create a binary file with an image extension
    # Get the decoded contents of the image stream
    # Copy them to the image path that we constructed
    with open(img_path, 'wb') as file_path:
        request.raw.decode_content = True
        shutil.copyfileobj(request.raw, file_path)

    print(DOWNLOADING_MESSAGE + str(page))