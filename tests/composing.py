# coding: utf-8

import unittest
import urlencoding


class TestComposeQS(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(urlencoding.compose_qs({'a': '1'}), 'a=1')

    def test_array(self):
        self.assertEqual(urlencoding.compose_qs({'a': ['2', '1']}), 'a=2&a=1')

    def test_sorted_array(self):
        self.assertEqual(urlencoding.compose_qs({'a': ['2', '1']}, sort=True), 'a=1&a=2')

    def test_sorted_dict(self):
        self.assertEqual(urlencoding.compose_qs({'a': {'b': '1', 'c': '2'}}, sort=True), 'a%5Bb%5D=1&a%5Bc%5D=2')
