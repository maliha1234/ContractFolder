import pandas as pd
import numpy as np

def block():
	# this is the label file for local experiment on debo s smart contract
	dataset = pd.read_csv("/Users/malihasarwat/Documents/Summer2020/Sir/DEBO_smartcontract/contracts/ecr2/label_with_block_smart_contract_debo_local.csv")

 # Then I downloaded from remote server the final label csv file for 60k contract
 
	#print(dataset.groupby(['Name','label']).count())
	df = dataset.groupby(['Name','label']).count()

	#print(df)

	df.to_csv ("/Users/malihasarwat/Documents/Summer2020/Sir/DEBO_smartcontract/contracts/ecr2/label_analysis.csv",  header=True)
	#print(df["label"].max())


def find():
	import csv
	dict={}
	with open("/Users/malihasarwat/Documents/Summer2020/Sir/DEBO_smartcontract/contracts/ecr2/label_analysis.csv") as csv_file:
	        csv_reader = csv.reader(csv_file, delimiter=',' )
	        count_label_0 = 0
	        for row in csv_reader:
	        	
	        	if(row[1] =='0'):
	        		count_label_0 = row[2]
	        		#print (row[0]) 

	        	if(row[1] =='1'):
	        		count_label_1 = row[2]
	        		percentage = 100* int(count_label_1) /(int(count_label_0)+int(count_label_1))

	        		key = row[0]

	        		dict[key] = percentage

	        max_value =0
	        key_max = ""
	        avg = 0
	        for key in dict:
	        	avg+= dict[key]

	        	if dict[key]>max_value:
	        		max_value = dict[key]
	        		key_max = key
	        print(str(key_max)+ "," +str(max_value) + "\n")

	        avg = avg/len(dict)
	        print(avg)



if __name__ == "__main__": 
    block()
    find()