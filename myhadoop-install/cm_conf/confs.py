# -*- coding=utf-8 -*-

# root password and ssh port. this is just for test. root password and ssh port should be
# input as the myhadoop.py args
root_pass = '123456'
ssh_port = '22'

mysql_pass = '123456' # this password will set for mysql root user and for cloudera manager databases user.

# cm_tar is you put in tars of the CM tar package
cm_tar = 'cloudera-manager-el6-cm4.6.2_x86_64.tar.gz'

""" CM connetct info  """
CM_HOST = 'platform30'
CM_PORT = '7180'
CM_USERNAME = 'admin'
CM_USER_PASSWORD = 'admin'


MB = 1024 * 1024
GB = 1024 * 1024 * 1024

""" The services conf, you can change the these conf for your own """
# zookeeper
SERVER_CONF = { # zookeeper conf
    'dataLogDir': '/home/CDH-data/zookeeper',
    'zk_server_log_dir': '/home/CDH-data/log/zookeeper',
    'zookeeper_server_java_heapsize': 128 * MB, #bytes
    'dataDir': '/home/CDH-data/zookeeper',
    'zookeeper_config_safety_valve': """"""
}

# hdfs
NAMENODE_CONF = { # Namenode conf
    'dfs_name_dir_list': '/home/CDH-data/hdfs-nn',
    'fs_trash_interval': 60,  # Minutes
    'namenode_java_heapsize': 2 * GB, #bytes
    'namenode_log_dir': '/home/CDH-data/log/hadoop-hdfs',
    'dfs_http_port': 50070,
    'namenode_java_opts': '',
    'namenode_config_safety_valve': """"""
}
DATANODE_CONF = { # datanode conf
    'dfs_data_dir_list': '/home/CDH-data/hdfs-dn',
    'dfs_datanode_handler_count': 4,
    'dfs_datanode_du_reserved': 10 * GB, #bytes
    'dfs_datanode_max_xcievers': 4096,
    'datanode_java_heapsize': 1 * GB, #bytes
    'datanode_java_opts': '',
    'datanode_config_safety_valve': """"""
}
SECONDARY_NAMENODE_CONF = { # Secondary Namenode conf
    'fs_checkpoint_dir_list': '/home/CDH-data/hdfs-snn',
    'secondary_namenode_java_heapsize': 2 * GB, #bytes
    'secondarynamenode_log_dir': '/home/CDH-data/log/hadoop-hdfs',
    'dfs_secondary_http_port': 50090,
    'secondarynamenode_java_opts': '',
    'secondarynamenode_config_safety_valve': """"""
}
JOURNALNODE_CONF = { # JournalNode conf
    'dfs_journalnode_edits_dir': '/home/CDH-data/journal_edit_logs/',
    'journalNode_java_heapsize': 256 * MB, #bytes
    'journalnode_log_dir': '/home/CDH-data/log/hadoop-hdfs',
    'dfs_journalnode_http_port': 50480,
    'jn_config_safety_valve': """"""
}

# yarn
RESOURCEMANAGER_CONF = { # resource manager conf
    'yarn_resourcemanager_scheduler_class': 'org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair'
                                            '.FairScheduler',
    'resourcemanager_fair_scheduler_configuration': """
<?xml version="1.0"?>
<allocations>
  <queue name="pool_high">
    <minResources>4096</minResources>
    <weight>6.0</weight>
    <maxRunningApps>5</maxRunningApps>
  </queue>
  <queue name="default">
    <weight>3.0</weight>
    <maxRunningApps>10</maxRunningApps>
  </queue>
  <queue name="pool_low">
    <weight>1.0</weight>
    <maxRunningApps>10</maxRunningApps>
  </queue>
  <user name="kpi">
    <maxRunningApps>9</maxRunningApps>
    <weight>3.0</weight>
  </user>
  <userMaxAppsDefault>10</userMaxAppsDefault>
  <defaultMinSharePreemptionTimeout>600</defaultMinSharePreemptionTimeout>
  <fairSharePreemptionTimeout>600</fairSharePreemptionTimeout>
  <queueMaxAppsDefault>30</queueMaxAppsDefault>
  <defaultQueueSchedulingMode>fair</defaultQueueSchedulingMode>
</allocations>
            """,
    'yarn_resourcemanager_webapp_address': '50088',
    'resource_manager_java_heapsize': 2 * GB, #bytes
    'resource_manager_log_dir': '/home/CDH-data/log/hadoop-yarn',
    'resource_manager_java_opts': '',
    'resourcemanager_config_safety_valve': """""",
    'resourcemanager_mapred_safety_valve': """"""
}
JOBHISTORY_CONF = { #jobhistory conf
    'yarn_app_mapreduce_am_staging_dir': '/user',
    'mr2_jobhistory_log_dir': '/home/CDH-data/log/hadoop-mapreduce',
    'mapreduce_jobhistory_webapp_address': 50888,
    'mr2_jobhistory_java_heapsize': 1 * GB, #bytes
    'mr2_jobhistory_java_opts': '',
    'jobhistory_mapred_safety_valve': """""",
    'jobhistory_config_safety_valve': """"""

}
NODEMANAGER_CONF = { # nodemanager conf
    'node_manager_java_heapsize': 2 * GB, #bytes
    'node_manager_log_dir': '/home/CDH-data/log/hadoop-yarn',
    'yarn_nodemanager_vmem_pmem_ratio': 2.1,
    'yarn_nodemanager_resource_memory_mb': 5 * GB, # MB
    'yarn_nodemanager_local_dirs': '/home/CDH-data/yarn-nm',
    'yarn_nodemanager_webapp_address': 50842,
    'yarn_nodemanager_log_dirs': '/home/CDH-data/log/hadoop-yarn-container',
    'nodemanager_mapred_safety_valve': """""",
    'nodemanager_config_safety_valve': """"""
}

