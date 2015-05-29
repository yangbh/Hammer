#!/usr/bin/python2.7
#coding:utf-8

from consoleColor_class   import *
from os         import path,system
from pluginLoader_class import PluginLoader

from dummy import BASEDIR

class m:
	'''mst plugin's class'''
	def __init__(self,name):
		'''exec plugin code'''
		self.pluginPath = BASEDIR + '/' + name
		self.plugin = PluginLoader()
		self.services = {}

		self.pluginOpts = self.plugin.getPluginOpts(self.pluginPath)
		print self.pluginOpts
		self.pluginInfo = self.plugin.getPluginInfo(self.pluginPath)
		
		# for t in self.pluginOpts:
		# 	o=t[0]
		# 	v=t[1]
		# 	# print o,v
		# 	if type(v)!=int:
		# 		# print type(v)
		# 		if(v[0]=='[' and v[-1] == ']') or (v[0]=='{' and v[-1] == '}'):
		# 			v = eval(v)
		# 			# print v
		# 	self.services[o] = v
		# 	# print self.services

		self.services.update(self.pluginOpts)
		# for key in self.pluginOpts:
		# 	if key in ('url','ip','host','timeout'):
		# 		self.services[key] = self.pluginOpts[key]

		# print 'done'

	def info(self):
		'''display plugin infos'''
		color.cprint("PLUGIN INFOS",YELLOW)
		color.cprint("============",GREY)
		color.cprint("PARAMETER       VALUE",YELLOW)
		color.cprint("-"*15+" "+"-"*20,GREY)
		for key in self.pluginInfo.keys():
			p=key
			v=self.pluginInfo[p]
			color.cprint("%-15s"%p,CYAN,0)
			color.cprint("%-s"%v,PURPLE)

	def opt(self):
		'''display plugin opts'''
		# print self.pluginOpts
		color.cprint("PLUGIN OPTS",YELLOW)
		color.cprint("===========",GREY)
		color.cprint("%-15s %-20s %-40s"%("PARAMETER","VALUE","DESCRIPTION"),YELLOW)
		color.cprint("%-15s %-20s %-40s"%("-"*15,"-"*20,"-"*40),GREY)
		# for n in self.pluginOpts:
		# 	p=n[0]
		# 	v=n[1]
		# 	d=n[2]
		# 	color.cprint("%-15s"%p,CYAN,0)
		# 	color.cprint("%-20s"%self.services[p],PURPLE,0)
		# 	color.cprint("%-40s"%d,GREEN)

		for key in self.pluginOpts.keys():
			p=key
			color.cprint("%-15s"%p,CYAN,0)
			color.cprint("%-20s"%self.pluginOpts[p],PURPLE)

	def setp(self,p,v):
		'''set plugin par value'''
		# p=p.upper()
		if self.pluginOpts.has_key(p):
			color.cprint("[*] SET %s=>%s"%(p,v),YELLOW)
			value = eval(v) if (v[0]=='[' and v[-1] == ']') or (v[0]=='{' and v[-1] == '}') else v
			self.pluginOpts[p] = value
			self.services[p] = value
			print self.pluginOpts
		else:
			color.cprint("[*] NO PARA %s" % p,YELLOW)

	def run(self):
		'''start run !!'''
		try:
			color.cprint("[*] Start run..",YELLOW)
			self.plugin.runAudit(self.pluginPath, self.pluginOpts, self.services)
		except Exception,e:
			color.cprint("[!] Err:%s"%e,RED)

	def printp(self,pt,plu):
		'''plugin color input'''
		ptmp=plu.split("/")
		pplu=plu[len(ptmp[0])+1:]
		color.cprint("hammer",GREY,0)
		color.cprint("%s["%pt,WHITE,0)
		color.cprint(pplu,RED,0)
		color.cprint("]",WHITE,0)

	def pluhelp(self):
		'''plugin help menu'''
		color.cprint('PLUGIN HELP MENU',YELLOW)
		color.cprint('================',GREY)
		color.cprint('        Command         Description',YELLOW)
		color.cprint('        -------         -----------',GREY,0)
		color.cprint('''
	help            Displays the plugin menu
	back            Back to Mst Main
	cls             Clear the screen
	info            Displays the plugin info
	opts            Displays the mst options
	set             Configure the plugin parameters
	run             Start plugin to run''',CYAN)
		color.cprint('PLUGIN SET HELP',YELLOW)
		color.cprint('===============',GREY)
		color.cprint('        Command         Description',YELLOW)
		color.cprint('        -------         -----------',GREY,0)
		color.cprint('''
	<PARAMETER>     Set parameter''',CYAN)
	def cls(self):
		'''clear the screen'''
		if  name == 'nt':
			system("cls")
		else:
			system("clear")
	def load(self):
		color.cprint("[?] USAGE::load <loadPlu>",YELLOW)
# ----------------------------------------------------------------------------------------------------
# 
# ----------------------------------------------------------------------------------------------------
import sys
sys.path.append(BASEDIR+'/plugin')
if __name__ == '__main__':
	pluginpath = 'System/iismethod'
	if len(sys.argv) ==  2:
		pluginpath = sys.argv[1]
	pl = m(pluginpath)
