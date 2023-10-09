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
    path('prepare-payment/', views.prepare_payment, name="prepare-payment"),
    path('about-ai/',views.about, name="about-ai"),
    path('cr/',views.cr_reg, name='cr_reg'),
    path('gg/',views.gg_reg, name='gg_reg'),
    path('bb/',views.bb_reg, name='bb_reg'),
    path('optiml/',views.optiml_reg, name='optiml_reg'),
    path('vv/',views.vv_reg, name='vv_reg'),
    path('gg_back/', views.gg_back, name='gg_back'),
    path('cr_back/', views.cr_back, name='cr_back'),
    path('bb_back/', views.bb_back, name='bb_back'),
    path('optiml_back/', views.optiml_back, name='optiml_back'),
    path('vv_back/', views.vv_back, name='vv_back'),
    path('team/', views.team, name='team'),


    # events urls hrefs
    path('cubical_realm/', views.cubical_realm, name="cubical_realm"), 
    path('giga_gen/', views.giga_gen, name="giga_gen"),
    path('beat_bots/', views.beat_bots, name="beat_bots"),
    path('opti_ml/', views.OptiML, name="opti_ml"), 
    path('ss/', views.ss, name="ss"),  
]


# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)