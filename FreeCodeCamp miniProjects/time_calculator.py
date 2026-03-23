def add_time(start, duration, day = ''):
    #Splitting time to extract hours minutes AM and PM
    #Getting seprately hours and minutes of added time
    
    start_time_hour = int(start.split(':')[0])
    start_time_minutes = int(start.split(':')[1].split(' ')[0])
    AM_PM = start.split(':')[1].split(' ')[1]

    hours_to_add = int(duration.split(':')[0])
    minutes_to_add = int(duration.split(':')[1])
    
    minutes_added = start_time_minutes + minutes_to_add

    final_hours = start_time_hour
    final_minutes = 0
    days_passed = 0
    #Checking if there is an hour change by added minutes
    if minutes_added >= 60:
        hours_to_add += 1
        minutes_added -= 60
    #Addinf hours to check if there is a change during 12 oclock
    while hours_to_add > 0:
        final_hours += 1
        hours_to_add -= 1
        if final_hours == 12:
            if AM_PM == 'PM':
                days_passed += 1
                AM_PM = 'AM'
            else: 
                AM_PM = 'PM'
        if final_hours == 13:
            final_hours -= 12

    final_minutes = minutes_added
    #zapewnienie zera na poczatku minut i godzin gdy wartosc jest ponizej 10
    #assuring zero befeore minutes and hours when values is below 10
    if final_minutes < 10:
        final_minutes = '0'+str(final_minutes)
        day_text = ''
    if final_hours < 10:
        final_hours = '0'+str(final_hours)
        day_text = ''
    if days_passed == 1:
        day_text = ' (next day)'
    elif days_passed == 0:
        day_text = ''
    else:
        day_text = f' ({days_passed} days later)'
    if day != '':
        week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',  'sunday']
        start_idx = week.index(day.lower()) + 1
        end_day = week.index(day.lower()) + 1 + days_passed
        end_day_idx = end_day % 7
        return f'{final_hours}:{final_minutes} {AM_PM}, {week[end_day_idx -1].capitalize()}{day_text} '
    else:  
        return f'{final_hours}:{final_minutes} {AM_PM}{day_text}'
print(add_time('2:59 AM', '5:50', 'saturDay'))