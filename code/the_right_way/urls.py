# For more information please see:
#     https://docs.djangoproject.com/en/3.0/topics/http/urls/
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('the-pattern/', include('the_right_way.the_pattern.urls')),
    path('the-pattern-explanation/', include('the_right_way.the_pattern.explanation_urls')),
    path('context-data/', include('the_right_way.context_data.urls')),
    path('context-data-discussion/', include('the_right_way.context_data.discussion_urls')),
]