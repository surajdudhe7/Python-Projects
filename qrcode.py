import pyqrcode 
from pyqrcode import QRCodes
s="https:/www.youtube.com"
a=pyqrcode.create(s)
a.svg(suraj.svg,scale=10)