# adds example.org/file to download queue
import urllib2, json
jsonreq = json.dumps({'jsonrpc':'2.0', 'id':'qwer',
    'method':'aria2.addUri',
    'params':[['http://example.org/file']]})
c = urllib2.urlopen('http://localhost:6800/jsonrpc', jsonreq)
c.read()
'{"id":"qwer","jsonrpc":"2.0","result":"2089b05ecca3d829"}'
