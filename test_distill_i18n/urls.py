"""test_distill_i18n URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.i18n import i18n_patterns

from django_distill import distill_path

# WITHOUT I18N URLS
# urlpatterns = [
#     path('foo/', include('foo.urls'), name='foo'),
# ]

# WITH I18N URLS
urlpatterns = i18n_patterns(
    path('foo/', include('foo.urls'), name='foo'),
)

urlpatterns += [
    path('admin/', admin.site.urls),
]
