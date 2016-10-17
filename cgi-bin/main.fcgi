#!/usr/bin/python

import sys
import os

sys.path.insert(0, '/kunden/homepages/0/d374033285/htdocs/.local/lib/python2.7/site_packages')
sys.path.append('/kunden/homepages/0/d374033285/htdocs/mgw/mysite')

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="prefork", daemonize="false")
