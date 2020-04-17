#!/usr/bin/env python

import os
import shutil
import sys

def check_reboot():
    """return true if the computer has a pending reeboot"""
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk,min_gb,min_percent):
    """return true if there isn't enough disk space ,false otherwise"""
    du=shutil.disk_usage(disk)

    percent_free= 100*du.free/du.total

    gigabytes_free =du.free/2**30
    if gigabytes_free <min_gb or percent_free < min_percent:
        return True
    return False

def check_root_full():
    """Returns True is the root patition is full ,false otherwise"""
    return check_disk_full(disk="/",min_gb=2,min_percent=10)
def main():
    checks=[(check_reboot,"pending reboot"),(check_root_full,"root partition full")]
    for check ,msg in checks:
        if check():
            print(msg)
            sys.exit(1)

    print("everyting is ok")
    sys.exit(0)

main()
