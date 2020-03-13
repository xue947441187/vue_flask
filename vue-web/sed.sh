#!/usr/bin/env bash
sed -i 's!http://.*!http://'$FLASK_HOST_PORT';!g' /etc/nginx/conf.d/default.conf