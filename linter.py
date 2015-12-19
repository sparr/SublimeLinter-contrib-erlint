#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Clarence "Sparr" Risher sparr0@gmail.com
# Copyright (c) 2015 Clarence "Sparr" Risher sparr0@gmail.com
#
# License: MIT
#

"""This module exports the Erlint plugin class."""

from SublimeLinter.lint import Linter, util


class Erlint(Linter):
    """Provides an interface to erlint."""

    syntax = 'erlang'
    cmd = 'erlint'
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 0.1.0'

    # hello.erl:7: error: {unbound_var,'J'}
    # hello.erl:5: warning: {unused_var,'X'}
    regex = (
        r'^.+?:(?P<line>\d+): '
        r'(?:(?P<error>error)|(?P<warning>warning)): '
        r'(?P<message>.+)'
    )
    multiline = False

    line_col_base = (1, 1)
    tempfile_suffix = '.erl'
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None

