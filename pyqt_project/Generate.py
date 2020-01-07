
from os.path import join
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

from Ui_layout import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap

class Gen_Emails(QtWidgets.QMainWindow):
	def __init__(self):
		super(Gen_Emails, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

	def FindFiles(self, files, output):
		self.output = output
		for f in files:
			filename, file_extension = os.path.splitext(os.path.basename(f))
			html = codecs.open(f, 'r', 'utf-8')
			self.EmailGen(filename, html)

	def EmailGen(self, filename, html):
		data = []
		cid_list = []

		#find base64 img and replace
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

		#start generate message
		sender = ''
		recepiant = ''
		subject = filename

		msg = MIMEMultipart('mixed')
		msgImg = MIMEMultipart('related')

		msg['Subject'] = subject
		msg['From'] = sender
		msg['To'] = recepiant

		#html
		part = MIMEText(html, 'html')

		msgImg.attach(part)

		#image
		for i, img in enumerate(data, start=0):
			fp = base64.b64decode(img.split(',')[1])
			msgImage = MIMEImage(fp, _subtype='png')
			msgImage.add_header('Content-ID', cid_list[i])
			msgImg.attach(msgImage)

		msg.attach(msgImg)

		self.SaveToFile(msg, subject)

	def SaveToFile(self, msg, filename):
		file = filename + '.eml'
		with open(join(self.output, file), 'w') as outfile:
			gen = generator.Generator(outfile)
			gen.flatten(msg)