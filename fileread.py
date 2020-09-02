filepath = '/Users/malihasarwat/Documents/Summer2020/Sir/DEBO_smartcontract/contracts/ecr20000000000000'
projectdir = '/Users/malihasarwat/Documents/Summer2020/Sir/DEBO_smartcontract/contracts/ecr2/smartcontract_Bytecode_folder/'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
   	line = fp.readline()
   	filename = 'smart_contract_' + str(cnt) + '.txt'
    
    #print("Line {}: {}" + line)
    
    outF = open(projectdir+filename, "w")   
  	outF.write(line)
  	#outF.write("\n")
	
    cnt += 1