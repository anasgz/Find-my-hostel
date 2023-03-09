from django.urls import path
from Backend import views

urlpatterns=[
    path('indexpage/',views.indexpage, name="indexpage"),
    path('addadmin/',views.addadmin, name="addadmin"),
    path('saveadmin/',views.saveadmin,name="saveadmin"),
    path('displayadmin/',views.displayadmin,name="displayadmin"),
    path('editadmin/<int:dataid>/',views.editadmin,name="editadmin"),
    path('updateadmin/<int:dataid>/',views.updateadmin,name="updateadmin"),
    path('deleteadmin/<int:dataid>/',views.deleteadmin,name="deleteadmin"),
    path('addcategory/',views.addcategory,name="addcategory"),
    path('savecategory/',views.savecategory,name="savecategory"),
    path('viewcategory/',views.viewcategory,name="viewcategory"),
    path('editcategory/<int:dataid>/',views.editcategory,name="editcategory"),
    path('updatecategory/<int:dataid>/', views.updatecategory, name="updatecategory"),
    path('deletecategory/<int:dataid>/', views.deletecategory, name="deletecategory"),
    path('addproduct/', views.addproduct, name="addproduct"),
    path('saveproduct/', views.saveproduct, name="saveproduct"),
    path('displayproduct/',views.displayproduct,name="displayproduct"),
    path('editproduct/<int:dataid>/', views.editproduct, name="editproduct"),
    path('updateproduct/<int:dataid>/', views.updateproduct, name="updateproduct"),
    path('deleteproduct/<int:dataid>/', views.deleteproduct, name="deleteproduct"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('adminlogin/',views.adminlogin, name="adminlogin"),
    path('logoutadmin/',views.logoutadmin,name="logoutadmin"),
    path('displaycontactfn/', views.displaycontactfn, name="displaycontactfn"),
    path('deletecontactfn/<int:dataid>/', views.deletecontactfn, name="deletecontactfn"),
    path('bookings/', views.bookings, name="bookings"),
    path('deletebookings/<int:dataid>/',views.deletebookings,name="deletebookings")

]