
class TW_player:

    def calc_timezone( self, zone ):
        if zone == 'eastern':
            return 19
        elif zone == 'central':
            return 18
        elif zone == 'moutian':
            return 17
        elif zone == 'pacific':
            return 16
        else:
            return None

    def __init__( self, player_name = '', tribe = '', time_zone = 'eastern' ):
        self.player_name = player_name
        self.tribe = tribe
        #self.villages = villages
        self.time_zone = self.calc_timezone( time_zone )

    def set_timezone( self, zone ):
        self.time_zone = self.calc_timezone( zone )

#    def clear_village_list( self ):
#        self.villages = None
#
#    def add_village( self, village ):
#        self.villages.append( village )
#
#    def get_villages( self ):
#        return self.villages

    def get_tribe( self ):
        return self.tribe

    def set_tribe( self, tribe ):
        self.tribe = tribe

    def get_player_name( self ):
        return self.player_name
    
    def get_time_zone( self ):
        return self.time_zone




