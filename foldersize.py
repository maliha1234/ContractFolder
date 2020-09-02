project_dir= "/Users/malihasarwat/Documents/Summer2020/Sir/FengCodes/"

def num_total_basic_blocks(dict,label,smart_contract_name):
    #Number total basic blocks
    total_basic_blocks = len(dict)
    write = smart_contract_name+","+str(total_basic_blocks)+"\n"
    import os
    file = 'label'+str(label)+'_num_total_basic_blocks.csv'

    f = open(project_dir+csv_dir+file, "a+")
    f.write(write)
def max_instructions(dict,label,smart_contract_name):
    #Max number of instruction of a single block
    max=0;
    for key in dict:
        if len(dict[key])>max:
            max=len(dict[key])
    file = 'label'+str(label) + '_max_instructions_block.csv'
    write = smart_contract_name+","+str(max)+"\n"
    print("$$$$ wring to max max_instructions",file)
    f = open(project_dir+csv_dir+file, "a+")
    f.write(write)
def get_opc_dict(dir,dict,label,smart_contract_name):
    for key in dict:
        list=[]
        for value in dict[key]:
            list.append(getopcname(dir,value))
        dict[key]= list
    print(dict)

    # 1,2,3 ,9, 10, 11, 12
    condition_op_block(dir,dict,label,smart_contract_name)
    uncondition_op_block(dir,dict,label,smart_contract_name)
    eq_op_block(dir,dict,label,smart_contract_name)
    zero_count_op_block(dir,dict,label,smart_contract_name)
    data_load_op_block(dir,dict,label,smart_contract_name)
    sha_op_block(dir,dict,label,smart_contract_name)
    revert_op_block(dir,dict,label,smart_contract_name)
    # 1,2,3, 9, 10,11,12

    # arith_opc_block(dir,dict,label,smart_contract_name)
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

def condition_op_block(dir,dict,label,smart_contract_name):
    opc_dict=dict
    #Number of conditional branch in a single block
    numdict=opc_dict
    numdict_track={}
    condition_opc = ["JUMPI"]
    for key in numdict:
        count=0;
        for value in numdict[key]:
            if value in condition_opc:
                count=count+1;
        numdict_track[key]=count;

    file = 'label'+str(label)+'single_block_condition.csv'
    for key in numdict_track:
        write = smart_contract_name+","+str(numdict_track[key])+"\n"
        f = open(project_dir+csv_dir+file, "a+")
        f.write(write)

def uncondition_op_block(dir,dict,label,smart_contract_name):
    opc_dict=dict
    #Number of unconditional branch in a single block
    numdict=opc_dict
    numdict_track={}
    condition_opc = ["JUMP"]
    for key in numdict:
        count=0;
        for value in numdict[key]:
            if value in condition_opc:
                count=count+1;
        numdict_track[key]=count;

    file = 'label'+str(label)+ 'single_block_uncondition.csv'
    for key in numdict_track:
        write = smart_contract_name+","+str(numdict_track[key])+"\n"
        f = open(project_dir+csv_dir+file, "a+")
        f.write(write)

def eq_op_block(dir,dict,label,smart_contract_name):
    opc_dict=dict
    #Number of equal check in a single block
    numdict=opc_dict
    numdict_track={}
    condition_opc = ["EQ"]
    for key in numdict:
        count=0;
        for value in numdict[key]:
            if value in condition_opc:
                count=count+1;
        numdict_track[key]=count;

    file = 'label'+str(label)+'single_block_eq.csv'
    for key in numdict_track:
        write = smart_contract_name+","+str(numdict_track[key])+"\n"
        f = open(project_dir+csv_dir+file, "a+")
        f.write(write)

def get_definition_dict(dir,dict,label,smart_contract_name):
    numdict_track={}
    try:
        f=open(dir+"/def.facts", 'r')

        for key in dict:
            count=0;
            lines=f.readlines()
            for value in dict[key]:
                for line in lines:
                    if value == line.split()[1]:
                        count=count+1;
                        print("COUNT" + str(value) + "888888" + str(count))
            numdict_track[key]=count;

        file = 'label'+str(label)+'single_block_definition.csv'
        for key in numdict_track:
            write = smart_contract_name+","+str(numdict_track[key])+"\n"
            f = open(project_dir+csv_dir+file, "a+")
            f.write(write)

    except FileNotFoundError:
        print("Wrong file or file path")

def get_use_dict(dir,dict,label,smart_contract_name):
    numdict_track={}

    try:    
        f=open(dir+"/use.facts", 'r')

        for key in dict:
            count=0;
            lines=f.readlines()
            for value in dict[key]:
                for line in lines:
                    if value == line.split()[1]:
                        count=count+1;
                        # print("Key" + key + "COUNT" + str(value) + "999999" + str(count))
            numdict_track[key]=count;

        file = 'label'+str(label)+'single_block_use.csv'
        for key in numdict_track:
            write = smart_contract_name+","+str(numdict_track[key])+"\n"
            f = open(project_dir+csv_dir+file, "a+")
            f.write(write)

    except FileNotFoundError:
        print("Wrong file or file path")

def get_back_edge_dict(dir,dict,label,smart_contract_name):
    numdict_track={}
    try:
        f=open(dir+"/CFGEdge.facts", 'r')

       
        lines=f.readlines()
        
        count = 0;
        for line in lines:
            start_point = line.split()[0];
            numdict_track[start_point]=1;
            end_point = line.split()[1];
            if end_point in numdict_track.keys():
                count = count+1;

        file = 'label'+str(label)+'single_block_back_edge.csv'
        
        write = smart_contract_name+","+str(count)+"\n"
        f = open(project_dir+csv_dir+file, "a+")
        f.write(write)

    except FileNotFoundError:
        print("Wrong file or file path")

