# -*- coding: utf-8 -*-

'''
Tests for rssgen main
'''

import os
import sys
import tempfile
import unittest

from rssgen import __main__


class TestSequenceFunctions(unittest.TestCase):

    def test_usage(self):
        sys.argv = ['rssgen']
        try:
            __main__.main()
        except BaseException as e:
            assert e.code is None

    def test_feed(self):
        for ftype in 'rss', 'atom':
            sys.argv = ['rssgen', ftype]
            try:
                __main__.main()
            except Exception:
                assert False

    def test_file(self):
        for extemsion in '.atom', '.rss':
            fh, filename = tempfile.mkstemp(extemsion)
            sys.argv = ['rssgen', filename]
            try:
                __main__.main()
            except Exception:
                assert False
            os.close(fh)
            os.remove(filename)
