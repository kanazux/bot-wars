#!/usr/bin/python3.6


from unittest import TestCase, main
from bot_tools.get_events import list_events


class testGetEvents(TestCase):
    def test_get_events(self):
        self.assertIsInstance(list_events(), (str))


if __name__ == "__main__":
    main()
