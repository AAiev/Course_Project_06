from django.urls import path, include

from catalog.views import home, contacts

urlpatterns = [
    path('', home),
    path('', contacts),
    path('home/', contacts),
    path('contacts/', contacts),

]
