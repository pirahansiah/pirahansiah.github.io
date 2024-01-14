# which python
#! /Users/farshid/miniconda3/envs/farshid/bin/python

import shutil
import psutil
def check_disk(disk):
    du=shutil.disk_usage(disk)
    free=du.free /du.total * 100
    return free # > 20
def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage # < 25

if __name__=="__main__" :
    print(check_disk('/'))
    print(check_cpu_usage())

