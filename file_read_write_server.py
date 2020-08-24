filepath = '/home/maliha/smartcontract/DEBO_smartcontract/contracts/ecr20000000000000'
projectdir = '/home/maliha/smartcontract/DEBO_smartcontract/contracts/ecr2/smartcontract_Bytecode/'
f = open(filepath, "r")
cnt = 1
lines = f.readlines()
import os
filename='smart_contract_'
for line in lines:
 filename='smart_contract_'+ str(cnt)
 outF=open(projectdir+filename, "w")
 outF.write(str(line))
 cnt+=1

