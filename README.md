# mesos-task-exec

mesos-task-exec is an application launching commands in Mesos containers as
`docker exec`. The main difference being it launches an interactive terminal
by default.

This application has been built out of the DCOS cli exec command. It
does not rely on DCOS internals to work. Therefore, all credits goes to
https://github.com/dcos/dcos-cli.

The code might have been modified but still remains under the Apache 2.0
license.

# License

See [LICENSE](LICENSE)
