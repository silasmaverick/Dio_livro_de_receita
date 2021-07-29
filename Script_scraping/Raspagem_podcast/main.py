'''Script para captura de podcasts da baixada em pauta'''

#%%
from typing import Text
import requests 
from bs4 import BeautifulSoup as bs
import pandas as pd


#%%
url = 'https://g1.globo.com/sp/santos-regiao/podcast/baixada-em-pauta/'

#%%
ret = requests.get(url)
ret

#%%
src = ret.content
src
#%%
soup = bs (src, 'html.parser')
soup

# %%
links = soup.find_all('a')
print(links)

#%% definindo a lista dos nomes
lst_nome = []

#%% definindo a lista dos links
lst_link = []
#%%
for link in links:
    if "Baixada em Pauta" in link.text:
        lst_nome += link
# %%
for link in links:
    if "Baixada em Pauta" in link.text:
        lst_link.append(link.attrs['href']) 
# %%
print(lst_nome)
len(lst_nome)
# %%
print(lst_link)
len(lst_link)

# %% definindo um dataframe para os dados
df = pd.DataFrame(list(zip(lst_nome, lst_link)),
            columns =['Nome', 'Link'])

#%%
df.shape

#%%
df
# %%
df.to_csv('baixada_em_pauta.csv', index=False)
# %%
#pesquisar sobre a rolagem da pagina

