#%%
import pandas as pd 
import requests
import datetime
import json
import time

# %%
def get_response(**kwargs):
    
    response = requests.get(url, params=kwargs)
    
    if response.status_code == 200:
        return response
    else:
        return response

def save_data(data, option='json'):
    
    now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
    
    if option == 'json':
        with open(f'data/contents/json/{now}.json', 'w') as open_file:
            json.dump(data, open_file, indent=4)
            
    elif option == 'dataframe':
        df = pd.DataFrame(data)
        df.to_parquet(f'data/contents/parquet/{now}.parquet', index=False)       
# %%


page = 1
while True:
    print(page)
    url = 'https://www.tabnews.com.br/api/v1/contents'
    resp = get_response(url=url,page=page, per_page=100, strategy='new')
    
    if resp.status_code == 200:
        data = resp.json()
        save_data(data)
        if len(data) < 1:
            break
        page += 1
        time.sleep(1)
    elif resp.status_code == 429:
        print('Too Many Requests Error')
        break
    else:
        time.sleep(30)
#%%



