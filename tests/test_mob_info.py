from unittest import TestCase, main
from collections import defaultdict
from bot_wars.mob_info import get_info


class testMobInfo(TestCase):
    def test_mob_info(self):
        self.assertIsInstance(get_info('rinoceronte'), (defaultdict))


if __name__ == "__main__":
    main()