# hbase
MASTER_CONF = { # hbase
    'hbase_master_handler_count': 25,
    'hbase_master_info_port': 50610,
    'hbase_master_logcleaner_ttl': 60000, # millisecond
    'hbase_master_log_dir': '/home/CDH-data/log/hbase',
    'hbase_master_java_heapsize': 2 * GB,
    'hbase_master_java_opts': '',
    'hbase_master_config_safety_valve': """"""
}
REGIONSERVER_CONF = { # region server conf
    'hbase_hregion_memstore_flush_size': 128 * MB, #bytes
    'hbase_regionserver_handler_count': 10,
    'hbase_regionserver_java_heapsize': 512 * MB, #bytes
    'hbase_regionserver_info_port': 50630,
    'hbase_regionserver_log_dir': '/home/CDH-data/log/hbase',
    'hbase_regionserver_lease_period': 60000, # millisecond
    'hbase_regionserver_java_opts': '',
    'hbase_regionserver_config_safety_valve': """"""
}

# hive
HIVEMETASTORE_CONF = { # hive metastore conf
    'hive_log_dir': '/var/log/hive',
    'hive_metastore_max_threads': 100000,
    'hive_metastore_min_threads': 200,
    'hive_metastore_java_heapsize': 128 * MB, #bytes
    'hive_metastore_java_opts': '',
    'hive_metastore_config_safety_valve': """"""
}


# hue
HUE_SERVER_CONF = { # hue server conf
    'hue_http_port': 8888,
    'hue_server_log_dir': '/home/CDH-data/log/hue',
    'hue_server_hue_safety_valve': """"""

}
BEESWAX_SERVER_CONF = { # beeswax server conf
    'beeswax_server_conn_timeout': 120, # seconds
    'metastore_conn_timeout': 10, # seconds
    'beeswax_log_dir': '/home/CDH-data/log/hue',
    'beeswax_server_heapsize': 128 * MB, #bytes
    'beeswax_hive_conf_safety_valve': """"""

}

# impala
IMPALAD_CONF = { # impala conf
    'impalad_memory_limit': 4 * GB, #bytes
    'log_dir': '/home/CDH-data/log/impalad',
    'impala_hive_conf_safety_valve': """""",
    'impala_hdfs_site_conf_safety_valve': """"""
}
STATESTORE_CONF = { # impala state store
    'log_dir': '/home/CDH-data/log/statestore',
    'state_store_num_server_worker_threads': 4
}

# Oozie
OOZIE_SERVER_CONF = { # Oozie server conf
    'oozie_log_dir': '/home/CDH-data/log/oozie',
    'oozie_java_heapsize': 512 * MB, #bytes
    'oozie_data_dir': '/home/CDH-data/oozie-data',
    'oozie_config_safety_valve': """"""
}

# flume
AGENT_CONF = { # flume conf
    'agent_java_heapsize': 256 * MB, #bytes
    'agent_home_dir': '/home/CDH-data/flume-ng',
    'agent_name': 'tier1',
    'agent_config_file': """
# Please paste flume.conf here. Example:

# Sources, channels, and sinks are defined per
# agent name, in this case 'tier1'.
tier1.sources  = source1
tier1.channels = channel1
tier1.sinks    = sink1

# For each source, channel, and sink, set
# standard properties.
tier1.sources.source1.type     = netcat
tier1.sources.source1.bind     = 127.0.0.1
tier1.sources.source1.port     = 9999
tier1.sources.source1.channels = channel1
tier1.channels.channel1.type   = memory
tier1.sinks.sink1.type         = logger
tier1.sinks.sink1.channel      = channel1

# Other properties are specific to each type of
# source, channel, or sink. In this case, we
# specify the capacity of the memory channel.
tier1.channels.channel1.capacity = 100
    """
}