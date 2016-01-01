import sys
import re
import TW_village as VILLAGE
import TW_player as PLAYER

class TW_file_input:

    def read_new_data( self, file_name ):
        the_file = open( file_name )
        contents = the_file.read()
        the_file.close()
        results = [] 
        entries = re.findall('\{.*\}', contents.strip(" \n"))
        for an_entry in entries:
            coords = re.search('coords=\((\d\d\d)\|(\d\d\d)\)', an_entry)
            player_name = re.search('player=(\w+)', an_entry)
            results.append( VILLAGE.TW_village( ( int( coords.group(1) ), int( coords.group(2) ) ),  PLAYER.TW_player( player_name.group(1) ) ))

        return results
