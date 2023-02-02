#!/bin/sh
curl https://kornelix.net/fotoxx/fotoxx.html 2>/dev/null|grep -- '<br>' |head -n1 |sed -e 's,<.*,,' |xargs echo
