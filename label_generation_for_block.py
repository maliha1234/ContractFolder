project_dir= "/Users/malihasarwat/Documents/Summer2020/Sir/FengCodes/"
#project_dir= "/home/maliha/smartcontract/"






 
def get_opc_dict(dir,dict,smart_contract_name):
    
    try:
        for key in dict:
            list=[]
            for value in dict[key]:
                list.append(getopcname(dir,value))
            dict[key]= list
        #print(dict)

        label = Labal_arith_opc_block(dir,dict,smart_contract_name)
        
        # return dict

        #file = 'label_with_block_smart_.csv'
        

        #write = smart_contract_name +","+  str(key)+ ","+ str(label) 
        # write = smart_contract_name+","+ str(label)+ "," + first_six_features +"," + str(feature1) +  ","+ str(feature3)+ ","+str(feature4)+ ","+str(feature5)+ ","+str(feature6) +  ","+str(feature7) + ","+str(feature8) +  ","+str(feature9) + ","+str(feature10) + ","+str(feature11) +    ","+str(feature16) +"\n"
        #f = open(project_dir+file, "a+")
        #f.write(write)
    except:
        print("Wrong file or file path")


def arith_opc_block(dir,dict,smart_contract_name):
    opc_dict=dict
    #Number of arithmetic operation in a single block
    numdict=opc_dict
    numdict_track={}
    previous = ""
    prev_previous = ""
    arit_opc = ["ADD","SUB"]
    for key in numdict:
        count=0;
        for value in numdict[key]:

            if value in arit_opc:
                #count=count+1;
                print(numdict[key])
                #print(numdict[key].index[value])
        #numdict_track[key]=count;

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

                if ((valueList[i] in arit_opc)  and (valueList[i-1] in push_opc) and (valueList[i-2] in previous_opc )) :
                    print(valueList[i-2] + "," + valueList[i-1] + "," +  valueList[i] )
                    label =1 
                    break;
        
        file = 'label_with_block_smart_.csv' 

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
    dir = dir+"/CFGs"
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
        deal_one_dir(one);

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
        deal_one_contract(one);
def deal_one_contract(dir):
    smart_contract_name= dir.split("/")[-1]
    dict=getblock_dict(dir)
    #label= getlabel(project_dir+smart_contract_name)
    #max_instruc = max_instructions(dict,label,smart_contract_name) #12
    #avg_instruc = avg_instructions(dict,label,smart_contract_name)
    
    # definition = 
    #backeddge = get_back_edge_dict(dir,dict,label,smart_contract_name) # 14
    #entry_exit = get_entry_exit_dict(dir,dict,label,smart_contract_name) # 15 16
    #use = 
    #an = num_total_basic_blocks(dict,label,smart_contract_name) #17
    #feature12= max_definition_dict(dir,dict,label,smart_contract_name)
    #feature13= avg_definition_dict(dir,dict,label,smart_contract_name)
    #feature14= max_use_dict(dir,dict,label,smart_contract_name)
    #feature15= avg_use_dict(dir,dict,label,smart_contract_name)
    #opc = get_opc_dict(dir,dict,label,smart_contract_name) 
    #first_six_features = str(max_instruc) + ","+ str(avg_instruc) + "," + str(backeddge) + "," + str(entry_exit) + "," + str(an) + ","+str(feature12) +  ","+str(feature13) + ","+str(feature14) +  ","+str(feature15) 
    #print( "Final OUTPUT" + first_six_features+ "\n")

    opc = get_opc_dict(dir,dict,smart_contract_name) 
    
