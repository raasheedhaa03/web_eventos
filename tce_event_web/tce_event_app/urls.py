from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
		path('', views.home, name ="home"),
		path('signup',views.signup,name="signup"),
		path('login',views.login,name="login"),
		path('logout',views.logout,name="logout"),
		path('profile/<int:user_id>/', views.profile_view, name='profile'),
]
