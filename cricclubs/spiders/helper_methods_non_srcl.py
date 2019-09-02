from helper_methods_common import *


def return_meat(col_number, row):
    if debug: print col_number
    if debug: print row.extract()

    # batsmen name
    if col_number == 0:
        return row.css('td a ::text').extract_first()
    # how batsmen got out
    elif col_number == 1:
        return None
    # place holder
    elif col_number == 2:
        return None
    # runs scored
    elif col_number == 3:
        return row.css('td strong ::text').extract_first()
    # balls faced
    elif col_number == 4:
        return row.css('td ::text').extract_first()
    # sixes hit
    elif col_number == 5:
        return row.css('td ::text').extract_first()
    # fours hit
    elif col_number == 6:
        return row.css('td ::text').extract_first()
    # strike rate
    elif col_number == 7:
        return row.css('td ::text').extract_first()
    else:
        return None


def extract_scorecard(response):
    print "Scraping Match: {}".format(response.request.url)
    tables = response.css('div.tab-content')
    table_rows = tables.css('tr')
    batsmen_record = []
    batsmen_stats = []
    our_innings = None
    seq = 0
    for index, row in enumerate(table_rows):
        # print row
        # iterate through table elements until bazookas score card is found
        our_innings = is_innings_found(row, our_innings)
        if our_innings is None or our_innings is False:
            continue
        if our_innings:
            if debug: print "bazookas innings found"
            batsmen_elem_list = row.css("tr td")
            if len(batsmen_elem_list) == 8:
                for col_number, batsmen_elem in enumerate(batsmen_elem_list):
                    value = return_meat(col_number, batsmen_elem)
                    if value is not None:
                        batsmen_record.append(value)
                batsmen_record.insert(0, position_generator(seq))
                batsmen_stats.append(batsmen_record)
                batsmen_record = []
                seq = seq + 1
    print batsmen_stats
    for item in batsmen_stats:
        yield construct_batsmen_record(item)
