from etsy_py.api import EtsyAPI
from pprint import pprint
import pandas as pd
from json import JSONDecodeError
import pickle
import time


api = EtsyAPI(api_key=j3)

def get_category_json(category):
    offset = 100
    data_list_2 = []
    for i in range(498):
        time.sleep(1)
        print(i)
        r = api.get('listings/active?sort_order=up&category=jewelry/'+str(category)+'&limit=100&offset=' + str(offset))
        print(r.status_code, r.headers['X-RateLimit-Remaining'])
        if r.status_code == 200:
            data = r.json()
            for item in data['results']:
                data_list_2.append(item)
        else:
            print("ERROR Occurred", r.status_code)
        offset += 100
    return data_list_2

cats = ['bracelet', 'earrings', 'necklace', 'anklet', 'brooch', 'ring', 'pendant', 'piercing']

# c = cats[0]
c = cats[7]
ob = {'data':get_category_json(c), 'name':c}

with open(f"{ob['name']}.pkl", 'wb') as f:
    pickle.dump(ob['data'], f)