# %% 
import pandas as pd

df = pd.read_csv("Reservatorio.csv", sep=",")
df.head()
# %%

# Convertendo a data para tipo date
df["Data da Medição"] = pd.to_datetime(df["Data da Medição"], format='%d/%m/%Y')
# %%
df.dtypes
df.shape
# %%

# funcao para separar por mes 
def separar_por_mes(df, coluna_data, colunas):
    df = df.copy()
    df[coluna_data] = pd.to_datetime(df[coluna_data])

    return (df.groupby([df[coluna_data].dt.year.rename('Ano'), df[coluna_data].dt.month.rename('mes')]
                      )[colunas]
        .mean()
        .round(0)
        .astype(int)
        .reset_index())

meses = separar_por_mes(df, 'Data da Medição',[
      'Cota (m)',
      'Volume Útil (hm³)',
      'Volume Útil (%)',
      'Afluência (m³/s)',
      'Defluência (m³/s)'
])

## Renomenado as colunas

meses.columns = [
    'Ano',
    'Meses',
    'Cota (m',
    'Volume Útil (hm³)',
    'Volume Útil (%)',
    'Afluência (m³/s)',
    'Defluência (m³'

]






# %%
# %%


# Projeto pegando o ano de 2020 
## Pesquisa em Ano e meses 
Janeiro = meses[(meses['Ano'] == 2020) & (meses['Meses'] == 1)]
Janeiro
# %%
Ano2020 = meses[meses['Ano'] == 2020]
Ano2020
# %%
