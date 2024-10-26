#%%
import pandas as pd 
import requests
import datetime
import json
import time

#%%
def get_response(**kwargs):
    
    response = requests.get(url, params=kwargs)
    
    if response.status_code == 200:
        return response
    else:
        return response
    
def save_data(data, format='json'):
    
    now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
    
    if format == 'json':
        with open(f'data/episodios/json/{now}.json', 'w') as open_file:
            json.dump(data, open_file, indent=4)
            
    elif format == 'parquet':
        df = pd.DataFrame(data)
        df.to_parquet(f'data/episodios/parquet/{now}.parquet', index=False)       
# %%


url = 'https://api.jovemnerd.com.br/wp-json/jovemnerd/v1/nerdcasts'

# %%
get_response(url = url, per_page=1000, page=1)
# %%
