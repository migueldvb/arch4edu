#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur': None}]
build_prefix = 'extra-x86_64'
depends = ['coin']

def pre_build():
    aur_pre_build()
    add_makedepends(['cmake', 'swig', 'qt5-base'])

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)