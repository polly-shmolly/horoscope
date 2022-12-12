from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path('Aries', views.aries, name='aries'),
    path('Taurus', views.taurus, name='taurus'),
    path('Gemini', views.gemini, name='gemini'),
    path('Cancer', views.cancer, name='cancer'),
    path('Leo', views.leo, name='leo'),
    path('Virgo', views.virgo, name='virgo'),
    path('Libra', views.libra, name='libra'),
    path('Scorpio', views.scorpio, name='scorpio'),
    path('Sagittarius', views.sagittarius, name='sagittarius'),
    path('Capricorn', views.capricorn, name='capricorn'),
    path('Aquarius', views.aquarius, name='aquarius'),
    path('Pisces', views.pisces, name='pisces'),
    path('Add', views.add, name='add'),
] + static(settings.STATIC_URL,
           document_root=settings.STATIC_ROOT)

