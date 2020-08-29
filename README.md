# search-for-chi-b
	ssh <CERN ID>@lxplus.cern.ch 
	ssh lxplus6 
	export SCRAM_ARCH=slc6_amd64_gcc530
	# or
	ssh <CERN ID>@lxplus6.cern.ch
	export SCRAM_ARCH=slc6_amd64_gcc530

	scramv1 p -n <new_directory_name> CMSSW CMSSW_8_0_26_patch2
	cd <new_directory_name>/src/
	cmsenv
