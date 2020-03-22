from . import views
from django.urls import path,include

app_name = 'checkout'

urlpatterns = [
    path('',views.IndexView.as_view(), name="index"),
    path('create-checkout-session/',views.onetime_payment_checkout , name='create-checkout'),
    path('config/',views.stripe_config),
    path('success/',views.SuccessView.as_view() ),
    path('canceled/', views.CanceledView.as_view())
]