def get_entry_exit_dict(dir,dict,label,smart_contract_name):
    
    try:
        f=open(dir+"/entry.facts", 'r')

        lines=f.readlines()
        count = len(lines)  

        file = 'label'+str(label)+'single_block_entry.csv'
        
        write = smart_contract_name+","+str(count)+"\n"
        f = open(project_dir+csv_dir+file, "a+")
        f.write(write)

    except FileNotFoundError:
        print("Wrong file or file path")


    
    try:
        f=open(dir+"/exit.facts", 'r')

        lines=f.readlines()
        count = len(lines)  

        file = 'label'+str(label)+'single_block_exit.csv'
        
        write = smart_contract_name+","+str(count)+"\n"
        f = open(project_dir+csv_dir+file, "a+")
        f.write(write)

    except FileNotFoundError:
        print("Wrong file or file path")


def zero_count_op_block(dir,dict,label,smart_contract_name):
    opc_dict=dict
    #Number of unconditional branch in a single block
    numdict=opc_dict
    numdict_track={}
    condition_opc = ["ISZERO"]
    for key in numdict:
        count=0;
        for value in numdict[key]:
            if value in condition_opc:
                count=count+1;
        numdict_track[key]=count;

    file = 'label'+str(label)+'single_block_zero_count.csv'
    for key in numdict_track:
        write = smart_contract_name+","+str(numdict_track[key])+"\n"
        f = open(project_dir+csv_dir+file, "a+")
        f.write(write)

def data_load_op_block(dir,dict,label,smart_contract_name):
    opc_dict=dict
    #Number of unconditional branch in a single block
    numdict=opc_dict
    numdict_track={}
    condition_opc = ["CALLDATALOAD"]
    for key in numdict:
        count=0;
        for value in numdict[key]:
            if value in condition_opc:
                count=count+1;
        numdict_track[key]=count;

    file = 'label'+str(label)+'single_block_data_load_count.csv'
    for key in numdict_track:
        write = smart_contract_name+","+str(numdict_track[key])+"\n"
        f = open(project_dir+csv_dir+file, "a+")
        f.write(write)

def sha_op_block(dir,dict,label,smart_contract_name):
    opc_dict=dict
    #Number of unconditional branch in a single block
    numdict=opc_dict
    numdict_track={}
    condition_opc = ["SHA3"]
    for key in numdict:
        count=0;
        for value in numdict[key]:
            if value in condition_opc:
                count=count+1;
        numdict_track[key]=count;

    file = 'label'+str(label)+'single_block_sha_count.csv'
    for key in numdict_track:
        write = smart_contract_name+","+str(numdict_track[key])+"\n"
        f = open(project_dir+csv_dir+file, "a+")
        f.write(write)

def revert_op_block(dir,dict,label,smart_contract_name):
    opc_dict=dict
    #Number of unconditional branch in a single block
    numdict=opc_dict
    numdict_track={}
    condition_opc = ["REVERT"]
    for key in numdict:
        count=0;
        for value in numdict[key]:
            if value in condition_opc:
                count=count+1;
        numdict_track[key]=count;

    file = 'label'+str(label)+'single_block_revert_count.csv'
    for key in numdict_track:
        write = smart_contract_name+","+str(numdict_track[key])+"\n"
        f = open(project_dir+csv_dir+file, "a+")
        f.write(write)

def writeSome(dir,dict,label,smart_contract_name,numdict_track,numdict_max_track,numdict_load_track):
    #Number of arithmetic operation in a single block
    #Maximum number of arithmetic operation from any single block
    #Number of load and store operation in a single block
    file = 'label'+str(label)+'single_block_arith.csv'
    for key in numdict_track:
        write = smart_contract_name+","+str(numdict_track[key])+"\n"
        f = open(project_dir+csv_dir+file, "a+")
        f.write(write)
    file = 'label'+str(label)+'single_block_load.csv'
    for key in numdict_load_track:
        write = smart_contract_name+","+str(numdict_load_track[key])+"\n"
        f = open(project_dir+csv_dir+file, "a+")
        f.write(write)
    file = 'label'+str(label)+'single_block_max_arith.csv'
    write = smart_contract_name+","+str(numdict_max_track)+"\n"
    f = open(project_dir+csv_dir+file, "a+")
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
    #print(len(path))

def deal_one_dir(dir):
    path=[]
    # print("enter dir",dir)
    os.chdir(dir)
    for file in glob.glob("*"):
            if os.path.isdir(file):
                # print(file)
                path.append(dir+'/'+file)
                # print("the path is",path)
    #for one in path:
        # deal_one_file('/media/feng/Samsung_T5/decompile/'+one);
    #    print("one",one)
        #deal_one_contract(one);
    print(len(path))

def deal_one_contract(dir):
    smart_contract_name= dir.split("/")[-1]
    dict=getblock_dict(dir)
    label= getlabel(project_dir+smart_contract_name)
    # max= max_instructions(dict,label,smart_contract_name)
    opc = get_opc_dict(dir,dict,label,smart_contract_name) # 1,2,3,9,10,11,12
    definition = get_definition_dict(dir,dict,label,smart_contract_name) # 4
    backeddge = get_back_edge_dict(dir,dict,label,smart_contract_name) # 5
    entry_exit = get_entry_exit_dict(dir,dict,label,smart_contract_name) # 6,7
    use = get_use_dict(dir,dict,label,smart_contract_name) # 8
    # an = num_total_basic_blocks(dict,label,smart_contract_name)
if __name__ == "__main__":
    fetch_dirfiles(project_dir)
    