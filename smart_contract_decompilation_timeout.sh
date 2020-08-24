#!/bin/bash


cd /Users/malihasarwat/Documents/Summer2020/Sir/DEBO_smartcontract/vandal

for file in /Users/malihasarwat/Documents/Summer2020/Sir/DEBO_smartcontract/contracts/ecr2/sm_test/*; do
  echo "${file##*/}"
  path="/Users/malihasarwat/Documents/Summer2020/Sir/DEBO_smartcontract/contracts/ecr2/sm_decompile_test/${file##*/}"
  gtimeout 50 bin/decompile -n -v $file -t $path

done

#wc -l $file
#wc -l ${file##*/}
#path="/Users/malihasarwat/Documents/Summer2020/Sir/DEBO_smartcontract/contracts/ecr2/smartcontract_Decompile_folder/${file##*/}"

#echo $path

#bin/decompile -n -v $file -t $path



