# TOOLS FOR DATE AND TIME CALCULATIONS

# Libararies and modules

import datetime # Python's internal date-time library

def datediff_days(d1, d2):
    """Calculates the difference between two dates in days

    Args:
        d1 (str): A date in ISO format YYYY-MM-DD
        d2 (str): A date in ISO format YYYY-MM-DD

    Returns:
        int: absolute difference in days
    """
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    difference = abs((d2 - d1).days)
    return difference

def datediff_choose_unit(d1, d2, unit):
    """Returns difference between 2 dates in chosen unit (day, month or year)

    Args:
        d1 (str): 1 st date in ISO format (YYYY-mm-dd)
        d2 (str): 2 nd date in ISO format (YYYY-mm-dd)
        unit (str): unit to return

    Returns:
        float: difference between dates in desired units
    """
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    difference = abs((d2 - d1).days) # Timedelta in days
    units = {'day': 1, 'year': 365, 'month': 30} # Dictionary for unid dividers
    divider = units[unit] # Choose by unit argument
    value = difference / divider
    return value

def datetimediff(start, end):
    """Returns difference in hours between two moments

    Args:
        start (str): date time value in format YYYY-MM-dd hh:mm:ss
        end (str): date time value in format YYYY-MM-dd hh:mm:ss

    Returns:
        float: difference in hours
    """
    v1 = datetime.datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
    v2 = datetime.datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
    difference = v2 - v1
    seconds = difference.total_seconds()
    hours = seconds / 3600
    return hours

def datetimediff_choose_unit(date_start, date_end, unit):
    """Calculates difference between date time values in choosen unit(day, hour, minute or second)

    Args:
        date_start (str): date time value in format YYYY-MM-dd hh:mm:ss
        date_end (str): date time value in format YYYY-MM-dd hh:mm:ss
        unit (str): name of time unit: day, hour, minute, second

    Returns:
        float: difference in given units
    """
    v1 = datetime.datetime.strptime(date_start, "%Y-%m-%d %H:%M:%S")
    v2 = datetime.datetime.strptime(date_end, "%Y-%m-%d %H:%M:%S")
    difference = v2 - v1
    units = {'day':86400, 'hour': 3600, 'minute': 60, 'second': 1}
    divider = units[unit]
    seconds = difference.total_seconds()
    value = round(seconds / divider, 4)
    return value
    
def timediff(t1, t2):
    """Calculates the difference between time values in hours

    Args:
        t1 (str): time value in format hh:mm:ss
        t2 (str): time value in format hh:mm:ss

    Returns:
        float: time difference in hours
    """
    # Fucnction calculates a timedelta which supports only seconds or microseconds
    t1 = datetime.datetime.strptime(t1, "%H:%M:%S")
    t2 = datetime.datetime.strptime(t2, "%H:%M:%S")
    seconds = abs((t2 - t1).seconds)
    hours = seconds / 3600 # minute = 60 seconds, hour 60 minutes
    return hours

def timediff_no_overnight(t1, t2):
    """Calculates the difference between time values in hours

    Args:
        t1 (str): time value in format hh:mm:ss
        t2 (str): time value in format hh:mm:ss

    Returns:
        float: time difference in hours
    """
    # Fucnction calculates a timedelta which supports only seconds or microseconds
    t1 = datetime.datetime.strptime(t1, "%H:%M:%S")
    t2 = datetime.datetime.strptime(t2, "%H:%M:%S")

    if t2 > t1:
        seconds = abs((t2 - t1).seconds)
       
    else:
        seconds = abs((t1 - t2).seconds)

    hours = seconds / 3600 # minute = 60 seconds, hour 60 minutes
    return hours

def timediff_choose_unit(t1, t2, unit):
    """Calculates difference between two time values (day, minute or second)

    Args:
        ti (str): time value in format hh:mm:ss
        t2 (str): time value in format hh:mm:ss
        unit (str): unit to return

    Returns:
        float: time difference in chosen units
    """
    t1 = datetime.datetime.strptime(t1, "%H:%M:%S")
    t2 = datetime.datetime.strptime(t2, "%H:%M:%S")
    units = {'hour': 3600, 'minute': 60, 'second': 1}
    seconds = abs((t2 - t1).seconds)
    divider = units[unit]
    value = seconds / divider
    return value

def finnishWeekdayOrder(weekday):
    weekdayNumber = {'maanantain': 1, 'tiistai': 2, 'keskiviikko': 3, 'torstai': 4, 'perjantai': 5, 'lauantai': 6, 'sunnuntai': 7}
    try:
        value = f'{weekday} on viikon {weekdayNumber[weekday]}. päivä'
    except Exception as error:
        value = f'{weekday} ei ole viikonpäivä, tarkista syötteesi'
    return value
    
if __name__ == "__main__":
    # Let's test date difference
    #date1 = '2023-03-21'
    #date2 = '2023-03-17'

    #ero = datediff_choose_unit(date1, date2,'day')
    #print('ero oli', ero ,'päivää')

    # Let's test time difference
    #time1 = '10:00:00'
    #time2 = '15:25:00'
    #ero = timediff_choose_unit(time1, time2, 'minute')
    #print('ero oli', ero, 'minuuttia')

    #print(round(timediff('10:10:05', '11:30:15'), 4))

    #print(dateTimeDiff('2023-04-28 10:00:00', '2023-04-29 11:00:00'), 'tuntia')
    print(datetimediff_choose_unit('2023-04-27 10:00:00', '2023-04-28 12:30:00', 'day'))
    #print(datediff_choose_unit('2023-04-10', '2023-06-12', 'day'))
    print(finnishWeekdayOrder('torstai'))