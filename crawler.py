# -*- coding: utf-8 -*-

import re
import requests
import string
from typing import NamedTuple
from bs4 import BeautifulSoup


AZCHORD_URL = "http://www.azchords.com"

class Artist(NamedTuple):
    artist: str
    url: str


def get_artist_links(alphabet):
    counter = 1
    prev_item_div = None

    while True:
        page = "{}/{}_page_{}.html".format(AZCHORD_URL, alphabet, counter)
        print(page)
        req = requests.get(page)
        html = req.content

        soup = BeautifulSoup(html, 'html.parser')
        item_div = str(soup.find("div", {"class": "items"}))

        if item_div == prev_item_div:
            break
        prev_item_div = item_div

        processed_item_div = item_div.replace(' rel="noindex, follow"', "")
        url_artist_list = re.findall(r'<a href="(.*?)">(.*?)</a>', processed_item_div)
        for url, artist in url_artist_list:
            yield Artist(artist, "{}{}".format(AZCHORD_URL, url))

        counter += 1


def get_song_links(url):
    req = requests.get(url.replace("tabs", "chords"))
    html = req.content

    soup = BeautifulSoup(html, 'html.parser')
    item_div = str(soup.find("div", {"class": "items"}))
    for x in re.findall(r'<tr class="rowlink clickable".*?>(.*?)</tr>', item_div):
        print(x)
    return

    page = "http://www.azchords.com/" + link.replace('tabs','chords')
    html = urllib2.urlopen(page).read().replace('\n',' ')

    links = []

    for x in re.findall(r'<tr class="rowlink clickable".*?>(.*?)</tr>', html):
        for link in re.findall(r'<a href="(.*?)">',html):
            links.append(link)

    return links


def scrape():
    for alphabet in string.ascii_lowercase:
        for artist_obj in get_artist_links(alphabet):
            get_song_links(artist_obj.url)


if __name__=="__main__":
    scrape()
