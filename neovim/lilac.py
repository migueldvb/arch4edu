#!/usr/bin/env python3
from lilaclib import *

luapkg = 'luajit-git-v2.1.0.beta3.r124.gbd00094c-1-aarch64.pkg.tar.xz'

maintainers = [{'github': 'petronny', 'email': 'Jingbei Li <i@jingbei.li>'}]
update_on = [{'archpkg': 'neovim'}]
build_prefix = 'extra-aarch64'
makechrootpkg_args = ['-I', luapkg]

def pre_build():
    download_official_pkgbuild('neovim')
    add_arch(['aarch64'])
    run_cmd(['wget', 'https://mirrors.tuna.tsinghua.edu.cn/archlinuxarm/aarch64/alarm/%s' % luapkg])

def post_build():
    git_add_files('PKGBUILD')
    git_commit()
    run_cmd(['rm', luapkg])

if __name__ == '__main__':
    single_main(build_prefix)
