import pandas as pd

def ler_csv(caminho_arquivo, separador=','):
    try:
        print(f"[INFO] Lendo o arquivo: {caminho_arquivo}")
        df = pd.read_csv(caminho_arquivo, sep=separador)
        print("[INFO] Arquivo CSV carregado com sucesso.")
        print(f"[INFO] Colunas encontradas: {df.columns.tolist()}")

        # Nomes das colunas
        col_valor_produto = 'Valor do Produto'
        col_valor_final = 'Valor Final'
        col_tipo_aluno = 'Tipo de Aluno'
        col_tipo_pagamento = 'Tipo de Pagamento'
        col_data_compra = 'Data da Compra'

        # Conversão dos valores
        df[col_valor_produto] = (
            df[col_valor_produto]
            .astype(str)
            .replace(r'[R$\s]', '', regex=True)
            .str.replace(',', '.')
            .astype(float)
        )

        df[col_valor_final] = (
            df[col_valor_final]
            .astype(str)
            .replace(r'[R$\s]', '', regex=True)
            .str.replace(',', '.')
            .astype(float)
        )

        print("[INFO] Colunas de valor convertidas com sucesso.")

        # Filtra linhas com diferença
        df_diferenca = df[df[col_valor_produto] != df[col_valor_final]]
        linhas_com_diferenca = df_diferenca.to_dict(orient='records')
        print(f"[INFO] Encontradas {len(linhas_com_diferenca)} linhas com diferença entre os valores.")

        # Contagem de tipo de aluno
        contagem_aluno = df[col_tipo_aluno].value_counts().to_dict()
        print(f"[INFO] Contagem por Tipo de Aluno: {contagem_aluno}")

        # Contagem de tipo de pagamento
        contagem_pagamento = df[col_tipo_pagamento].value_counts().to_dict()
        print(f"[INFO] Contagem por Tipo de Pagamento: {contagem_pagamento}")

        # Conversão da data e contagem
        df[col_data_compra] = pd.to_datetime(df[col_data_compra], format='%d/%m/%y', errors='coerce')
        # Converte a data
        df[col_data_compra] = pd.to_datetime(df[col_data_compra], format='%d/%m/%y', errors='coerce')

        # Data mais antiga e mais recente
        data_mais_antiga = df[col_data_compra].min().date() if not df[col_data_compra].isnull().all() else None
        data_mais_recente = df[col_data_compra].max().date() if not df[col_data_compra].isnull().all() else None



        return {
            'linhas_com_diferenca': linhas_com_diferenca,
            'contagem_tipo_aluno': contagem_aluno,
            'contagem_tipo_pagamento': contagem_pagamento,
            'data_mais_antiga': data_mais_antiga,
            'data_mais_recente': data_mais_recente
        }

    except FileNotFoundError:
        print(f"[ERRO] Arquivo não encontrado: {caminho_arquivo}")
        return {}
    except Exception as e:
        print(f"[ERRO] Falha ao processar o CSV: {e}")
        return {}
