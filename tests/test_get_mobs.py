from unittest import TestCase, main
from bot_tools.get_mobs import list_mobs
from collections import defaultdict


class testListMobs(TestCase):
    def test_list_mobs(self):
        self.assertIsInstance(list_mobs(), (defaultdict))


if __name__ == "__main__":
    main()