if __name__ == "__main__":
    fetch_dirfiles(project_dir)
    # main()
    # re=getblock_dict(project_dir+'2x2')
    # label= getlabel(project_dir+'2x2')
    # max = max_instructions({'0x0': ['0x0', '0x2', '0x4', '0x5', '0x7', '0x8', '0x27', '0x28', '0x2d', '0x2f', '0x34', '0x35', '0x38'], '0x39': ['0x39', '0x3a'], '0x3b': ['0x3b', '0x3c', '0x3d', '0x3e', '0x41'], '0x42': ['0x42'], '0x43': ['0x43', '0x44', '0x47', '0x4a'], '0x4b': ['0x4b', '0x4c', '0x4e', '0x51', '0x53', '0x56', '0x58', '0x5c', '0x5e', '0x5f', '0x61', '0x65', '0x67', '0x69', '0x6e', '0x71', '0x72', '0x75'], '0x76': ['0x76', '0x78', '0x7a', '0x7b', '0x7e', '0x7f', '0x80', '0x83'], '0x84': ['0x84', '0x87', '0x8a', '0x8d', '0x90', '0x93', '0x96', '0x99'], '0x9a': ['0x9a', '0xa2', '0xa4', '0xa6', '0xa8', '0xa9', '0xac'], '0xad': ['0xaf', '0xb1', '0xb2', '0xb5', '0xb7', '0xb8', '0xbb', '0xbc', '0xbd', '0xbe', '0xc0', '0xc1', '0xc3'], '0xc6': ['0xc6', '0xcc', '0xce', '0xd1', '0xd3'], '0xd4': ['0xd4', '0xd5', '0xd8', '0xdb'], '0xdc': ['0xdc', '0xdd', '0xdf', '0xe1', '0xe4', '0xe5', '0xe7', '0xe9', '0xec', '0xed', '0xef', '0xf0', '0x112', '0x113', '0x115', '0x116', '0x138', '0x139', '0x13b', '0x13c', '0x15e'], '0x162': ['0x162', '0x164'], '0x165': ['0x165', '0x166', '0x168', '0x16a', '0x16d', '0x16e', '0x170', '0x172', '0x175', '0x178'], '0x179': ['0x179', '0x17a', '0x17b', '0x182', '0x183', '0x184', '0x185', '0x186', '0x187', '0x19a', '0x19b']},0,'2x2')
    # opc= get_opc_dict(project_dir+'2x2',{'0x0': ['0x0', '0x2', '0x4', '0x5', '0x7', '0x8', '0x27', '0x28', '0x2d', '0x2f', '0x34', '0x35', '0x38'], '0x39': ['0x39', '0x3a'], '0x3b': ['0x3b', '0x3c', '0x3d', '0x3e', '0x41'], '0x42': ['0x42'], '0x43': ['0x43', '0x44', '0x47', '0x4a'], '0x4b': ['0x4b', '0x4c', '0x4e', '0x51', '0x53', '0x56', '0x58', '0x5c', '0x5e', '0x5f', '0x61', '0x65', '0x67', '0x69', '0x6e', '0x71', '0x72', '0x75'], '0x76': ['0x76', '0x78', '0x7a', '0x7b', '0x7e', '0x7f', '0x80', '0x83'], '0x84': ['0x84', '0x87', '0x8a', '0x8d', '0x90', '0x93', '0x96', '0x99'], '0x9a': ['0x9a', '0xa2', '0xa4', '0xa6', '0xa8', '0xa9', '0xac'], '0xad': ['0xaf', '0xb1', '0xb2', '0xb5', '0xb7', '0xb8', '0xbb', '0xbc', '0xbd', '0xbe', '0xc0', '0xc1', '0xc3'], '0xc6': ['0xc6', '0xcc', '0xce', '0xd1', '0xd3'], '0xd4': ['0xd4', '0xd5', '0xd8', '0xdb'], '0xdc': ['0xdc', '0xdd', '0xdf', '0xe1', '0xe4', '0xe5', '0xe7', '0xe9', '0xec', '0xed', '0xef', '0xf0', '0x112', '0x113', '0x115', '0x116', '0x138', '0x139', '0x13b', '0x13c', '0x15e'], '0x162': ['0x162', '0x164'], '0x165': ['0x165', '0x166', '0x168', '0x16a', '0x16d', '0x16e', '0x170', '0x172', '0x175', '0x178'], '0x179': ['0x179', '0x17a', '0x17b', '0x182', '0x183', '0x184', '0x185', '0x186', '0x187', '0x19a', '0x19b']},0,'2x2')
    # an = num_total_basic_blocks({'0x0': ['0x0', '0x2', '0x4', '0x5', '0x7', '0x8', '0x27', '0x28', '0x2d', '0x2f', '0x34', '0x35', '0x38'], '0x39': ['0x39', '0x3a'], '0x3b': ['0x3b', '0x3c', '0x3d', '0x3e', '0x41'], '0x42': ['0x42'], '0x43': ['0x43', '0x44', '0x47', '0x4a'], '0x4b': ['0x4b', '0x4c', '0x4e', '0x51', '0x53', '0x56', '0x58', '0x5c', '0x5e', '0x5f', '0x61', '0x65', '0x67', '0x69', '0x6e', '0x71', '0x72', '0x75'], '0x76': ['0x76', '0x78', '0x7a', '0x7b', '0x7e', '0x7f', '0x80', '0x83'], '0x84': ['0x84', '0x87', '0x8a', '0x8d', '0x90', '0x93', '0x96', '0x99'], '0x9a': ['0x9a', '0xa2', '0xa4', '0xa6', '0xa8', '0xa9', '0xac'], '0xad': ['0xaf', '0xb1', '0xb2', '0xb5', '0xb7', '0xb8', '0xbb', '0xbc', '0xbd', '0xbe', '0xc0', '0xc1', '0xc3'], '0xc6': ['0xc6', '0xcc', '0xce', '0xd1', '0xd3'], '0xd4': ['0xd4', '0xd5', '0xd8', '0xdb'], '0xdc': ['0xdc', '0xdd', '0xdf', '0xe1', '0xe4', '0xe5', '0xe7', '0xe9', '0xec', '0xed', '0xef', '0xf0', '0x112', '0x113', '0x115', '0x116', '0x138', '0x139', '0x13b', '0x13c', '0x15e'], '0x162': ['0x162', '0x164'], '0x165': ['0x165', '0x166', '0x168', '0x16a', '0x16d', '0x16e', '0x170', '0x172', '0x175', '0x178'], '0x179': ['0x179', '0x17a', '0x17b', '0x182', '0x183', '0x184', '0x185', '0x186', '0x187', '0x19a', '0x19b']},0,'2x2')
    # deal_one_contract()
    #Number total basic blocks
    #Max number of the successor of a single block
    #Max number of instruction of a single block
    #Number of arithmetic operation in a single block
    #Maximum number of arithmetic operation from any single block
    #Number of load and store operation in a single block
