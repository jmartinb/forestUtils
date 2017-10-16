# forestUtils

###### multiPDs

Scripts and configs to run forest for multiple PDs. Pay attention to the folders structure, since it is intended to run separately for different runs, so modify it according to your needs

* crabConfig is run like: 'python crabConfig.py'

It will run 'crab submit' for each PD in the loop list, so it will create N_PD tasks.

* You can use './crabSubmit.sh' in case you want to run for different runs separately

* You can use './crabStatus.sh runNumber' to check the status of the jobs for all the tasks

* You can use './crabGetOutput.sh runNumber' to get the outputs for a given run

* You can use './hadd.sh runNumber' to merge the output of each job in a single .root file 


###################
