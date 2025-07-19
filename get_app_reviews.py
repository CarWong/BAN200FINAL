import os
import json
import pandas as pd
from google_play_scraper import Sort, app, reviews_all # pip install google_play_scraper

def default(obj):
    """Default JSON serializer."""
    import datetime
    if isinstance(obj, datetime.datetime):
        if obj.utcoffset() is not None:
            obj = obj - obj.utcoffset()
        return str(obj)
    raise TypeError('Not sure how to serialize %s' % (obj,))

def get_apps_details(apps, output):
    all_apps_details = []
    i = 0
    for app_id in apps:
        i += 1
        try:
            result = app(app_id,
                        lang='en',  # defaults to 'en'
                        country='us'   # defaults to 'us'
                    )
            result = {k: str(v, "utf-8") if isinstance(v, bytes) else v for k, v in result.items()}
            all_apps_details.append(result)
            print(i, "-", app_id)
        except Exception as e:
            print(i, "-", app_id, "--", e)
        
    with open(output, 'w', encoding='utf-8') as fw:
        json.dump(all_apps_details, fw, indent=4)

def get_apps_reviews(apps, output):
    os.makedirs(output, exist_ok = True) 

    i = 0
    for app_id in apps:      
        i += 1  
        print(str(i)+': '+app_id)

        if not os.path.isfile(output+app_id+'.json'):
            result = reviews_all(
                app_id,
                sleep_milliseconds=0, # defaults to 0
                lang='en', # defaults to 'en'
                country='us', # defaults to 'us'
                sort=Sort.NEWEST, # Sorting by date (newest first)
                filter_score_with=None # None means all score
                )
            
            with open(output+app_id+'.json', 'w', encoding='utf8') as file:
                json.dump(result, file, indent=4, default=default)

apps = ['com.rbc.mobile.android',
        'com.cibc.android.mobi',
        'com.td',
        'com.scotiabank.banking',
        'com.bmo.mobile']

#get_apps_details(apps, output='banking_apps_details.json')
get_apps_reviews(apps, output='app_reviews/')