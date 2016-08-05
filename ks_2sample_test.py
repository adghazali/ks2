import argparse 
import sys 
from scipy import stats
import MySQLdb

parser = argparse.ArgumentParser(description = 'Apply Kolmogorov Smirnov 2 sample test to all numeric columns in a table')
parser.add_argument( 't', help = 'tablename required')
parser.add_argument( '-n', help = 'NULLS assigned this value, default of 0', default = 0)
parser.add_argument( '-e', help = 'exclude the following oolumns delimited by commas') 
parser.add_argument( '-s', help = 'maximum sample size, default of 10,000', default = 10000)
args = parser.parse_args()


# connect to mysql

# create cursor object 

# find all numeric columns in mysql table using information_schema, assigning it numeric_columns

numeric_columns = []
numeric_columns.append('test')

# for curr & curr-1 monthends,  for i in numeric_columns, select a sample of size [args.s] and save to a list
curr_sample = []
prev_sample = []

for sample in [curr_sample, prev_sample]:
    for column in numeric_columns:
         
        #result = CURSOR.exec('SELECT %s FROM %s WHERE monthend = %s SAMPLE %S')
        sample.append(0)

print stats.ks_2samp(curr_sample, prev_sample)
    

