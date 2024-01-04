""""""
from datetime import datetime

# HDFS & HIVE ACCESS
HDFS_JOB_HISTORY_SERVER = "http://192.168.64.102:19888/"
HDFS_LINK = "192.168.64.102:9870"

HIVE_METASTORE_HOSTNAME = "192.168.64.102:3306"

HDFS_HOST = "192.168.64.102"
HDFS_PORT = 9870

HIVE_HOST = "192.168.64.102"
HIVE_PORT = 10000
HIVE_THRIFT_PORT = 9088


# PATHS

HDFS_DEFULT_EDW_PSA_PATH = "/edw/hive/psa/"
HDFS_DEFULT_EDW_TMP_PATH = "/edw/hive/tmp/"
HDFS_DEFULT_EDW_BCK_PSA_PATH = "/edw/hive/bck_psa/"

# UTILS

CONCAT_PK_STRING = "_||_"
CONCAT_COLDIFF_STRING = "_||_"

PARQUET_COMPRESSION = "snappy"

PK_COLUMNNAME = "pk"

BATCH_FILENAME = "BATCH"
UPDATED_FILENAME = "UPDATE"


DT_MAX_VALID_DATETIME = datetime(2100, 12, 31)
