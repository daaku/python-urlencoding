# coding: utf-8

import unittest
import urlencoding


class TestParseQS(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(urlencoding.parse_qs('a=1'), {'a': '1'})

    def test_multi(self):
        self.assertEqual(urlencoding.parse_qs('a=1&b=2'), {'a': '1', 'b': '2'})

    def test_space(self):
        self.assertEqual(
            urlencoding.parse_qs('a=1&b=2&c=%20d'),
            {'a': '1', 'b': '2', 'c': ' d'}
        )

    def test_square_index(self):
        self.assertEqual(
            urlencoding.parse_qs('a%5Bb%5D=1&a%5Bc%5D=2'),
            {'a[b]': '1', 'a[c]': '2'}
        )

    def test_array_value(self):
        self.assertEqual(
            urlencoding.parse_qs('a=1&a=2'),
            {'a': ['1', '2']}
        )
