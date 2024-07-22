import os
from tkinter import filedialog as fd

import pyspark.sql.functions as F
from pyspark.sql import SparkSession
from pyspark.sql.types import FloatType, IntegerType, StringType

os.system('clear')

directory = os.path.dirname(os.path.abspath(__file__))
path = f'{directory}/file'
path = fd.askopenfilename(title='Select a file input',
        initialdir = directory,
        initialfile = path,
        )

spark = SparkSession.builder.getOrCreate()
df = spark.read.csv(path, header=False, inferSchema=False,sep='@')
col_p = ["_c0","c0"]
cols = ['c1','c2','c3','c4']

df = (df.select('_c0')
 .withColumn('c0', F.split(F.col('_c0'), r'[-.,\s]+'))
 .withColumn('c1',F.col('c0')[0].cast(IntegerType()))
 .withColumn('c2',F.col('c0')[1].cast(IntegerType()))
 .withColumn('c3',F.col('c0')[2].cast(IntegerType()))
 .withColumn('c4',F.col('c0')[3].cast(IntegerType()))
 .withColumn('SORTED IP ADRRESSES',F.concat_ws(".",*cols))
)
df = df.orderBy(*cols)
df = df.drop(*col_p,*cols)
df.show()