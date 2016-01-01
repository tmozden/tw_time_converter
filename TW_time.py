
class TW_time:

    def __init__( self, hours = 0, minutes = 0, seconds = 0 ):
        self.hrs = hours
        self.mins = minutes
        self.secs = seconds
        self.update_total_time()

    def set_hrs( self, hrs ):
        self.hrs = hrs
        update_total_time()

    def set_mins( self, mins ):
        self.mins = mins
        update_total_time()

    def set_secs( self, secs ):
        self.secs = secs
        update_total_time()

    def set_time( self, time_tuple ):
        self.set_hrs( time_tuple[0] )
        self.set_mins( time_tuple[1] )
        self.set_secs( time_tuple[2] )
        update_total_time()

    def set_total_time( self, secs ):
        self.hrs = int( ( secs / 3600 ) )
        self.mins = int( ( ( secs % 3600 ) / 60 ) )
        self.secs = int( round( secs % 60 ) )
        self.total_time = secs

    def get_hrs( self ):
        return self.hrs

    def get_mins( self ):
        return self.mins

    def get_secs( self ):
        return self.secs

    def get_time_tuple( self ):
        return ( self.get_hrs(), self.get_mins(), self.get_secs() ) 

    def get_total_time( self ):
        return self.total_time

    def get_time_string( self ):
        return str(self.hrs) + ":" + str(self.mins) + ":" + str(self.secs)

    def tw_to_real_time_str( self, tz_offset ):
        am_pm = "pm" if ( ( self.hrs + tz_offset ) % 24 ) > 11 else "am" 
        hours = ( self.hrs + tz_offset ) % 12
        return str(hours) +":"+ str(self.mins) + ":" + str(self.secs) + am_pm

    def update_total_time( self ):
        self.total_time = ( self.hrs * 3600 ) + ( self.mins * 60 ) + self.secs

    def __sub__( self, other ):
        new_val = self.get_total_time() - other.get_total_time()
        full_day = TW_time(24,00,00)
        date = 0
        while( new_val < 0 ):
            date = date - 1
            new_val = new_val + full_day.get_total_time()
            
        new_time = TW_time()
        new_time.set_total_time( new_val )
        return new_time
