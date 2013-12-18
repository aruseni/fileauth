from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(
        r'^login/$',
        'django.contrib.auth.views.login',
        {'template_name': 'login.html'}
    ),
    url(
        r'^file_login/$',
        'fileauth.views.file_login_view'
    ),
    url(
        r'^logout/$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/login/'
        }
    ),
    (
        r'^$',
        login_required(
            TemplateView.as_view(template_name='index.html')
        )
    ),
)
