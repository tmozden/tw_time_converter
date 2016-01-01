import re


class Time_Manager:

    def calc_timezone():
        zone = raw_input("Please enter timezone(ie. eastern) tap enter for central: ").strip(" \n").lower()
        
        if zone == 'eastern':
            return 19
        elif zone == 'central':
            return 18
        elif zone == 'moutian':
            return 17
        elif zone == 'pacific':
            return 16
        elif zone == '':
            return 18
        else:
            print "Your timezone may have been miss spelled or may not be supported at this time please try again or select another"

def main():
    #This is the hours offset from tw 
    time_offset = calc_timezone()

    cmd = ''
    while cmd != 'exit':

        cmd = raw_input("Enter TW time or command:").strip(" \n").lower()
        if cmd == 'change timezone':
            time_offset = calc_timezone()
        else:
            the_match = re.match("(\d\d):(\d\d):(\d\d)",cmd)
            if the_match:
                hours = int( the_match.group(1) )
                am_pm = True if ( ( hours + time_offset ) % 24 ) > 11 else False 
                am_pm = "pm" if am_pm else "am"
                hours = ( hours + time_offset ) % 12
                print str(hours) +":"+ the_match.group(2) + ":" + the_match.group(3) + am_pm
            else:
                if cmd == 'exit':
                    continue
                print "Invalid input: Please reformat input correctly (ie. 01:22:00 )"
        


if __name__ == '__main__':
    main()
