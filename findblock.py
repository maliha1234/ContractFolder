project_dir= "/Users/malihasarwat/Documents/Summer2020/Sir/FengCodes"
def num_total_basic_blocks(dict,label,smart_contract_name):
    #Number total basic blocks
    total_basic_blocks = len(dict)
    write = smart_contract_name+","+str(total_basic_blocks)+"\n"
    import os
    file = 'label'+str(label)+'_num_total_basic_blocks.csv'

    f = open(project_dir+file, "a+")
    f.write(write)
def max_instructions(dict,label,smart_contract_name):
    #Max number of instruction of a single block
    max=0;
    for key in dict:
        if len(dict[key])>max:
            max=len(dict[key])
    file = 'label'+str(label)+'_max_instructions_block.csv'
    write = smart_contract_name+","+str(max)+"\n"
    print("$$$$ wring to max max_instructions",file)
    f = open(project_dir+file, "a+")
    f.write(write)
def get_opc_dict(dir,dict,label,smart_contract_name):
    for key in dict:
        list=[]
        for value in dict[key]:
            list.append(getopcname(dir,value))
        dict[key]= list
    print(dict)
    arith_opc_block(dir,dict,label,smart_contract_name)
    # return dict
def arith_opc_block(dir,dict,label,smart_contract_name):
    opc_dict=dict
    #Number of arithmetic operation in a single block
    numdict=opc_dict
    numdict_track={}
    arit_opc = ["ADD","MUL","SUB","DIV","SDIV","SMOD","ADDMOD","MULMOD","EXP","SIGNEXTEND"]
    for key in numdict:
        count=0;
        for value in numdict[key]:
            if value in arit_opc:
                count=count+1;
        numdict_track[key]=count;
    #Maximum number of arithmetic operation from any single block
    numdict_max_track=0;
    max=0;
    for key in numdict_track:
        if max<numdict_track[key]:
            max = numdict_track[key]
    numdict_max_track =max



    loadstore=["MLOAD","MSTORE","MSTORE8","SLOAD","SSTORE"]
    #Number of load and store operation in a single block
    numdict_load_track={}
    for key in numdict:
        count=0;
        for value in numdict[key]:
            if value in loadstore:
                count=count+1;
        numdict_load_track[key]=count;
    print("numdict_track",numdict_track)
    print("numdict_max_track",numdict_max_track)
    print("numdict_load_track",numdict_load_track)
    writeSome(dir,dict,label,smart_contract_name,numdict_track,numdict_max_track,numdict_load_track)

def writeSome(dir,dict,label,smart_contract_name,numdict_track,numdict_max_track,numdict_load_track):
    #Number of arithmetic operation in a single block
    #Maximum number of arithmetic operation from any single block
    #Number of load and store operation in a single block
    file = 'label'+str(label)+'single_block_arith.csv'
    for key in numdict_track:
        write = smart_contract_name+","+str(numdict_track[key])+"\n"
        f = open(project_dir+file, "a+")
        f.write(write)
    file = 'label'+str(label)+'single_block_load.csv'
    for key in numdict_load_track:
        write = smart_contract_name+","+str(numdict_load_track[key])+"\n"
        f = open(project_dir+file, "a+")
        f.write(write)
    file = 'label'+str(label)+'single_block_max_arith.csv'
    write = smart_contract_name+","+str(numdict_max_track)+"\n"
    f = open(project_dir+file, "a+")
    f.write(write)
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
        print(line)
        block = line.split()[1];
        value = line.split()[0];
        if block not in dict.keys():
            dict[block]= [value]
        else:
            dict[block].append(value)
    print(dict)
    return dict
def getlabel(dir):
    newdir = dir.split("/")[-1]
    print("newdir",newdir)
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
        print("one",one)
        deal_one_contract(one);
def deal_one_contract(dir):
    smart_contract_name= dir.split("/")[-1]
    dict=getblock_dict(dir)
    label= getlabel(project_dir+smart_contract_name)
    max= max_instructions(dict,label,smart_contract_name)
    opc = get_opc_dict(dir,dict,label,smart_contract_name)
    an = num_total_basic_blocks(dict,label,smart_contract_name)
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
