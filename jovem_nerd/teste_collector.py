#%%
from collector import Collector
url = 'https://api.jovemnerd.com.br/wp-json/jovemnerd/v1/nerdcasts/'

teste = Collector(url, 'episodios')

# %%
teste.get_response()
# %%
teste.get_and_save()
# %%
