from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path('reg/', views.reg, name="reg"),
    path('explore/',views.explore, name='explore'),
    path('login/', views.admin, name="admin"),
    path('logout/', views.handlelogout, name="logout"),
    path('payment/', views.payment, name="payment"),
    path('prepare-payment/', views.prepare_payment, name="prepare-payment")
]


# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)