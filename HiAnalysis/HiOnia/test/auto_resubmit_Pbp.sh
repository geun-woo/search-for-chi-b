#
while true;
do
#
echo -e "crab st -d crab_chi_b_analysis_Pbp/"
crab st -d crab_chi_b_analysis_Pbp/
minutes=60
seconds=`expr $minutes \* 60`
echo -e "\n----------waiting for $minutes minites----------\n"
sleep $seconds
#
echo -e "crab resubmit -d crab_chi_b_analysis_Pbp/"
crab resubmit -d crab_chi_b_analysis_Pbp/
#
done
