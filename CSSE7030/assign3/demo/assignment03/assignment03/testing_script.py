#!/usr/bin/env python3
# coding:utf-8
from back_end import BackEndManager
from better_controller import Controller
import pprint
manager = BackEndManager()
print(manager.get_active_data(type='quick'))