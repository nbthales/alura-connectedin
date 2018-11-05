from django.urls import path
from usuarios.views import RegistrarUsuarioView
from django.contrib.auth import views

urlpatterns = [
    path('registrar/', RegistrarUsuarioView.as_view(), name="registrar"),
    path('login/', views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', views.logout_then_login, {'login_url':'/login/'}, name='logout')
]
