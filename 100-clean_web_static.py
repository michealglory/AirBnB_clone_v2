#!/usr/bin/python3
"""
Removes out-of-date archives
"""

import os
from fabric.api import *

env.hosts = ['54.160.97.141', '18.233.64.80']


def do_clean(number=0):
    """Removes out-of-date archives.
    Args:
        number (int): number of archives to keep.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
