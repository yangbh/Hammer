# -*- coding: utf-8 -*-
import unittest

# From http://www.iana.org/domains/root/db
GENERAL_TLD = ['com','edu','gov','net','org','mil','travel','aero',
			   'asia','cat','coop','int','jobs','mobi','museum','post',
			   'tel','xxx','pro','arpa']

REGOIN_TLD  = { "cn": ['xj', 'sh', 'ac', 'gs', 'zj', 'yn', 'ah', 'gz', 
					   'bj', 'gx', 'jl', 'hk', 'gd', 
					   'hn', 'hl', 'edu', 'hb', 'cq', 'ha', 'fj', 'he',
					   'xz', 'sx', 'jx','ln', 'tw', 
					   'mo', 'js', 'nx', 'hi', 'tj', 'sn', 'nm', 'sc', 'qh',
					   'sd'],
				"tw": ['idv','game','club','ebiz'],
				"hk": ['idv'],
			}

def GetFirstLevelDomain(raw_host=""):
	''' '''
	raw_host.lower()
	port = 80
	if ":" in raw_host:
		try:
			(host, port) = raw_host.split(':')
		except ValueError:
			raise ValueError('Too many ":" in %s' % raw_host)
	else:
		host = raw_host
	
	rev = host.split(".")[::-1]
	
	if rev[0] in GENERAL_TLD:
		rev = rev[:2]
	elif len(rev[0].decode('utf-8')) == 2:
		if rev[1] in GENERAL_TLD+REGOIN_TLD.get(rev[0], []):
			rev = rev[:3]
		else:
			rev = rev[:2]
	else:
		return None

	return ".".join(rev[::-1])

def GetSmartDomain(raw_host=''):
	firstdomain = GetSmartDomain(raw_host)
	tp = raw_host - firstdomain
	if len(tp):
		tlist = tp.split(tp[:-1])
		if len(tlist) >1:
			tlist = tlist[1:]
			tmp = '.'.join(tlist[1:]) + '.'
			return tmp + firstdomain
	return firstdomain
	
class DomainTest(unittest.TestCase):
   
	def test_base_function(self):
		self.assertEqual(GetFirstLevelDomain('www.google.com'), 'google.com')

	def test_g_tld(self):
		tlds = ['subdomain.china.asia',
				'4th.www.float.int',
				'e.pypi.python.org']

		match = ['china.asia','float.int','python.org']

		self.assertEquals([GetFirstLevelDomain(t) for t in tlds], match)

	def test_special_cctld(self):

		self.assertEqual(GetFirstLevelDomain('www.gx.cn'), 'www.gx.cn')

	def test_cjk_domain(self):
		
		self.assertEqual(GetFirstLevelDomain('www.g.中国'), 'g.中国')

	def test_domain_with_port(self):
		self.assertEqual(GetFirstLevelDomain('del.icio.us:8080'), 'icio.us')

	def test_bad_domain(self):
		self.assertIsNone(GetFirstLevelDomain('i-am.b_ad.domain'))

if __name__ == '__main__':
	unittest.main()
