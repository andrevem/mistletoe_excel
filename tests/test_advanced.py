# -*- coding: utf-8 -*-

from .context import mistletoe_excel

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(mistletoe_excel.hmm())


if __name__ == '__main__':
    unittest.main()
