#!/bin/sh

#  Script.sh
#  
#
#  Created by Javier Martin Blanco on 03/10/17.
#

for i in {1..20}
do
crab status -d /afs/cern.ch/work/j/jmartinb/private/Forest/CMSSW_8_0_28/test/forest_DATA_MB/pPb/run$1/crab_projects/crab_PAMinimumBias$i
done
