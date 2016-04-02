# MapReduceLib
Tool in Python to generate MapReduce jobs, file transfers in HDFS and assist administrative functions of Hadoop

## Support
  - Python 2.6+ and 3.2+
  - pySpark 1.5+

## Usage

#### Administration tasks

```
from mapreducelib import Hadoop

hadoop = Hadoop()   # You can set your Hadoop sbin dir, ex: Hadoop("/usr/local/hadoop/sbin")

#Start/Stop Hadoop Cluster
hadoop.start_all()
hadoop.stop_all()

#Start/Stop only Yarn
hadoop.yarn_start()
hadoop.yarn_stop()

#Start/Stop only HDFS
hadoop.dfs_start()
hadoop.dfs_stop()

#Formating namenode/datanode
hadoop.format_datanode()
hadoop.format_namenode()

```

#### HDFS Functions
```
hdfs = Hdfs()   # You can set your Hadoop bin dir, ex: Hadoop("/usr/local/hadoop/bin/bin fs")

hdfs.cat(<file>)

hdfs.chgrp(<file>)

hdfs.chmod(<file>)

hdfs.chown(<file>)

hdfs.get(<file>)

hdfs.ls(<dir>)      # If you don't pass a parameter, list the root

hdfs.mkdir(<dir>)

hdfs.put(<file>)

hdfs.rm(<file>)

hdfs.rm_dir(<dir>)


```
