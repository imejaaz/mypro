from django.urls import path
from django.urls import include

from . import views

urlpatterns=[
    path('', views.index, name='home'),
    path('forms/', views.forms, name='form'),
    path('formSubmit/', views.formSubmit, name='fsub'),
    path('delete/<id>', views.delete_receipe, name='delete'),
    path('update/<id>', views.update_receipe, name='update'),
    path('SearchReceipe/', views.search, name='search'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register_form, name='register'),
    path('student/', views.get_student, name='student'),
    path('studentResult/<str:sId>/', views.studentResult, name='sResult')
    # path('studentResult/<str:sId>', views.studentResult, name='sResult')
]
