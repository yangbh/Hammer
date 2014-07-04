#!/usr/bin/python2.7
#coding:utf-8
import os
import sys
import re
services={u'106.187.37.47': {'status': {'state': u'up', 'reason': u'reset'}, 'hostname': u'li380-47.members.linode.com', 'vendor': {}, 'addresses': {u'ipv4': u'106.187.37.47'}, u'tcp': {80: {'product': u'nginx', 'state': u'open', 'version': '', 'name': u'http', 'conf': u'10', 'extrainfo': '', 'reason': u'syn-ack', 'cpe': u'cpe:/a:igor_sysoev:nginx'}}}}

sys.path.append('plugins')
importcmd = 'from http.robots import *'
exec(importcmd)

if globals().has_key('Assign'):
	print 'Plugin function Assign loaded'
	Assign()
if globals().has_key('Audit'):
	print 'Plugin function Audit loaded'
	Audit(services)