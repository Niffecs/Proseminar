#!/usr/bin/env python3

import os 
import ftplib
import sys

# Load env
FILE = sys.argv[1]
HOST = os.environ["FTP_SERVER"]
USER = os.environ["FTP_USER"]
PWD  = os.environ["FTP_PWD"]


# Test PDF 
if not "pdf" in FILE: 
    print("no pdf")
    sys.exit(-1)
    
# FTP Gedoens
ftp = ftplib.FTP(HOST, USER, PWD)
ftp.encoding = "utf-8"
with open(FILE, "rb") as file:
    ftp.storbinary(f"STOR {FILE}", file)