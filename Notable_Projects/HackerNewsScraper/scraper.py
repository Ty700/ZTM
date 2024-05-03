#####################################################################################
# Usage:                                                                            #
#   Scrapes Hacker News for top stories based on user-defined number of pages.      #
#   Optionally, user can specify the number of pages to scrape. Default is 1.       #
#                                                                                   #
# How to use:                                                                       #
#   # Run the script with optional argument for number of pages.                    #
#                                                                                   #
#   Example:                                                                        #
#       python3 scrape_hacker_news.py <amount_of_pages>                             #
#                                                                                   #
#####################################################################################


import requests
from bs4 import BeautifulSoup
import pprint
import sys

# BeautifulSoap allows us to use the HTML we requested and scrape it
# Requests allows us to download the HTML

def sort_stories_by_votes(links_list):
    return sorted(links_list, key=lambda k:k['votes'], reverse=True)

def filter_links(links, subtext):
    res = []

    for index, link in enumerate(links):
        title = link.getText()
        href = link.get('href', None)
        vote = subtext[index].select('.score')

        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                res.append({'title': title, 'link': href, 'votes': points})

    return res

def main(amount_of_pages):

    master_links = []

    for page_number in range(1, amount_of_pages + 1):
        
        res = requests.get('https://news.ycombinator.com/?p=' + str(page_number)) 

        soup = BeautifulSoup(res.text, 'html.parser')

        links = (soup.select('.titleline > a'))

        subtext = (soup.select('.subtext'))

        master_links.append(filter_links(links, subtext))   
    
    flattened_links = [item for sublist in master_links for item in sublist]

    pprint.pprint(sort_stories_by_votes(flattened_links))
    
if __name__ == '__main__':
    if len(sys.argv) == 1:
        amount_of_pages = 1
    else:
        amount_of_pages = int(sys.argv[1])

    if amount_of_pages < 1:
        amount_of_pages = 1
    elif amount_of_pages > 10:
        amount_of_pages = 10

    main(amount_of_pages)

