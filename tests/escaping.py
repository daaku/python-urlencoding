# coding: utf-8

import unittest
from urlencoding import escape


class TestEscape(unittest.TestCase):
    def test_no_escaping(self):
        self.assertEqual(escape('abcd'), 'abcd')

    def test_space(self):
        self.assertEqual(escape(' '), '%20')

    def test_alphanumeric(self):
        alpha_num = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.assertEqual(escape(alpha_num), alpha_num)

    def test_urlencoding_mentioned_specials(self):
        mentioned = '-._~'
        self.assertEqual(escape(mentioned), mentioned)

    def test_percent(self):
        self.assertEqual(escape('%'), '%25')

    def test_plus(self):
        self.assertEqual(escape('+'), '%2B')

    def test_amp(self):
        self.assertEqual(escape('&'), '%26')

    def test_equal(self):
        self.assertEqual(escape('='), '%3D')

    def test_star(self):
        self.assertEqual(escape('*'), '%2A')

    def test_line_feed(self):
        self.assertEqual(escape(u'\u000A'), '%0A')

    def test_unicode_space(self):
        self.assertEqual(escape(u'\u0020'), '%20')

    def test_seven_f(self):
        self.assertEqual(escape(u'\u007F'), '%7F')

    #FIXME: these currently fail
    def test_eighty(self):
        self.assertEqual(escape(u'\u0080'), '%80')

    def test_three_thousand_one(self):
        self.assertEqual(escape(u'\u3001'), '%E3%80%81')
