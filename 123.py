#coding=utf-8
import urllib
import urllib2
import xml.dom.minidom
import time
import HTMLParser 
import win32api,win32con  
#import easygui 

def getHtml(url):
    req = urllib2.Request(url)
    req.add_header('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
    res = urllib2.urlopen(req)
    html = res.read()
    return html
    
def getTime(html):
    p_tpc_pos = html.find(r'class="f10"')
    
    if p_tpc_pos < 0 :
        pass
    else:
        sThString = html[0:p_tpc_pos]
        sth = sThString.rfind(r'<a ')
        #print sth
        if sth < 0:
            print('no <a ')
            return ;
        eThString = html[sth:]
        eth = eThString.find(r'</a>')
        #print eth
        if eth < 0:
            print('no </a>')
            return ;
        thString = eThString[:eth+4]
        
        #print thString
        
        sth = thString.find(r'> ')
        #print sth
        if sth < 0:
            print('no >')
            return ;
        thString = thString[sth+2:]
        eth = thString.find(r'</a>')
        #print eth
        if eth < 0:
            print('no </a>')
            return ;
        thString = thString[:eth]
        print thString
        fp.write(thString)
        fp.write('\r\n')
        return thString;
        
def getKey(html,fp):
    # p_tpc_pos = html.find(r'p_tpc')
    p_tpc_pos = html.find(r'read_tpc')
    
    if p_tpc_pos < 0 :
        pass
    else:
        #print('Get 5.1!')
        sThString = html[0:p_tpc_pos]
        #sth = sThString.rfind(r'<th ')
        sth = sThString.rfind(r'<div ')
        #print sth
        if sth < 0:
            print('no <div ')
            return ;
        eThString = html[sth:]
        #eth = eThString.find(r'</th>')
        eth = eThString.find(r'</div>')
        #print eth
        if eth < 0:
            print('no </div>')
            return ;
        #thString = html[sth:sth+eth+5]
        #thString = eThString[:eth+5]
        thString = eThString[:eth+6]
        #print thString
        for i in [0,1,2]:
            sth = thString.find(r'<br /><br />')
            if sth < 0:
                print('no <br /><br />')
                return ;
            else:
                thString = thString[sth+12:]
        
        thString = thString.replace('<br /><br />',',');
        eth = thString.find(r'</div>')
        #print eth
        if eth < 0:
            print('no </div>')
            return ;
        thString = thString[:eth]
        fp.write(thString)
        fp.write('\r\n')
        return thString;
        '''
        try:  
            print thString.decode('utf-8').encode('gbk')
            #decode('gbk').encode('utf-8')
            dom = xml.dom.minidom.parseString(thString)
            root = dom.documentElement
            key = root.getElementsById('read_tpc');
            print key
        except Exception,e:  
            print Exception,":",e
        '''
def post(url, data): 
    req = urllib2.Request(url) 
    req.add_header('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
    data = urllib.urlencode(data) 
    #enable cookie 
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor()) 
    response = opener.open(req, data) 
    return response.read() 
  
def getckcode(): 
    url = 'http://1024.stv919.rocks/pw/ck.php?nowtime=' + str(int(round(time.time() * 1000)));
    req = urllib2.Request(url)
    req.add_header('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
    res = urllib2.urlopen(req)
    png = res.read()
    tp = open('test.png','wb');
    tp.write(png);
    tp.close()
    win32api.MessageBox(0, "We get a Key!", "Alert", win32con.MB_OK)  
    gdcode = raw_input('Enter gdcode:') 
    return gdcode
  
def sign_up(josnArray):
    gdcode = getckcode();
    data = {'gdcode':'',    'regname':'cnmsn',    'regpwd':'123456',    'regpwdrepeat':'123456',    'regemail':'1029486538@qq.com',    'invcode':'',    'question':'0',    'customquest':'',    'answer':'',    'regoicq':'',    'forward':'',    'step':'2',    'regsubmit':'提 交'}
    for i in josnArray:
        for j in i['key']:
            data['gdcode'] = gdcode;
            data['invcode'] = j;
            print post('http://1024.stv919.rocks/pw/regr.php',data)
            

#五一劳动节快乐，邀请码放送
# html = getHtml("http://1024.stv919.rocks/pw/thread.php?fid=78")

'''
http://1024.stv919.rocks/pw/regr.php?

gdcode:4138
regname:cnmsn
regpwd:123456
regpwdrepeat:123456
regemail:1029486538@qq.com
invcode:1a8cf49ef7337583
question:0
customquest:
answer:
regoicq:
forward:
step:2
regsubmit:提 交
                            ck.php?nowtime= + new Date().getTime();
http://1024.stv919.rocks/pw/ck.php?nowtime=1493969252852
'''
def start():
    lalala = []

    for i in [78,73,25,80,53,46,11,79]:
        time.sleep(2)
        urlpath = "http://1024.stv919.rocks/pw/thread.php?fid=" + str(i);
        html = getHtml(urlpath)
        print urlpath
        
        text = html
        while 1:
            sStr = r'<a '
            eStr = r'</a>'
            sPos = text.find(sStr)
            if sPos < 0:
                break;
            ePos = text.find(eStr)
            if ePos < 0:
                break;
            aim = text[sPos:ePos+4]
            ok = aim.find(r'五一劳动节快乐，邀请码放送')
            if ok < 0:
                pass
            else:
                try:  
                    #print aim
                    dom = xml.dom.minidom.parseString(aim)
                    root = dom.documentElement
                    href = root.getAttribute('href')
                    newurlpath = "http://1024.stv919.rocks/pw/" + href
                    newhtml = getHtml(newurlpath)
                    #print newurlpath
                    #get time 
                    timeStr = text[ePos+4:]
                    tp_time = getTime(timeStr)
                    tp = getKey(newhtml,fp)
                    json = {}
                    json['time'] = tp_time;
                    json['key'] = tp.split(',');
                    lalala.append(json);
                except Exception,e:  
                    print Exception,":",e
            text = text[ePos+4:]
            
    if len(lalala) > 0:
        sign_up(lalala)

if __name__ == '__main__':
    #easygui.msgbox(u'内容',u'标题',image='1231.png')
    while 1:
        fp = open("test.txt",'w+')
        start()
        fp.close()
        #time.sleep(20)