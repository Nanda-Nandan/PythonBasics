import urllib.request
import sys
if len(sys.argv)!=3:
    raise SystemExit('enter route and stopid')
route =sys.argv[1]
stopid=sys.argv[2]
u=urllib.request.urlopen('website which will return xml file according to query params ex-metrozip.com route = {} & stop={}'.format(route,stopid))
data=u.read()
from xml.etree.ElementTree import XML
doc=XML(data)
for node in doc.findall('.//tag'):
    print(node.text)
import pdb;pdb.set_trace() #will launch debugger and take the control to error line,u can write it manually in the code before running,so that control will stop at this point of code,so that u can debug


