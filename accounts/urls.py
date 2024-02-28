from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile_history_detail/<id>', views.order_history_items, name='profile_history_detail'),

]
