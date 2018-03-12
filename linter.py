#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Kyle Chisholm
# Copyright (c) 2016 Kyle Chisholm
#
# License: MIT
#

"""This module exports the AvrGcc plugin class."""

import shlex
from SublimeLinter.lint import Linter, util


class AvrGcc(Linter):
    """Provides an interface to avr-gcc."""

    syntax = ('c', 'c++', 'c++11')
    executable = 'avr-gcc'

    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 4.0'

    # 1. column number, colon and space are only applicable for single line
    #    messages
    # 2. several lines of anything followed by
    #    either error/warning/note or newline (= irrelevant backtrace content)
    #    (lazy quantifiers so we don’t skip what we seek)
    # 3. match the remaining content of the current line for output
    regex = (r'<stdin>:(?P<line>\d+):'
             r'((?P<col>\d*): )?'
             r'(.*?((?P<error>error)|(?P<warning>warning|note)|\r?\n))+?'
             r': (?P<message>.+)')

    multiline = True

    defaults = {
        'include_dirs': [],
        'extra_flags': "",
        'extra_cflags': "",
        'extra_cxxflags': ""
    }

    base_cmd = 'avr-gcc -fsyntax-only -Wall '

    error_stream = util.STREAM_BOTH
    tempfile_suffix = None
    word_re = None
    inline_settings = None
    inline_overrides = None
    comment_re = None

    def cmd(self):
        """
        Return the command line to execute.

        We override this method, so we can add extra flags and include paths
        based on the 'include_dirs' and 'extra_flags' settings.

        """

        result = self.base_cmd
        settings = self.get_view_settings()

        if util.get_syntax(self.view) in ['c', 'c improved']:
            result += ' -x c ' + settings.get('extra_cflags', '') + ' '
        elif util.get_syntax(self.view) in ['c++', 'c++11']:
            result += ' -x c++ ' + settings.get('extra_cxxflags', '') + ' '
        result += settings.get('extra_flags', '')

        include_dirs = settings.get('include_dirs', [])
        if include_dirs:
            result += ' '.join(
                [' -I ' + shlex.quote(include) for include in include_dirs])

        return result + ' -'
