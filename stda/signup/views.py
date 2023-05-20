from django.shortcuts import render
import mysql.connector as sql
from django.http import HttpResponse
from django.template import loader


fn=''
ln=''
s=''
pwd=''
bd=''
phone_number=''
pl=''
hn=''
tp=''

# Create your views here.
def signaction(request):
    global fn,ln,s,pwd,bd,phone_number,pl,hn,tp
    if request.method=="POST":


        m=sql.connect(host='database-1.cafue6n4qwbz.ap-south-1.rds.amazonaws.com',user='admin',passwd='1234567890',database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="First_name":
                fn=value
            if key=="Last_name":
                ln=value
            if key=="sex":
                s=value
           
            if key=="password":
               
                pwd=value
               
                    
                
            if key=="blood":
                bd=value
            if key=="phone_number":
                phone_number=value
            if key=='place':
                pl=value
            if key=='house_no':
                hn=value
            if key=='type':
                tp=value
           
            
        c="insert into users2 Values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(fn,ln,s,pwd,bd,phone_number,pl,hn,tp)
        cursor.execute(c)
        m.commit()
    return render(request,'signup_page.html')

