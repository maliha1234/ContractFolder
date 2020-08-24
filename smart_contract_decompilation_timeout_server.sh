#!/bin/bash


cd vandal

for file in /home/maliha/smartcontract/DEBO_smartcontract/contracts/ecr2/smartcontract_Bytecode/*; do
  echo "${file##*/}"
  path="/home/maliha/smartcontract/DEBO_smartcontract/contracts/ecr2/smartcontract_Decompile_folder/${file##*/}"
  timeout 10 bin/decompile -n -v $file -t $path

done

#wc -l $file
#wc -l ${file##*/}
#path="/Users/malihasarwat/Documents/Summer2020/Sir/DEBO_smartcontract/contracts/ecr2/smartcontract_Decompile_folder/${file##*/}"

#echo $path

#bin/decompile -n -v $file -t $path



