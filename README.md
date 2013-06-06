stackmonitor
============

Some script for monitoring Openstack Services


Usage
=====

    if [ -e stackmonitor ]; then
        rm -rf stackmonitor
    fi
    git clone git://github.com/gtt116/stackmonitor >/dev/null

    python stackmonitor/check_glance.py true
