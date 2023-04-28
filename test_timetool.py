import timetools

# Test if datediff calculates correct and absolute values 
def test_datediff_days():
    assert timetools.datediff_days('2023-04-28', '2023-04-10') == 18
    assert timetools.datediff_days('2023-04-10', '2023-04-28') == 18

def test_timediff():
    assert round(timetools.timediff_no_overnight('10:10:05', '11:30:15'), 4) == 1.3361
    assert round(timetools.timediff_no_overnight('11:30:15', '10:10:05'), 4) == 1.3361

def test_datetimediff():
    assert timetools.datetimediff('2023-04-27 10:00:00', '2023-04-28 12:30:00') == 26.5

def test_datediff_choose_unit():
    assert timetools.datediff_choose_unit('2023-04-10', '2023-04-12', 'day') == 2
    assert round(timetools.datediff_choose_unit('2023-04-10', '2023-08-09', 'month')) == 4
    assert timetools.datediff_choose_unit('2023-04-10', '2025-04-09', 'year') == 2

def test_timediff_choose_untit():
    assert timetools.timediff_choose_unit("10:00:00", "12:30:00", "hour") == 2.5
    assert timetools.timediff_choose_unit("10:00:00", "12:30:00", "minute") == 150
    assert timetools.timediff_choose_unit("10:00:00", "12:30:00", "second") == 9000

def test_datetimediff_choose_unit():
    assert timetools.datetimediff_choose_unit('2023-04-27 10:00:00', '2023-04-28 12:30:00', 'day') == 1.1042
    assert timetools.datetimediff_choose_unit('2023-04-27 10:00:00', '2023-04-28 12:30:00', 'hour') == 26.5
    assert timetools.datetimediff_choose_unit('2023-04-27 10:00:00', '2023-04-28 12:30:00', 'minute') == 1590

def test_finnishWeekdayOrder():
    assert timetools.finnishWeekdayOrder('perjantai') == 'perjantai on viikon 5. päivä'
    assert timetools.finnishWeekdayOrder('mantai') == 'mantai ei ole viikonpäivä, tarkista syötteesi'
    


