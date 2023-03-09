from django.urls import path
from frondend import views

urlpatterns=[
path('homepage/' ,views.homepage, name="homepage"),
path('Hostels/' ,views.Hostels, name="Hostels"),
path('review/' ,views.review, name="review"),
path('contactpage/' ,views.contactpage, name="contactpage"),
path('aboutus/' ,views.aboutus, name="aboutus"),
path('category/<itemcatg>' ,views.category, name="category"),
path('singlepage/<int:dataid>' ,views.singlepage, name="singlepage"),
path('loginpages/' ,views.loginpages, name="loginpages"),
path('savelogin/' ,views.savelogin, name="savelogin"),
path('custumerlogin/', views.custumerlogin, name="custumerlogin"),
path('weblogout/', views.weblogout, name="weblogout"),
path('saveadmincontact/', views.saveadmincontact, name="saveadmincontact"),
path('checkoutpage/', views.checkoutpage, name="checkoutpage"),
path('paypage/',views.paypage,name="paypage"),
path('chkoutdb/',views.chkoutdb,name="chkoutdb")
]