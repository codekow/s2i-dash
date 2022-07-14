#!/bin/bash
# set -x

if ! whoami &> /dev/null; then
    if [ -w /etc/passwd ]; then
        echo "${USER_NAME:-apb}:x:$(id -u):0:${USER_NAME:-apb} user:${HOME}:/sbin/nologin" >> /etc/passwd
    fi
fi

USER_ID=$(id -u)

if [ x"$USER_ID" != x"0" -a x"$USER_ID" != x"1001" -a -e /usr/lib64/libnss_wrapper.so ]; then
    NSS_WRAPPER_PASSWD=/tmp/passwd.nss_wrapper
    NSS_WRAPPER_GROUP=/etc/group

    cp /etc/passwd $NSS_WRAPPER_PASSWD

    echo "${USER_NAME:-apb}:x:$(id -u):0:${USER_NAME:-apb} user:${HOME}:/sbin/nologin" >> $NSS_WRAPPER_PASSWD

    export NSS_WRAPPER_PASSWD
    export NSS_WRAPPER_GROUP

    export LD_PRELOAD=/usr/lib64/libnss_wrapper.so

fi
