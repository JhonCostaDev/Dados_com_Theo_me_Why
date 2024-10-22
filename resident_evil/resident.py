#%% 
# Importação da biblioteca requests para 
import requests 
from tqdm import tqdm
import pandas as pd
from bs4 import BeautifulSoup 

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
    }

def get_content(url:str)-> str:
    
    response = requests.get(url, headers)
    return response
    

def get_basic_info(soup):
    data = {}
    
    div_content = soup.find("div", class_='td-page-content')
    paragrafo = div_content.find_all('p')[1]
    ems = paragrafo.find_all('em')
    
    for i in ems:
        chave, valor, *_ = i.text.split(':')
        chave = chave.strip(" ")
        data[chave] = valor.strip(" ")
    
    return data

def get_aparicoes(soup):
    lis = soup.find('div', class_='td-page-content').find('h4').find_next().find_all('li')

    aparicoes = [i.text for i in lis]
    return aparicoes 

def get_personagens_info(url):
    resp = get_content(url=url)
    
    if resp.status_code != 200:
        print('Não foi possível obter os dados')
        return {}
    else:
        soup = BeautifulSoup(resp.text)
        data = get_basic_info(soup)
        data['aparicoes'] = get_aparicoes(soup=soup)
        
    return data

def get_links():
    
    url = 'https://www.residentevildatabase.com/personagens/'
    resp = requests.get(url, headers)
    
    soup_personagens = BeautifulSoup(resp.text)

    ancoras = soup_personagens.find('div', class_='td-page-content').find_all('a')

    links = [i ['href'] for i in ancoras]

    return links

def transform_dictionary():
    links = get_links()
    data = []

    for i in tqdm(links):
        #print(i)
        d = get_personagens_info(i)
        d['link'] = i
        nome = i.strip("/").split("/")[-1].replace("-", " ").title()
        d['nome'] = nome
        data.append(d)
        
    print('Operação concluída com sucesso!')

    return data

def save_to_parquet(dictonary: dict)-> object:
    
    df = pd.DataFrame(dictonary)
    df.to_parquet('dados_re.parquet', index=False)
    print('Operação concluída com sucesso!')
# %%

dados = transform_dictionary()

#%%
save_to_parquet(dados)
# =============================================================================================
# %%
new_df = pd.read_parquet('dados_re.parquet')
new_df
# %%
