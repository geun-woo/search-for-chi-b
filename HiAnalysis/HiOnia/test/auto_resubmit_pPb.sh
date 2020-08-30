#
while true;
do
#
echo -e "crab st -d crab_chi_b_analysis_pPb/"
crab st -d crab_chi_b_analysis_pPb/
minutes=60
seconds=`expr $minutes \* 60`
echo -e "\n----------waiting for $minutes minites----------\n"
sleep $seconds
#
echo -e "crab resubmit -d crab_chi_b_analysis_pPb/"
crab resubmit -d crab_chi_b_analysis_pPb/
#
done
