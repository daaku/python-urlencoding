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
