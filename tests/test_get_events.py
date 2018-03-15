#!/usr/bin/python3.6


import re
from unittest import TestCase, main
from bot_wars.tools import get_events


pattern = re.compile(r"[.*\n]{5}")


class testGetEvents(TestCase):
    def test_get_events(self):
        self.assertTrue(pattern.match(get_events()))


if __name__ == "__main__":
    main()
