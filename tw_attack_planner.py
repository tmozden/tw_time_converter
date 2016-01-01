import TW_village as VILLAGE
import TW_distance_calculator as CALC
import TW_time as TIME
import TW_file_input as FILEIN
import re

village_one = VILLAGE.TW_village( ( 511, 507 ) )
village_two = VILLAGE.TW_village( ( 514, 501 ) )
dis_calc = CALC.TW_distance_calculator()
distance = dis_calc.calc_dist(village_one, village_two)
print distance
a_time = dis_calc.calc_travel_time( 'noble', distance )
print a_time.get_time_string()

filer = FILEIN.TW_file_input()

vil_list = filer.read_new_data("new_tw_data.txt")

attacker = vil_list.pop(0)

landing_time = raw_input("enter landing time:").strip(" \n").lower()
time = re.search("(\d\d):(\d\d):(\d\d)", landing_time)
landing_time = TIME.TW_time( int(time.group(1)), int(time.group(2)), int(time.group(3)))
results_list = []
for each_vil in vil_list:
    launch_time = dis_calc.launch_time_calc( attacker, each_vil, 'lc', landing_time )
    coords = each_vil.get_coords()
    results_list.append((launch_time, coords))

results_list = sorted(results_list, key=lambda time: time[0].get_total_time())
for launch_time in results_list:
    lt_string = launch_time[0].get_time_string()
    rw_time = launch_time[0].tw_to_real_time_str( attacker.get_player().get_time_zone() )
    print rw_time + " tw time:"+lt_string + " (" + str(launch_time[1][0]) + "|" + str(launch_time[1][1]) + ") "

        

