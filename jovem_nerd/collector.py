import requests
import datetime
import json
import time

class Collector:
    
    def __init__(self, url, instance_name):
        self.url = url
        self.instance_name = instance_name
        
    def get_response(self, **kwargs):
    
        response = requests.get(self.url, params=kwargs)
        
        if response.status_code == 200:
            return response
        else:
            return response
        
    def save_parquet(self, data):
        now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')

        df = pd.DataFrame(data)
        df.to_parquet(f'data/{self.instance_name}/parquet/{now}.parquet', index=False) 
        
    def save_json(self, data):
        now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
        with open(f'data/{self.instance_name}/json/{now}.json', 'w') as open_file:
                json.dump(data, open_file, indent=4)
                
    def save_data(self, data, format='json'):
        now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
        
        if format == 'json':
            self.save_json(data)
                
        elif format == 'parquet':
            self.save_parquet(data)     
            
    def get_and_save(self, **kwargs):
        response = self.get_response(**kwargs)
        if response.status_code == 200:
            self.save_data(response.json())
        else: 
            print(f'Request sem sucesso: {response.status_code}')