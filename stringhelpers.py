from settings import *  # Global constants
import re  # Deals with RegExp


# Assemble the path of the folder to download the episode
def get_download_path(seriesName, episodeNum):
    return LOCAL_PATH + seriesName + "/" + episodeNum + "/"


# Assemble the url of the page (the website's html)
def get_page_url(seriesName, episodeNum, pageNum = 1):
    return PROVIDER + dashes(seriesName) + "/" + str(episodeNum) + "/" + str(pageNum)


# Get correct url slug (lowercased with dashes)
def dashes(seriesName):

    return "-".join(seriesName.split(" ")).lower() # Separate by a space and join with a dash


# Add zeros to the prefix of page number
def add_zeros(pageNum):
    digits = len(pageNum)  # pageNum is a string
    zeros = "0" * (ESTIMATED_MAX_DIGITS - digits)

    return zeros + pageNum