#encoding=utf-8
import urllib2
import urllib
import cookielib
import time
from website import *
def ABrower(pausetime,user,password):
    #登陆页面，可以通过抓包工具分析获得，火狐谷歌等浏览器自带
    login_page = "http://www.stcyol.com/?c=zhuce&m=sigin"
    try:
        #获得一个cookieJar实例
        cj = cookielib.CookieJar()
        #cookieJar作为参数，获得一个opener的实例
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        #伪装成一个正常的浏览器，避免有些web服务器拒绝访问。
        opener.addheaders = [('User-Agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
        opener.addheaders = [('Referer','http://www.stcyol.com/?c=zhuce)')]
        opener.addheaders = [('Origin','http://www.stcyol.com)')]
        opener.addheaders = [('Host','www.stcyol.com)')]
        #生成Post数据，含有登陆用户名密码及某些自带数据（例如dit表示学生登陆）。
        data = urllib.urlencode({"dit":1,"user":user,"pwd":password})
        #以post的方法访问登陆页面，访问之后cookieJar会自定保存cookie
        opener.open(login_page,data)
        time.sleep(3)
        #以带cookie的方式访问页面
        
        print "为了防止网络延迟等问题，每刷一个页面会有一定的等待时间"
        print "每个页面之间的等待时间设置为"+str(pausetime)+"."
        
        count=1;
        for web in website:
            op=opener.open(web);
            time.sleep(pausetime);
            data=op.read();
            #print data
            print "现在正在刷第"+str(count)+"个视频......"
            count=count+1
            
        
        #一共刷100个创业资讯可以得到满分
        count=1;
        for ids in range(7575,7626):
            web=webinfo1+str(ids);
            op=opener.open(web);
            time.sleep(pausetime);
            data=op.read();
            print "现在正在刷第"+str(count)+"个创业资讯......"
            count=count+1
        
        
        #一共刷100个创业案例可以得到满分
        count=1;
        for ids in range(1,51):
            web=webinfo2+str(ids);
            op=opener.open(web);
            time.sleep(pausetime);
            data=op.read();
            print "现在正在刷第"+str(count)+"个创业案例......"
            count=count+1
        
        
        time.sleep(pausetime)
        return "用户名为"+user+"的账号执行成功！"
       
        #return data
    except Exception,e:
        print str(e)

#for xuehao in range(a,b):
while True:
    print "请输入0或者1,0表示单个用户，1表示连续区间且密码相同用户,其他输入表示退出"
    content= raw_input()
    if content=="0":
        username=raw_input("学号: ")
        password=raw_input("密码: ")
        print ABrower(0,username,password)
    elif content=="1":
        print "请输入一个左闭右开区间......"
        lowbound=raw_input("学号区间下界: ")
        upbound=raw_input("学号区间上界: ")
        password=raw_input("密码: ")
        low=int(lowbound)
        up=int(upbound)
        for username in range(low,up):
            print ABrower(0,str(username),password)
    else:
        break
