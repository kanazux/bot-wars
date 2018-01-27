#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup as bs


def get_events():
    events_data = bs(requests.get(
      'https://forum.com2us.com/forum/main-forum/summoner-s-war/events-ab').text, "html.parser")

    events = "\n".join([
      x.text for x in events_data.findAll("a") if 'class' in x.attrs
      if " ".join(x.attrs['class']) == "topic-title js-topic-title"][:4])

    return events

if __name__ == "__main__":
    print get_events()
