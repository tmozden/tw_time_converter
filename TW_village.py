import TW_player as PLAYER

class TW_village:

    def __init__( self, coord = ( 500, 500 ), player = PLAYER.TW_player(), vil_type = 'mix' ):
        self.coord = coord
        self.vil_type = vil_type
        self.player = player

    def set_coords( self, coords ):
        self.coord = coords

    def get_coords(self):
        return self.coord

    def get_player( self ):
        return self.player

    def set_player( self, player ):
        self.player = player
