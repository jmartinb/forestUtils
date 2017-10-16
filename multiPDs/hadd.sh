#!/bin/sh

#  Script.sh
#  
#
#  Created by Javier Martin Blanco on 03/10/17.
#

name=""
for i in {1..20}
do
hadd ./run$1/crab_projects/crab_PAMinimumBias$i/results/HiForestAOD_run$1_MB$i.root ./run$1/crab_projects/crab_PAMinimumBias$i/results/HiForestAOD_*.root
name+=" ./run$1/crab_projects/crab_PAMinimumBias$i/results/HiForestAOD_run$1_MB$i.root"
done


hadd ./run$1/HiForestAOD_run$1.root $name
