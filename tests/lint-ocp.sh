#!/bin/bash
oc process -f "$TEMPLATE_FILE" \
  -p APPLICATION_NAME=${TEMPLATE_NAME} \
  -p PI_WEB_API_PASSWORD=${PI_WEB_API_PASSWORD} \
  -p PI_WEB_API_USERNAME=${PI_WEB_API_USERNAME} > /dev/null
