#!/bin/sh
curl https://kornelix.net/fotocx/fotocx.html 2>/dev/null|grep -- '<br>' |head -n1 |sed -e 's,<.*,,' |xargs echo
