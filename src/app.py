import sys
import argparse
import os
from mesos.mesos import TaskIO

parser = argparse.ArgumentParser(description='Run commands in a nested container of a mesos task.')
parser.add_argument('task_id', type=str, help='The task id you want to connect to.')

args = parser.parse_args()

mesos_master_url = os.getenv('MESOS_MASTER_URL', 'http://localhost:5050')

t = TaskIO(mesos_master_url=mesos_master_url, task_id=args.task_id, tty=True, 
    interactive=True, cmd="/bin/bash", args=[])
t.run()
