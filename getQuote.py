'''
Get quote data from 126.net.
'''
import urllib

def getQuote(ids ='1150153'):
        
    try:
        def _ntes_quote_callback(dct):
            global jk_quote_d_res # any better way to return dct? pure return doesn't work
            jk_quote_d_res = dct
        
        url = "http://api.money.126.net/data/feed/{ids}".format(ids=ids)
        req = urllib.request.Request(url)
        res = urllib.request.urlopen(req)
        data = res.read()
        exec(data.decode())
	d = jk_quote_d_res
	jk_quote_d_res = None
        return d
    
    except Exception as e:
        print(str(e))
