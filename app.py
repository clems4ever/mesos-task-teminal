from mesos.mesos import TaskIO

t = TaskIO(task_id='mesos-ping.453fbeb7-cb7f-11e7-a63d-c4346bb5c9dc', tty=True, interactive=True, cmd="/bin/sh", args=[])
t.run()
