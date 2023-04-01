# urls.py

from django.urls import path
from website.views import home,services, about
# urls.py

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    # path('pricing/', pricing, name='pricing'),
    # path('gallery/', gallery, name='gallery'),
    path('services/', services, name='services'),
]