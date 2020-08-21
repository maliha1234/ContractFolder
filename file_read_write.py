filepath = '/Users/malihasarwat/Documents/Summer2020/Sir/DEBO_smartcontract/contracts/ecr20000000000000'
projectdir = '/Users/malihasarwat/Documents/Summer2020/Sir/DEBO_smartcontract/contracts/ecr2/smartcontract_Bytecode_folder/'
f = open(filepath, "r")
cnt = 1
lines = f.readlines()
import os
filename='smart_contract_text'
for line in lines:
 filename='smart_contract_text'+ str(cnt)
 outF=open(projectdir+filename, "w")
 outF.write(str(line))
 cnt+=1
 
