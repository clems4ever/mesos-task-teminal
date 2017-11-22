# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
#         "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

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
