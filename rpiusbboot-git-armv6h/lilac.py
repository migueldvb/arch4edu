#!/usr/bin/env python3
from lilaclib import *

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'aur': 'rpiusbboot-git'}, {'github': 'raspberrypi/usbboot'}]
build_prefix = 'extra-armv6h'

def pre_build():
    aur_pre_build('rpiusbboot-git')
    add_arch(['armv6h'])
    add_makedepends(['git'])

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
