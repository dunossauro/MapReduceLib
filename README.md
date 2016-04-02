# MapReduceLib
Python Tool which generates MapReduce jobs, file transfer in HDFS and assists Hadoop administrative functions.

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
hdfs = Hdfs()   # You can set your Hadoop bin dir, ex: Hdfs("/usr/local/hadoop/bin/hadoop fs")

hdfs.cat(<file>)

hdfs.chgrp(<file>)

hdfs.chmod(<file>)

hdfs.chown(<file>)

hdfs.get(<file>)

hdfs.ls(<dir>)      # if you don't set a parameter, list the root

hdfs.mkdir(<dir>)

hdfs.put(<file>)

hdfs.rm(<file>)

hdfs.rm_dir(<dir>)
```
#### MapReduce Functions
```
job = MapReduce()   # You can set your Streaming and Hadoop dirs, ex: 
                    # MapReduce("/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.*.jar",               
                                "/usr/local/hadoop/bin/hadoop")

job.run_map(<mapper_file>, <input_dir>, <output_dir>)
# run_map("map.py","data","out",)

job.run_map_combiner_reduce(<mapper_file>, <combiner_file>, <reducer_file>, <input_dir>, <output_dir>)
# job.run_map_combiner_reduce("map.py","reduce.py","reduce.py","data","out")

job.run_map_reduce(<mapper_file>, <reducer_file>, <input_dir>, <output_dir>)
# job.run_map_reduce("map.py","reduce.py","data","out")

job.run_pass_flags(<Parameter>)
# job.run_pass_flags("\
-mapper `pwd`/map.py \
-reducer `pwd`/reduce.py \
-input /data/* \
-output /out ")
```
