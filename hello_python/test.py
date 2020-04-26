#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author : XueKai_aCodingAddict
# @Time : 2019/10/25 6:20 下午

"""
DOCUMENT
"""

# import os
# import re
# import sys
# import commands

# workDir = os.path.dirname("baidu/dpfop/qianxun/cc/CI_TOOLS/deploy")
# print("workDir:  " + workDir)
# name = "AFS-AGENT"
# print("name:  " + name)
# metaDir = os.path.join(workDir, "..", name, "meta_file")
# print("metaDir:  " + metaDir)
# cmd_job_name = "echo %s | cut -d '/' -f2" % workDir

# cmd = commands.getoutput(cmd_job_name)

# print("cmd: " + cmd)

# print(commands.getoutput("echo %s" % metaDir))

list1 = [8, 2, 7, 9, 11]


def twoSum(nums, target):
    hash_map = dict()
    for i, x in enumerate(nums):
        print(i, ":", x)
        if target - x in hash_map:
            for m in hash_map.items():
                print("======")
                print(m)
                print("======")
            return [i, hash_map[target - x]]
        hash_map[x] = i


result = twoSum(list1, 9)
