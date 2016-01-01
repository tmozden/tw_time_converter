import TW_village
import math
import TW_time as TIME

class TW_distance_calculator:

    travel_times = { 'spear' : 18, 'sword' : 22, 'axe' : 18, 'archer' : 18, 'scout' : 9, 'lc' : 10, 'ma' : 10, 'hc' : 11, 'ram' : 30, 'cat' : 30, 'noble' : 35 }


    def calc_dist( self, village1, village2 ):
        vil1_coords = village1.get_coords()
        vil2_coords = village2.get_coords()
        xone_xtwo = math.pow( ( vil2_coords[0] - vil1_coords[0] ), 2)
        yone_ytwo = math.pow( ( vil2_coords[1] - vil1_coords[1] ), 2)
        dist = math.sqrt( xone_xtwo + yone_ytwo  ) 
        return dist

    def calc_travel_time( self, unit, distance ):
        
        unit_travel_time = ( self.travel_times[ unit ] * 60 )
        total_travel_time = ( unit_travel_time * distance )
        new_time = TIME.TW_time()
        new_time.set_total_time( total_travel_time )
        return new_time

    def launch_time_calc( self, attacker_vil, defender_vil, unit, landing_time ):
        dist = self.calc_dist( attacker_vil, defender_vil )
        travel_time = self.calc_travel_time( unit, dist )
        launch_time = landing_time - travel_time
        return launch_time
