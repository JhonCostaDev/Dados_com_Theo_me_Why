#%%
import pandas as pd 
import requests 
'''
 ================= Docs api Tab News =================
Parâmetro	Descrição
{pagina}	O número da página que você deseja acessar.
{porPagina}	O número de conteúdos que devem ser retornados por página.
{estrategia}	Ordem de classificação dos conteúdos, pode ser definida em new, old e relevant.

'''
pagina = 1
porPagina = 100
estrategia = 'old'
url = f'https://www.tabnews.com.br/api/v1/contents?page={pagina}&per_page={porPagina}&strategy={estrategia}'
#url = 'https://tabnews.com.br/api/v1/analytics/root-content-published'
response = requests.get(url=url)
response

# %%


# %%
data = response.json()
df = pd.DataFrame(data)
df
# %%
