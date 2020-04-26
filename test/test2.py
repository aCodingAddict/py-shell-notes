#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author : XueKai_aCodingAddict
# @Time : 2019/11/8 5:19 下午

"""
DOCUMENT
"""

import os
import sys
import platform

this_dir_path = os.path.dirname(os.path.realpath(__file__))
if platform.platform().find("centos") > 0:
    my_site_path = this_dir_path + '/site-packages/centos'
else:
    my_site_path = this_dir_path + '/site-packages/redhat'
sys.path.append(my_site_path)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bdg.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
