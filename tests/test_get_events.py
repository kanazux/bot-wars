#!/usr/bin/python3.6


import re
from unittest import TestCase, main
from bot_wars.get_events import list_events


class testGetEvents(TestCase):
    def test_get_events(self):
        self.assertIsInstance(list_events(), (str))

    def test_regex_events(self):
        pattern = re.compile(r"(.*\n){4}.*")
        self.assertTrue(pattern.match(list_events()))


if __name__ == "__main__":
    main()
