import pandas as pd 

def carregar_csv_e_filtrar(arquivo_csv, estado):
    # Carregar o arquivo CSV em um DataFrame
    df = pd.read_csv(arquivo_csv)
    
    # verifica e remove celulas vazias
    df = df.dropna()

    # Filtrar as linhas pela coluna 'estado'
    df_filtrado = df[df['estado'] == estado]

    return df_filtrado

# Exemplo de uso

arquivo_csv = './exemplo.csv' # substitua 'dados.csv' plo caminho do seu arquivo csv
estado_filtrado = 'SP' # estado que você quer filtrar
df_filtrado = carregar_csv_e_filtrar(arquivo_csv, estado_filtrado)

print(df_filtrado)