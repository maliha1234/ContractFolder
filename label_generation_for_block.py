#For my local contract
#project_dir= "/Users/malihasarwat/Documents/Summer2020/Sir/FengCodes/"

#for debo contract

project_dir= "/Users/malihasarwat/Documents/Summer2020/Sir/DEBO_smartcontract/contracts/ecr2/"

#for server

#project_dir= "/home/maliha/smartcontract/DEBO_smartcontract/contracts/ecr2/"






 
def get_opc_dict(dir,dict,smart_contract_name):
    
    try:
        for key in dict:
            list=[]
            for value in dict[key]:
                list.append(getopcname(dir,value))
            dict[key]= list
        #print(dict)

        label = Labal_arith_opc_block(dir,dict,smart_contract_name)
        
      
    except:
        print("Wrong file or file path")


def arith_opc_block(dir,dict,smart_contract_name):
    opc_dict=dict
    #Number of arithmetic operation in a single block
    numdict=opc_dict
    numdict_track={}
    arit_opc = ["ADD","SUB"]
    for key in numdict:
        count=0;
        for value in numdict[key]:

            if value in arit_opc:
                
                print(numdict[key])
                
    return 0


def Labal_arith_opc_block(dir,dict,smart_contract_name):
    opc_dict=dict
    #Number of arithmetic operation in a single block
    numdict=opc_dict
    numdict_track={}
    
    arit_opc = ["ADD","SUB"]
    push_opc = ["MLOAD","SLOAD"]
    previous_opc = ["CONST"]
    label = 0
    for key in numdict:
        label = 0
        valueList = numdict[key]
        

        for i in range(len(valueList)):
    
                #count=count+1;
            #print(valueList[i])

            if i>3 :

                if ((valueList[i] in arit_opc)  and (valueList[i-1] in push_opc)) :
                    #print(valueList[i-2] + "," + valueList[i-1] + "," +  valueList[i] )
                    label =1 
                    break;
        
        file = 'label_with_block_smart_contract_debo_local.csv' 

        write = smart_contract_name +","+  str(key)+ ","+ str(label) + "\n"
        f = open(project_dir+file, "a+")
        f.write(write)

    return 0

   


    

def getopcname(dir,opcaddr):
    f=open(dir+"/op.facts", 'r')
    addr="";
    if "finish" not in opcaddr:
        addr = opcaddr
    else:
        addr = opcaddr.split()[0]
    lines=f.readlines()
    for line in lines:
        # print(lines)
        if addr == line.split()[0]:
            return line.split()[1]
    raise Exception("Sorry, no opcode found foropcaddr: ",opcaddr,"in dir: ",dir)
def getblock_dict(dir):
    dict={}
    f=open(dir+"/block.facts", 'r')

    lines=f.readlines()
    for line in lines:
        #print(line)
        block = line.split()[1];
        value = line.split()[0];
        if block not in dict.keys():
            dict[block]= [value]
        else:
            dict[block].append(value)
    #print(dict)
    return dict
def getlabel(dir):
    newdir = dir.split("/")[-1]
    #print("newdir",newdir)
    import csv

    with open(project_dir+"/"+"AllSmartContractBinLabel_Oyente.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if row[0]== newdir:
                print('label',row[1])
                return row[1]

import sys
import glob, os
def fetch_dirfiles(dir):
    dir = dir+"/CFGs1"
    # print(dir)
    os.chdir(dir)
    path =[];
    for file in glob.glob("*"):
        if os.path.isdir(file):
            # print(file)
            path.append(dir+'/'+file)
            # print("the path is",path)
    for one in path:
        # deal_one_file('/media/feng/Samsung_T5/decompile/'+one);
        # print("path",path)
        try:
            deal_one_dir(one);
        except:
            print("exception")

def deal_one_dir(dir):
    path=[]
    # print("enter dir",dir)
    os.chdir(dir)
    for file in glob.glob("*"):
            if os.path.isdir(file):
                # print(file)
                path.append(dir+'/'+file)
                # print("the path is",path)
    for one in path:
        # deal_one_file('/media/feng/Samsung_T5/decompile/'+one);
        #print("one",one)
        try :
            deal_one_contract(one);
        except:
            print("exception")
def deal_one_contract(dir):
    smart_contract_name= dir.split("/")[-1]
    dict = getblock_dict(dir)
    
    opc = get_opc_dict(dir,dict,smart_contract_name) 
    
if __name__ == "__main__":
    fetch_dirfiles(project_dir)
    