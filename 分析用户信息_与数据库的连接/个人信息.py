import pymysql
db=pymysql.connect("localhost","root","","test")
cursor=db.cursor()
file =open('C:/Users/haome/Desktop/demo_信息.txt',encoding='utf-8',errors='ignore')
i=0
context=file.readline()
while 1:
    context=file.readline()
    context=context.replace(' ','')
    i=i+1
    if i==6:
        weibo_id=context.replace('\n','')
    elif i==12:
        di_qu=context.replace('\n','')
    elif i==15:
        miao_shu=context.replace('\n','')
    elif i==16:
        guanzhu=context.replace('\n','')
        guanzhu=int(guanzhu.replace('万','0000').replace('关注',''))
    elif i==17:
        fans=context.replace('\n','')
        fans=int(fans.replace('万','0000').replace('粉丝',''))
    elif i==18:
        weibo_num=context.replace('\n','')
        weibo_num=int(weibo_num.replace('万','0000').replace('微博',''))
##    elif i==20:
##        jian_jie=context.replace('\n','').replace('简介：','')
    elif i==21:
        tag=context.replace('\n','').replace('标签：','')
    elif i==22:
        education=context.replace('\n','').replace('教育信息：','')
    elif i==23:
        professional=context.replace('\n','').replace('职业信息：','')
    elif i==25:
##        if 'FEMALE' in context:
##            sex='女'
##        else:
##            sex='男'
        i=0
        db.begin()
        try:
           # sql="insert into weibo(id,di_qu,miao_shu,guanzhu,fans,weibo_num,jian_jie,tag,education,professional,sex) values ('%s','%s','%s','%d','%d','%d','%s','%s','%s','%s','%s')"%(weibo_id,di_qu,miao_shu,guanzhu,fans,weibo_num,jian_jie,tag,education,professional,sex)

            sql="insert into weibo(id,di_qu,miao_shu,guanzhu,fans,weibo_num,tag,education,professional) values ('%s','%s','%s','%d','%d','%d','%s','%s','%s')"%(weibo_id,di_qu,miao_shu,guanzhu,fans,weibo_num,tag,education,professional)
            db.ping(reconnect=True)
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            db.close()
    if len(context) ==0:
        break
db.close()
file.close()
print('succeed')
