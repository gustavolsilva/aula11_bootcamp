import pandas as pd

class ETLProcess:
    def __init__(self, fonte_dados):
        self.fonte_dados = fonte_dados

    def extrair_dados(self):
        raise NotImplementedError("Método extrair_dados_deve ser implementado nas classes filhas.", self)
    
    def transformar_dados(self, dados):
        raise NotImplementedError("Método transformar_dados_deve ser implementado nas classes filhas.", self, dados)
    
    def carregar_dados(self, dados_transformados):
        raise NotImplementedError("Método carregar_dados_deve ser implementado nas classes filhas.", self, dados_transformados)
    
    def executar(self):
        dados_extraidos = self.extrair_dados()
        dados_transformados = self.transformar_dados(dados_extraidos)
        self.carregar_dados(dados_transformados)

class ETLCSV(ETLProcess):
    def extrair_dados(self):
        return pd.read_csv(self.fonte_dados)
    
    def transformar_dados(self, dados):
        # Exemplo simples de transformação: converter todas as letras em maúsuculas
        return dados.applymap(lambda x: x.upper() if isinstance(x, str) else x)
    
    def carregar_dados(self, dados_transformados):
        # Aqui você pode implementar a lógica para carregar os dados transformados para onde desejar
        print("Dados transformados:")
        print(dados_transformados)


class ETLExcel(ETLProcess):
    def __init__(self, fonte_dados):
        super().__init__(fonte_dados)

    def extrair_dados(self):
        print("all")
        return super().extrair_dados()
    
    def transformar_dados(self, dados):
        return "dados transformados"

# Exemplo de uso
if __name__ == "__main__":
    fonte_csv = 'dados.csv'
    etl_csv = ETLCSV(fonte_csv)
    etl_csv.executar_etl()