from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('meta.views',
                       url(r'^api/branches/$', 'branches'),
                       url(r'^api/branches/([0-9]{1,2})/$', 'branches'),
                       url(r'^api/branches/([0-9]{1,2})/info/$', 'branch_info'),
                       url(r'^api/branches/([0-9]{1,2})/contacts/$', 'branch_contacts'),
                       url(r'^api/contacts/$', 'contacts'),
                       url(r'^api/contacts/([0-9]{1,2})/$', 'contacts'),
                       url(r'^api/contacts/([0-9]{1,2})/info/$', 'contact_info'),
                       url(r'^api/deals/$', 'deals'),
                       url(r'^api/deals/([0-9]{1,2})/$', 'deals'),
                       url(r'^api/deals/([0-9]{1,2})/info/$', 'deal_info'),
                       url(r'^api/deals/([0-9]{1,2})/branches/$', 'deal_branches'),
                       url(r'^api/deals/([0-9]{1,2})/branches/([0-9]{1,2})/$', 'deal_branches'),

)

urlpatterns += patterns('mf.views',
                        url(r'^$', 'home', name="home"))

urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)

urlpatterns += patterns('',
    url(r'^api/users/authenticate/', 'rest_framework.authtoken.views.obtain_auth_token')
)


