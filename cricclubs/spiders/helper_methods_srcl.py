from helper_methods_common import *


def return_meat_old(col_number, row):
    if col_number == 0:
        if 'innings' in row.extract():
            return row.css('th ::text').extract_first()
        return row.css('a ::text').extract_first()
    elif col_number == 1:
        return None
    elif col_number == 2:
        return row.css('th ::text').extract_first()
    elif col_number == 3:
        return row.css('th ::text').extract_first()
    elif col_number == 4:
        return row.css('th ::text').extract_first()
    elif col_number == 5:
        return row.css('th ::text').extract_first()
    elif col_number == 6:
        return row.css('th ::text').extract_first()
    else:
        return None


def return_meat(col_number, row):
    if debug: print col_number
    if debug: print row.extract()

    # batsmen name
    if col_number == 0:
        return row.css('th a ::text').extract_first()
    # how batsmen got out
    elif col_number == 1:
        return None
    # runs scored
    elif col_number == 2:
        return row.css('th ::text').extract_first()
    # balls faced
    elif col_number == 3:
        return row.css('th ::text').extract_first()
    # fours hit
    elif col_number == 4:
        return row.css('th ::text').extract_first()
    # sixes hit
    elif col_number == 5:
        return row.css('th ::text').extract_first()
    # strike rate
    elif col_number == 6:
        return row.css('th ::text').extract_first()
    else:
        return None


def extract_scorecard(response):
    print "Scraping Match: {}".format(response.request.url)
    tables = response.css('div.match-table-innings')
    table_rows = tables.css('tr')
    batsmen_record = []
    batsmen_stats = []
    our_innings = None
    seq = 0
    skip_header = True
    for index, row in enumerate(table_rows):
        # print row
        # iterate through table elements until bazookas score card is found
        our_innings = is_innings_found(row, our_innings)
        if our_innings is None or our_innings is False:
            continue
        if our_innings:
            if debug: print "bazookas innings found"
            if skip_header:
                skip_header = False
                continue
            batsmen_elem_list = row.css("tr th")
            if len(batsmen_elem_list) == 7:
                for col_number, batsmen_elem in enumerate(batsmen_elem_list):
                    value = return_meat(col_number, batsmen_elem)
                    if value is not None:
                        batsmen_record.append(value)
                if len(batsmen_record) == 6:
                    batsmen_record.insert(0, position_generator(seq))
                    batsmen_stats.append(batsmen_record)
                    batsmen_record = []
                    seq = seq + 1
    print batsmen_stats
    for item in batsmen_stats:
        yield construct_batsmen_record(item)


def extract_scorecard_old(response):
    print "Scraping Match: {}".format(response.request.url)
    tables = response.css('div.match-table-innings')
    rows = tables.css('tr th')
    batsmen_record = []
    batsmen_stats = []
    our_innings = None
    seq = 0
    for index, row in enumerate(rows):
        if debug: print row
        # keep iterating until required team's innings is found
        our_innings = is_innings_found(row, our_innings)
        if our_innings is None or our_innings is False:
            continue
        if our_innings:
            col_number = index % 7
            if col_number == 0 and len(batsmen_record) == 6:
                # Ignore the record with innings in it
                if "innings" in batsmen_record[0]:
                    if debug: print "skipping header record"
                    batsmen_record = []
                else:
                    batsmen_record.insert(0, position_generator(seq))
                    batsmen_stats.append(batsmen_record)
                    batsmen_record = []
                    seq = seq + 1

            value = return_meat(col_number, row)
            if value is not None:
                batsmen_record.append(value)
    print batsmen_stats
    for item in batsmen_stats:
        yield construct_batsmen_record(item)

