from os import listdir
from os.path import isfile, isdir, join
from email import generator
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import codecs
import re

class Gen_Emails(object):
    def __init__(self):
        pass

    def FindFiles(self):
        path = input('Enter folder path:')
        outputpath = input('Enter output path:')
        files = listdir(path)
        for f in files:
            # 產生檔案的絕對路徑
            fullpath = join(path, f)
            # 判斷 fullpath 是檔案還是目錄
            if isfile(fullpath) and 'html' in f:
                if not("._" in f):
                    self.EmailGen(fullpath, f, outputpath)

    def EmailGen(self, path, filename, output):
        sender = ''
        recepiant = ''
        subject = filename.replace('.html','')

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recepiant

        html = codecs.open(path, 'r', 'utf-8')
        # html = """\
        # <html>
        #     <head></head>
        #     <body>
        #         <p> hello world </p>
        #     </body>
        # </html>
        # """
        part = MIMEText(html.read(), 'html')

        msg.attach(part)

        self.SaveToFile(msg, subject, output)

    def SaveToFile(self,msg,filename,output):
        file = filename + '.eml'
        with open(join(output, file), 'w') as outfile:
            gen = generator.Generator(outfile)
            gen.flatten(msg)

x = Gen_Emails()
x.FindFiles()