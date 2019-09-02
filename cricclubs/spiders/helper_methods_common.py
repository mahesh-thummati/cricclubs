def position_generator(seq):
    if seq == 0 or seq == 1:
        return 0
    if seq >= 2:
        return seq - 1


def construct_batsmen_record(item):
    if debug: print item
    if len(item) == 7:
        batsmen_dict = {
            "0_position": item[0],
            "1_batsmen": item[1],
            "2_runs_scored": item[2],
            "3_balls_faced": item[3],
            "4_fours": item[4],
            "5_sixes": item[5]
        }
        return batsmen_dict
    else:
        print item


def is_innings_found(row, default_value):
    try:
        table_header = row.css('th ::text').extract_first()
        if debug: print table_header
        if 'bowling' in table_header.lower():
            return None
        if 'innings' in table_header.lower():
            if str(team) in table_header:
                return True
            else:
                return False
        else:
            return default_value
    except:
        return default_value


team = "Bazookas"
debug = False
