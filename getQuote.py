'''
Get quote data from 126.net.
'''
import urllib

def getQuote(ids, d={}):
    try:
        def _ntes_quote_callback(dct):   
            d['q'] = dct
            
        url = "http://api.money.126.net/data/feed/{ids}".format(ids= ids)
        req = urllib.request.Request(url)
        res = urllib.request.urlopen(req)
        exec(res.read().decode()) # should be better way there
        return d['q']
    
    except Exception as e:
        print(str(e))
