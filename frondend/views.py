from django.shortcuts import render,redirect
from Backend.models import categorydb, productdb, admincontactdb
from frondend.models import f_login, checkoutdb
from django.contrib import messages


# Create your views here.
def homepage(req):
    data=categorydb.objects.all()

    return render(req,"home.html",{"data":data})
def Hostels(req):
    data=categorydb.objects.all()
    return render(req,"MyHostels.html",{"data":data})
def review(req):
    return render(req,"reviews.html")
def contactpage(req):
    return render(req,"contact.html")
def aboutus(req):
    return render(req,"about.html")
def category(request,itemcatg):
    print("===itemcatg===", itemcatg)
    catg = itemcatg.upper()

    products = productdb.objects.filter(CATEGORY=itemcatg)
    context = {
        'products': products,
        'catg': catg
    }
    return render(request,"hostelcategory.html",context)
def singlepage(req,dataid):
    data = productdb.objects.get(id=dataid)
    return render(req,"singlehostel.html",{'data':data})
def loginpages(req):
    return render(req,"login1.html")
def savelogin(req):
    if req.method== "POST":
        USERNAME=req.POST.get('username')
        EMAIL=req.POST.get('email')
        PASSWORD =req.POST.get("password")
        CONFIRMPASSWORD = req.POST.get("confirmpassword")
        obj=f_login(username=USERNAME,Email=EMAIL,Password=PASSWORD,Confirmpassword=CONFIRMPASSWORD)
        obj.save()
        messages.success(req, "Registered Successfully..!")
        return redirect(loginpages)
def custumerlogin(req):
    if req.method == "POST":
        username_r = req.POST.get('username')
        password_r = req.POST.get('password')

        if f_login.objects.filter(username=username_r, Password=password_r).exists():
            req.session['username1'] = username_r
            req.session['password1'] = password_r
            messages.success(req, "LOGIN SUCESSFULLY")
            return redirect(homepage)
        else:
            messages.error(req, "INVALID USER or PASSWORD")
            return render(req,'login1.html')

def weblogout(req):
    del req.session['username1']
    del req.session['password1']
    messages.success(req, "Logout Successfully...!")
    return redirect(homepage)
def saveadmincontact(req):
    if req.method == "POST":
        na = req.POST.get('name')
        email = req.POST.get('email')
        sub = req.POST.get('subject')
        msg = req.POST.get('message')
        obj=admincontactdb(NAME=na, EMAIL=email, SUBJECT=sub, MESSAGE=msg)
        obj.save()
        return redirect(contactpage)
def checkoutpage(req):
    return render(req,"checkout.html")
def paypage(req):
    return render(req,"payment.html")
def chkoutdb(req):
    if req.method == "POST":
        na = req.POST.get('name')
        ad = req.POST.get('address')
        tot = req.POST.get('total')
        pin = req.POST.get('pincode')
        crd = req.POST.get('cardnumber')
        obj=checkoutdb(FIRSTNAME=na, ADRESS=ad, TOTAL=tot, PINCODE=pin,CARDNUMBER=crd)
        obj.save()
        messages.success(req,"Successfully Booked...!")
        return redirect(homepage)