#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""Part of bot wars."""


from requests_html import HTMLSession


def get_events():
    """Get events of summoners wars."""
    u = 'https://forum.com2us.com/forum/main-forum/summoner-s-war/events-ab'
    s = HTMLSession
    r = s.get(u)
    events = "\n".join([
        x.text for x in r.find("a.topic-title")[:5]])

    return events


if __name__ == "__main__":
    print(get_events())
