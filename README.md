stackmonitor
============

Some script for monitoring Openstack Services


Usage
=====

    if [ -e stackmonitor ]; then
        cd stackmonitor;
        git pull origin >/dev/null
        cd -
    else
        git clone git://github.com/gtt116/stackmonitor >/dev/null
    fi

    python stackmonitor/check_glance.py true
