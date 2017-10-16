#!/bin/sh

#  Script.sh
#  
#
#  Created by Javier Martin Blanco on 03/10/17.
#

for i in 285479 285480 285505 285517 285530 285537 285538 285539 285549 285684 285718 285726 285750 285759 285832
do
cd /afs/cern.ch/work/j/jmartinb/private/Forest/CMSSW_8_0_28/test/forest_DATA_MB/pPb/run$i
python crabConfig.py
done
