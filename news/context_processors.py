import datetime

from categories.models import Category



def date_context_processor(request):
    current_datetime = datetime.datetime.now()
    return {
        'current_day': current_datetime.day,
        'current_month': current_datetime.month,
        'current_year': current_datetime.year,
        'current_hour': current_datetime.hour,
        'curent_minutes': current_datetime.minute,
        'current_seconds': current_datetime.second,
    }

def is_time(request):
    pass