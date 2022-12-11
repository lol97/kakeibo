'''
code for simple kakeibo
IDEA :
-> write transaction and save to 'dataframe pandas'
by lol97 / warteg dust
'''

from datetime import datetime
import pandas as pd
import os 

# EXPLAIN DF
columns = ['date','name','nominal']

# CSV file transaksi
DF_FILE_CSV = "df_kakeibo2.csv"


def loadDataFrame(fileName):
	if os.path.isfile(fileName):
		return pd.read_csv(fileName)
	else:
		df = pd.DataFrame(columns=columns)
		df.to_csv(fileName, index = False)
		return df

def dfWrite(df, fileName = DF_FILE_CSV):
	print(df)
	df.to_csv(fileName, index = False)

# load data frame
df = loadDataFrame(DF_FILE_CSV)

def createTransaction(name, nominal, date = datetime.now(), df = df):
	print("creating transaction")
	print("name -> " + name)
	print("nominal -> " + str(nominal))
	print("waktu -> " + str(date))
	df = df.append({
		'name': name,
		'date': date,
		'nominal': nominal
	}, ignore_index=True)
	dfWrite(df)
	print("creating transaction")

createTransaction("belanja", 1000000, df = df)