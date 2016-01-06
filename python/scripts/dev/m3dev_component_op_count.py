#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Nov 2015

@author: CLF
"""
import m3.rt_proxy as m3p
proxy = m3p.M3RtProxy()
proxy.start()
print proxy.get_num_operational_components()
proxy.stop()
