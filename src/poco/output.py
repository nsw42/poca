#!/usr/bin/env python2
# 
# Copyright 2010-2015 Mads Michelsen (mail@brokkr.net)
# 
# This file is part of Poca.
# Poca is free software: you can redistribute it and/or modify it 
# under the terms of the GNU General Public License as published by 
# the Free Software Foundation, either version 3 of the License, 
# or (at your option) any later version.


import logging


color_codes = { 
    'reset': '\033[0;0m',
    'bold': '\033[1m',
    'red': '\033[31m',
    'green': '\033[32m',
    'blue': '\033[34m',
    'lred': '\033[1;31m',
    'lgreen': '\033[1;32m',
    'yellow': '\033[1;33m',
    'lblue': '\033[1;34m'
    }

class Outcome:
    def __init__(self, success, msg = ''):
        self.success = success
        self.msg = msg

class Out:
    def __init__(self, args):
        self.log = get_logger(args)

    def single(self, msg):
        self.log.info(msg)

    def cols(self, msg1, msg2):
        msg = (msg1[0:60] + ' ').ljust(63, '.') + ' ' + msg2
        self.log.info(msg)

    def head(self, msg):
        self.log.info(msg.upper())

def colorize(_string, color):
    return color_codes[color] + str(_string) + color_codes['reset']

def get_logger(args):
    logger = logging.getLogger('POCA')
    logger.setLevel(logging.INFO)
    null_handler = logging.NullHandler()
    logger.addHandler(null_handler)
    if not args.quiet:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_formatter = logging.Formatter("%(message)s")
        stream_handler.setFormatter(stream_formatter)
        logger.addHandler(stream_handler)
    if args.log_errors:
        file_handler = logging.FileHandler(paths.errors)
        file_handler.setLevel(logging.ERROR)
        file_formatter = logging.Formatter("%(asctime)s - %(message)s", 
            datefmt='%Y-%m-%d %H:%M')
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
    return logger


