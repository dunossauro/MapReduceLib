#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    About mapreducelib

Version:    0.2.1 (Dec/2015)
Author:     Eduardo Mendes (z4r4tu5tr4)
Oficial:    Github.com/z4r4tu5tr4/mapreducelib
License:    GPLv3
"""

import os


class hdfs:

    def __init__(self,hdfs_local="/usr/local/hadoop/bin/hadoop fs"):
        self.hdfs = hdfs_local

    def mkdir(self, local):
        os.system(("%s -mkdir %s")%(self.hdfs, local)

    def ls(self, dir='/'):
    	if dir != '/':
    		os.system(("%s -ls /%s")%(self.hdfs,dir))
    	else:
    		os.system(("%s -ls /")%(self.hdfs))

    def rm(self, dir):
    	os.system(("%s -rm /%s")%(self.hdfs,dir))

    def rm_dir(self, dir):
        os.system(("%s -rm -r /%s")%(self.hdfs,dir))

    def put(files,dir):
        os.system(("%s -put %s /%s")%(self.hdfs,files,dir))

    def get(self, dir, name):
        os.system(("%s -get /%s/part-00000 .")%(self.hdfs,dir))
        os.system(("mv part-00000 %s.dat")%(name))

    def cat(self, file):
    	system(("%s -cat /%s")%(self.hdfs,file))

    def chgrp(self, mode, file):
    	system(("%s -chgrp %s /%s")%(self.hdfs,mode,file))

    def chmod(self, mode,file):
    	system(("%s -chmod %s /%s")%(self.hdfs,mode,file))

    def chown(self, mode,file):
    	system(("%s -chown %s /%s")%(self.hdfs,mode,file))

class hadoop:
    def __init__(self, hadoop_sbin="/usr/local/hadoop/sbin"):
        self.sbin = hadoop_sbin

    def start_all(self,):
        os.system(("%s/start-all.sh")%(self.sbin))

    def stop_all(self,):
        os.system(("%s/stop-all.sh")%(self.sbin))

    def balancer_start(self,):
        os.system(("%s/start-balancer.sh")%(self.sbin))

    def balancer_stop(self,):
        os.system(("%s/stop-balancer.sh")%(self.sbin))

    def dfs_start(self,):
        os.system(("%s/start-dfs.sh")%(self.sbin))

    def dfs_stop(self,):
        os.system(("%s/stop-dfs.sh")%(self.sbin))

    def dns_start(self,):
        os.system(("%s/start-secure-dns.sh")%(self.sbin))

    def dns_stop(self,):
        os.system(("%s/stop-secure-dns.sh")%(self.sbin))

    def yarn_start(self,):
        os.system(("%s/start-yarn.sh")%(self.sbin))

    def yarn_stop(self,):
        os.system(("%s/stop-yarn.sh")%(self.sbin))

    def format_namenode():
        s_n = input("Deseja realmente formatar o seu HDFS? (S/N)")
        if s_n == "S" or "s":
            os.system("/usr/local/hadoop/bin/hdfs namenode -format")

    def format_datanode():
        s_n = input("Deseja realmente formatar o seu HDFS? (S/N)")
        if s_n == "S" or "s":
            os.system("/usr/local/hadoop/bin/hdfs datanode -format")

class map_reduce:
    def __init__(self,
                hadoop_streaming="/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.*.jar"
                hadoop_dir="/usr/local/hadoop/bin/hadoop"):

        self.streaming = hadoop_streaming
        self.hadoop = hadoop_dir

    def run_map_reduce(self, mapper, reducer,
                        _input,output):

    	os.system(("%s jar %s \
    	-mapper %s \
    	-reducer %s \
    	-input /%s \
    	-output /%s")%(self.hadoop,self.streaming,mapper,reducer,_input,output)

    def run_map(self, mapper,
                _input, output):

        os.system(("%s jar %s \
    	-mapper %s \
    	-input /%s \
    	-output /%s")%(self.hadoop,self.streaming,mapper,reducer,_input,output)

    def run_map_combiner_reduce(self, mapper, combiner,
                                reducer, _input, output):

        os.system(("%s jar %s \
    	-mapper %s \
    	-reducer %s \
        -combiner %s \
    	-input /%s \
    	-output /%s")%(self.hadoop,self.streaming,mapper, combiner,reducer,_input,output)

    def run_pass_flags(self, parameter):
        """
        here you can you only parameter,
        but you need write all streaming command
        before streaming
        """
        os.system(("%s jar %s %s")%(self.hadoop, self.streaming, parameter))
