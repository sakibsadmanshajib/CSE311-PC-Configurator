from django.urls import path
from . import views as pc

app_name = 'pcconfig'

urlpatterns = [

    # Home URL
    path('', pc.home, name='home'),

    # Authentication URL
    path('login/', pc.user_login, name='login'),
    path('signup/', pc.user_signup, name='signup'),
    path('logout/', pc.user_logout, name='logout'),

    # PC Entry manipulation
    path('create/', pc.createPC, name='createPC'),
    path('view/<int:PC_id>', pc.viewPC, name='viewPC'),
    path('edit/<int:PC_id>', pc.editPC, name='editPC'),
]