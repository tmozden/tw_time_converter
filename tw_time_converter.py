import re
def main():
    cmd = ''
    while cmd != 'exit':
        cmd = raw_input("Enter TW time:").strip(" \n").lower()
        the_match = re.match("(\d\d):(\d\d):(\d\d)",cmd)
        if the_match:
            hours = int( the_match.group(1) )
            am_pm = True if ( ( hours + 18 ) % 24 ) > 11 else False 
            am_pm = "pm" if am_pm else "am"
            hours = ( hours + 18 ) % 12
            print str(hours) +":"+ the_match.group(2) + ":" + the_match.group(3) + am_pm
        else:
            if cmd == 'exit':
                continue
            print "Invalid input: Please reformat input correctly (ie. 01:22:00 )"
        


if __name__ == '__main__':
    main()