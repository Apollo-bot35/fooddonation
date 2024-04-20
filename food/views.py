from django.shortcuts import render
from .services import foodServices
import pymysql


def home(request):
    return render(request,'index.html')

def donor(request):
    return render(request,'donorlogin.html')

def admin(request):
    return render(request,'adminlogin.html')

def recipient(request):
    return render(request,'recipient.html')

def volunteer(request):
    return render(request,'volunteer.html')

def login(request):
    return render(request,'login.html')

def userprofile(request):
    return render(request,'fooddetails.html')

def donoradd(request):
    mess=None
    if request.method=="POST":
        id=request.POST.get("username")
        pw=request.POST.get("password")
        nm=request.POST.get("name")
        em=request.POST.get("email")
        ph=int(request.POST.get("phone"))
        ad=request.POST.get("address")
       
        con=pymysql.connect(host='b9gk1na9gt43ebj6vr96-mysql.services.clever-cloud.com',user='unc92p2qdguypwyc',password='zs8EbBMJHTGGSqkKVGwY',database='b9gk1na9gt43ebj6vr96')
        curs=con.cursor()
        curs.execute("insert into donor values('%s','%s','%s','%s',%d,'%s')" %(id,pw,nm,em,ph,ad))
        con.commit()
    return render(request,"fooddetails.html")


def reportshow(request):
     return render(request,"blank.html")



def fooddetails(request):
    mess=None
    if request.method=="POST":
        ty=request.POST.get("type")
        ex=request.POST.get("date")
        des=request.POST.get("description")
        hr=int(request.POST.get("prepared"))
        cat=request.POST.get("raw")
        loc=request.POST.get("location")
        don=request.POST.get("date")

        
        con=pymysql.connect(host='b9gk1na9gt43ebj6vr96-mysql.services.clever-cloud.com',user='unc92p2qdguypwyc',password='zs8EbBMJHTGGSqkKVGwY',database='b9gk1na9gt43ebj6vr96')
        curs=con.cursor()
        curs.execute("insert into food_item values('%s','%s','%s',%d,'%s','%s','%s')" %(ty,ex,des,hr,cat,loc,don))
        con.commit()
    return render(request,"success.html")



def showdonor(request):
    obj=foodServices()
    data=obj.getalldata()
    return render(request,'details.html',{"donorlist":data})

def showfood(request):
    obj=foodServices()
    data=obj.getfood()
    return render(request,'foodreport.html',{"foodlist":data})













   


