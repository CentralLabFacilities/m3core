#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 15:19:50 2014

@author: Guillaume Walck
based on code m3dev_monitor.py
@author: Antoine Hoarau
"""
import m3.rt_proxy as m3p

proxy = m3p.M3RtProxy()
proxy.start()
proxy.make_operational_all()
proxy.make_operational_all_shm()
proxy.stop()

print 'Exit'
