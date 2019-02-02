import os
import xml.etree.ElementTree as et
from datetime import *

for root, dirs, files in os.walk("hbaseBugReport"):
    
    max_time = timedelta(-999999999).total_seconds()
    min_time = timedelta(days=999999999, hours=23, minutes=59, seconds=59,
                microseconds=999999).total_seconds()
    times = []
    for name in files:
        tree = et.parse("hbaseBugReport/" + name)
        root = tree.getroot()
        report_type = root.find('channel').find('item').find('type')
        status = root.find('channel').find('item').find('status')
        created = root.find('channel').find('item').find('created')
        resolved = root.find('channel').find('item').find('resolved')
       
        if report_type.text == 'Bug' and (status.text == 'Closed' or status.text == 'Resolved'):
            created_date = datetime.strptime(created.text, '%a, %d %b %Y %H:%M:%S +0000')
            resolved_date = datetime.strptime(resolved.text, '%a, %d %b %Y %H:%M:%S +0000')
            time = resolved_date - created_date

            max_time = max(max_time, time.total_seconds())
            min_time = min(min_time, time.total_seconds())
            times.append(time.total_seconds())        

            print(f'{name} {report_type.text} {status.text} {created_date} {resolved_date} {time}')

    print(f'Max: {str(timedelta(seconds=max_time))}')
    print(f'Min: {str(timedelta(seconds=min_time))}')
    print(f'Average: {str(timedelta(seconds=sum(times) / len(times)))}')


