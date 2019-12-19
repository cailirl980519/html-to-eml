from os import listdir
from os.path import isfile, isdir, join
import os
from email import generator
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import make_msgid
from bs4 import BeautifulSoup
import codecs
import base64
import smtplib

class Gen_Emails(object):
	def __init__(self):
		self.send = 1
		self.path = os.path.dirname(__file__)
		self.output = os.path.dirname(__file__)
		self.recepiant = '123@xyz.com'
		self.option()

	def option(self):
		print (self.path)
		print('1.Save as .eml\n')
		print('2.Send email\n')
		print('3.Above both\n')
		self.send = input('Enter option:') 
		if(int(self.send)>3):
			print('Error')
		else:
			self.FindFiles()

	def FindFiles(self):
		self.path = input('Enter path:')
		if(int(self.send) == 1 or int(self.send) == 3):
			self.output = input('Enter output path:')
		if(int(self.send) == 2 or int(self.send) == 3):
			self.recepiant = input('Enter Email address:')
		if os.path.isdir(self.path):
			files = listdir(self.path)
			for f in files:
				# 產生檔案的絕對路徑
				fullpath = join(self.path, f)
				# 判斷 fullpath 是檔案還是目錄
				if isfile(fullpath) and 'html' in f:
					if not("._" in f):
						html = codecs.open(fullpath, 'r', 'utf-8')
						filename, file_extension = os.path.splitext(f)
						self.EmailGen(filename, html)
		else:
			filename, file_extension = os.path.splitext(os.path.basename(self.path))
			html = codecs.open(self.path, 'r', 'utf-8')
			self.EmailGen(filename, html)	

	def EmailGen(self, filename, html):
		data = []
		cid_list = []
		
		soup = BeautifulSoup(html, 'html.parser')
		img_tag = soup.find_all('img')
		for tag in img_tag:
			try:
				src = tag['src']
			except:
				pass
			if 'data:image' in src:
				data.append(src)
				cid = make_msgid(domain='yahoo.com.tw')[1:-1]
				cid_list.append(cid)
				tag['src'] = "cid:{}".format(cid)

		html = soup.prettify()

		sender = ''
		recepiant = ''
		subject = filename

		msg = MIMEMultipart('mixed')
		msgImg = MIMEMultipart('related')		

		part = MIMEText(html, 'html')

		msgImg.attach(part)

		for i, img in enumerate(data, start=0):
			fp = base64.b64decode(img.split(',')[1])
			msgImage = MIMEImage(fp, _subtype='png')
			msgImage.add_header('Content-ID', cid_list[i])
			msgImg.attach(msgImage)

		msg.attach(msgImg)

		if(int(self.send) == 1 or int(self.send) == 3):
			msg['Subject'] = subject
			msg['From'] = sender
			msg['To'] = recepiant
			self.SaveToFile(msg, subject)
		if(int(self.send) == 2 or int(self.send) == 3):
			msg['Subject'] = subject
			self.Send(msg)

	def SaveToFile(self, msg, filename):
		file = filename + '.eml'
		with open(join(self.output, file), 'w') as outfile:
			gen = generator.Generator(outfile)
			gen.flatten(msg)

	def Send(self, msg):
		try:
			msg['From'] = 'd1997721@yahoo.com.tw'
			msg['To'] = self.recepiant
			s = smtplib.SMTP('smtp.mail.yahoo.com:587')
			s.starttls()
			s.login('d1997721@yahoo.com.tw',"D_a_n_i_e_l_19")
			s.sendmail('d1997721@yahoo.com.tw', self.recepiant, msg.as_string())
			s.quit()
			print('success')
		except smtplib.SMTPException:
			print('Error')

x = Gen_Emails()