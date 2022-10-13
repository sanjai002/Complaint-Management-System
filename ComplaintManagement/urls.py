"""ComplaintManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from complaint.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',user_login, name='user_login'),
    path('admin_login',admin_login, name='admin_login'),
    path('add_category',add_category, name='add_category'),
    path('edit_category/<int:pid>',edit_category, name='edit_category'),
    path('delete_category/<int:pid>',delete_category, name='delete_category'),
    path('changepassword_admin',changepassword_admin, name='changepassword_admin'),
    path('add_subcategory',add_subcategory, name='add_subcategory'),
    path('edit_subcategory/<int:pid>',edit_subcategory, name='edit_subcategory'),
    path('delete_subcategory/<int:pid>',delete_subcategory, name='delete_subcategory'),
    path('add_state',add_state, name='add_state'),
    path('edit_state/<int:pid>',edit_state,name='edit_state'),
    path('delete_state/<int:pid>',delete_state,name='delete_state'),
    path('logout',Logout,name='logout'),
    path('registration',registration, name='registration'),
    path('user_home',user_home, name='user_home'),
    path('profile',profile, name='profile'),
    path('update_image',update_image, name='update_image'),
    path('changepwd_user',changepwd_user, name='changepwd_user'),
    path('register_complaint',register_complaint, name='register_complaint'),
    path('load-subcategory/', load_subcategory, name='ajax_load_subcategory'),
    path('complaint_history',complaint_history, name='complaint_history'),
    path('complaint_details/<int:pid>',complaint_details,name='complaint_details'),
    path('notprocess_complaint',notprocess_complaint,name='notprocess_complaint'),
    path('complaint_detailsadmin/<int:pid>',complaint_detailsadmin, name='complaint_detailsadmin'),
    path('update_complaint/<int:pid>',update_complaint, name='update_complaint'),
    path('user_profile/<int:pid>',user_profile, name='user_profile'),
    path('manage_users',manage_users, name='manage_users'),
    path('delete_user/<int:pid>',delete_user, name='delete_user'),
    path('inprocess_complaint',inprocess_complaint,name='inprocess_complaint'),
    path('closed_complaint',closed_complaint,name='closed_complaint'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
