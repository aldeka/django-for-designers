from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'bookmarks.views.index', name='home'),
    url(r'^bookmarks/$', 'bookmarks.views.index', name='bookmarks_view'),
    url(r'^tags/([\w-]+)/$', 'bookmarks.views.tag'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
)
