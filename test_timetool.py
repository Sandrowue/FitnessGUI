import timetools

# Test if datediff calculates correct and absolute values 
def test_datediff_days():
    assert timetools.datediff_days('2023-04-28', '2023-04-10') == 18
    assert timetools.datediff_days('2023-04-10', '2023-04-28') == 18

def test_timediff():
    assert round(timetools.timediff_no_overnight('10:10:05', '11:30:15'), 4) == 1.3361
    assert round(timetools.timediff_no_overnight('11:30:15', '10:10:05'), 4) == 1.3361

def test_dateTimeDiff():
    assert timetools.dateTimeDiff('2023-04-27 10:00:00', '2023-04-28 12:30:00') == 26.5


