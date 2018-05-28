# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import os
import sys


def get_programname(module, command):
    module_name = module.split('.')[-1]
    return '{} {} {}'.format(os.path.basename(sys.argv[0]), module_name, command)


class CommandWrapper:
    def __init__(self, parser, func):
        self.parser = parser
        self.func = func
        self.doc = func.__doc__
        self.name = func.__name__
        self.module = func.__module__
        self.parser.description = self.doc
        self.parser.prog = get_programname(self.module, self.name)

    def call(self, args):
        args = self.parser.parse_args(args)
        self.func(args)


def cmd(parser):
    def decorator(func):
        return CommandWrapper(parser, func)
    return decorator