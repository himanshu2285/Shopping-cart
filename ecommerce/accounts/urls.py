from django.urls import path, include
from accounts import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.handlelogin, name='login'),
    path('logout/', views.handlelogout, name='logout'),
    # path('activate/<uidb64>/<token>', views.ActivateAccountView.as_view(), name="activate"),
]