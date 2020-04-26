#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author : XueKai_aCodingAddict
# @Time : 2019/11/7 6:30 下午

"""
DOCUMENT
"""

import sys
import os
import MySQLdb
import datetime


class BigreportMonitor(object):
    """
    核心大报表监控
    """

    def __init__(self):
        """
        初始化核心报表列表
        """
        self.bigreport_list = {
            'psubs_bigreport_monitor': ['05:30', 'PS-UBS天级报表'],
            'lingxi_bigreport_monitor': ['10:00', '灵犀核心数据'],
            'fc_bigreport_monitor': ['10:00', 'FC核心KPI报表'],
            'lbs_bigreport_monitor': ['12:00', 'LBS核心报表'],
            'psubs_bigreport_monitor': ['12:00', 'PS-UBS天级报表'],
            'searchbox_bigreport_monitor': ['10:00', '框核心报表'],
            'mobilehelper_bigreport_monitor': ['12:00', '手助核心报表'],
            'feed_bigreport_monitor': ['10:00', 'feed核心报表'],
            'fenrun_bigreport_monitor': ['07:30', '分润核心报表'],
            'fcearly_bigreport_monitor': ['08:00', 'FC早报'],
            'psanti_bigreport_monitor': ['10:00', 'PS反劫持报表'],
            'ps_bigreport_monitor': ['10:00', 'PS核心报表'],
            'wise_bigreport_monitor': ['10:00', 'Wise核心报表'],
            # 'wise_bigreport_monitor' : ['10:00', 'Wise核心报表'],
            # 'fc_layer3_bigreport_monitor' : ['11:00', 'FC分析报表']
            'fc_layer3_bigreport_monitor': ['09:00', 'FC分析报表']
        }

    def check_daily_track(self, base_time):
        bigreport_info = self.bigreport_list
        for graph_name in bigreport_info:
            info = self.get_graph_instance_status(graph_name, base_time)
            if not info:
                finish_time = None
            else:
                finish_time = info[0][2]
            # base_time = info[0][1]
            if finish_time is None:
                status = 1
                finish_time = 0
            else:
                status = 2
            # base_time = datetime.datetime.fromtimestamp(int(base_time))
            finish_time = datetime.datetime.fromtimestamp(int(finish_time)).strftime("%Y-%m-%d %H:%M")
            bigreport_info[graph_name].append(status)
            bigreport_info[graph_name].append(base_time)
            bigreport_info[graph_name].append(finish_time)
        return bigreport_info

    def get_graph_instance_status(self, graph_name, base_time):
        db = MySQLdb.connect(user='dataflow', db='dashboard', passwd='dataflow-panhong', \
                             host='10.151.36.18', port=3306)
        cursor = db.cursor()
        sql = "select table_name, base_time, finish_time  from dataflow_table_time where \
                table_name = '%s' and base_time = '%s';" % (graph_name, base_time)
        cursor.execute(sql)
        info = cursor.fetchall()
        return info
# monitor = BigreportMonitor()
# status = monitor.check_daily_track('2015-10-08 00:00:00')
# print status
