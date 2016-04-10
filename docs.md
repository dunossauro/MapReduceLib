# Simple Doc

all classes interacts with Bash using `os.system`

Ex:

```python
from os import system
hadoop_sbin = "/usr/local/hadoop/sbin/"
hadoop_fs = "/usr/local/hadoop/bin/hadoop fs"

system("{exec} {func} {dir}".format(exec=hadoop_fs, func="ls", dir="/"))

```

## Hadoop Class

The Hadoop class is an interface for all interactions sbin directory

```python
class Hadoop:
    def __init__(self, hadoop_sbin="/usr/local/hadoop/sbin"):
        self.sbin = hadoop_sbin
```
I've chosen to use '/usr/local/hadoop' because the official documentation of Hadoop recommends that directory. But you can modify the .py file in the init method or set in runtime

`hadoop_sbin = <your_dir>`

Using Hadoop class you can use its methods, such as direct interactions with Bash in python or pySpark Terminal

```python
from mapreducelib import Hadoop

hadoop = Hadoop()

hadoop.start_all()
hadoop.dfs_start()
```

Using Hadoop class you can also format and balance your HDFS

```python
hadoop.balancer_start()
hadoop.format_namenode()
hadoop.format_datanode()
```

## HDFS class

The HDFs class is an interface for all interactions command 'hadoop fs'

## MapReduce Class

The MapReduce class is an interface that uses the Hadoop Streaming
