from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'dmmoody.views.home', name="home"),
    url(r"^badges", 'dmmoody.views.badges', name="badges"),
    url(r"^about", 'dmmoody.views.about', name="about"),
    url(r'^admin/', include(admin.site.urls)),
)
