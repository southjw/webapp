#import os
#def getEncodeStr(word,val='utf-8'):
#    if os.name=='nt':
#        wtemp=u'wtemp'
#        if type(word)==type(wtemp):
#            disvalue=word
#        else:
#            disvalue=unicode(word, 'mbcs')
#        if val.lower()!='utf-8':
#            try:
#                tdv=disvalue.encode(val)
#            except:
#                tdv=disvalue.encode('utf-8')
#        else:
#            tdv=disvalue.encode(val)
#        return tdv
#    else:
#        return word


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = ('<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web'))
    return [body.encode('utf-8')]
