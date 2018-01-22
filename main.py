# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import praw
import base64

USERNAME = "WSBTip"
PASSWORD = base64.b64decode(open("../../Password.txt").read())
# Not going to post the password in plain text

class bot(object):
	def __init__(self, username, password):
		self.username = username
		self.password = password



if __name__ == '__main__':
	WSBbot = bot(USERNAME, PASSWORD)