 
from django.urls import path, include
from base import auth_views as authviews
from base.urls import urlpatterns
urlpatterns = [
    path('login/', authviews.login_page,name="login"),
    path('logout/', authviews.logout_page,name="logout"),
    path('register/', authviews.register_page,name="register"),
    path('profile/<int:pk>/', authviews.profile,name="profile"),
    path('edit-profile/<int:pk>/', authviews.editprofile,name="edit-profile"),
 
    
    
]
