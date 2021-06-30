
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('analyze/', views.analyze, name='removepunc'),
    # path('capitalizefirst/', views.capitalizefirst, name='capitalizefirst'),
    # path('newlineremove/', views.newlineremove, name='nrelineremove'),
    # path('spaceremove/', views.spaceremove, name='spaceremove'),
    # path('charcount/', views.charcount, name='charcount'),
]
