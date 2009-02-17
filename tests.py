# coding: utf-8

import unittest
import urlencoding


class TestEscape(unittest.TestCase):
    def test_no_escaping(self):
        self.assertEqual(urlencoding.escape('abcd'), 'abcd')

    def test_space(self):
        self.assertEqual(urlencoding.escape(' '), '%20')

    def test_alphanumeric(self):
        alpha_num = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.assertEqual(urlencoding.escape(alpha_num), alpha_num)

    def test_urlencoding_mentioned_specials(self):
        mentioned = '-._~'
        self.assertEqual(urlencoding.escape(mentioned), mentioned)

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

class TestComposeQS(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(urlencoding.compose_qs({'a': '1'}), 'a=1')

    def test_array(self):
        self.assertEqual(urlencoding.compose_qs({'a': ['2', '1']}), 'a=2&a=1')

    def test_sorted_array(self):
        self.assertEqual(urlencoding.compose_qs({'a': ['2', '1']}, sort=True), 'a=1&a=2')

    def test_sorted_dict(self):
        self.assertEqual(urlencoding.compose_qs({'a': {'b': '1', 'c': '2'}}, sort=True), 'a%5Bb%5D=1&a%5Bc%5D=2')

if __name__ == '__main__':
    unittest.main()