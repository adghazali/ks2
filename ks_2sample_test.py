import argparse 
import sys 
from scipy import stats
import MySQLdb

parser = argparse.ArgumentParser(description = 'Apply Kolmogorov Smirnov 2 sample test to all numeric columns in a table')
parser.add_argument( 'd', help = 'database REQUIRED')
parser.add_argument( 't', help = 'tablename REQUIRED')
parser.add_argument( 'm', help = 'monthend column, to pick up curr & curr-1 extracts REQUIRED')
parser.add_argument( '-n', help = 'NULLS assigned this value, default of 0', default = 0)
parser.add_argument( '-e', help = 'exclude the following oolumns delimited by commas') 
parser.add_argument( '-s', help = 'maximum sample size, default of 10,000', default = 10000)
args = parser.parse_args()


# connect to mysql
# create cursor object 

db = MySQLdb.connect(db = 'test')
c = db.cursor()
c.execute('SELECT * FROM %s' %args.t)
print c.fetchone()

# find all numeric columns in mysql table using information_schema, assigning it numeric_columns

numeric_columns = []

q_num_cols = 'select column_name from information_schema.columns where table_schema= \'test\' and  table_name = \'raw_stg\' and data_type = \'decimal\';'
c.execute(q_num_cols)
 

numeric_columns.append('test')

# find curr(monthend) and curr-1(monthend)


# for curr & curr-1 monthends,  for i in numeric_columns, select a sample of size [args.s] and save to a list
curr_sample = []
prev_sample = []

for sample in [curr_sample, prev_sample]:
    for column in numeric_columns:
         
        #result = CURSOR.exec('SELECT %s FROM %s WHERE monthend = %s SAMPLE %S')
        sample.append(0)

print stats.ks_2samp(curr_sample, prev_sample)
    

