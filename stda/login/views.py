from django.shortcuts import render
import mysql.connector as sql
ph=''
pwd=''
# Create your views here.
def loginaction(request):
    global pwd,ph
    if request.method=="POST":
        m=sql.connect(host='database-1.cafue6n4qwbz.ap-south-1.rds.amazonaws.com',user='admin',passwd='1234567890',database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():

           if key=="phone_no":

            ph=value
           if key=="password":
            pwd=value
            
            
        c="select * from users2 where phone_no='{}' and password='{}'".format(ph,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall()) 
        if t==():
            return render(request,"error.html")
        else:
            return render(request,"welcome.html")
    return render(request,'login_page.html')
