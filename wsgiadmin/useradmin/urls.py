# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('',
		(r'^/?$', 'wsgiadmin.useradmin.views.info'),
		(r'^domains/', include('wsgiadmin.domains.urls')),
        (r'^bills/', include('wsgiadmin.bills.urls')),
		(r'^ftp/', include('wsgiadmin.ftps.urls')),
        (r'^email/', include('wsgiadmin.emails.urls')),
        (r'^apache/', include('wsgiadmin.apacheconf.urls')),
		(r'^pg/', include('wsgiadmin.pgs.urls')),
		(r'^users/', include('wsgiadmin.users.urls')),
		(r'^mysql/', include('wsgiadmin.mysql.urls')),
        (r'^reg/?$', 'wsgiadmin.useradmin.views.reg'),
        (r'^reg-ok/?$', 'wsgiadmin.useradmin.views.regok'),
		(r"^message/([a-z]{1,20})/(.{1,100})?$","wsgiadmin.useradmin.views.message"),
		(r'^login/?$', 'django.contrib.auth.views.login', {'template_name': 'login_reg.html'}),
		(r'^logout/?$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
		(r'^change_passwd/?$', 'wsgiadmin.useradmin.views.change_passwd'),
		(r'^ok/?$', 'wsgiadmin.useradmin.views.ok'),
		(r'^error/?$', 'wsgiadmin.useradmin.views.error'),
		(r'^info/?$', 'wsgiadmin.useradmin.views.info'),
		(r'^pg/?$', 'wsgiadmin.useradmin.views.pg'),

)

