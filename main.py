# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import praw

class bot(object):
	def __init__(self, username, password):
		self.username = username
		self.password = password
