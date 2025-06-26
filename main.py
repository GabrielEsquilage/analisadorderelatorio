from pathlib import Path
from analisador.leitor_csv import ler_csv

CAMINHO_ARQUIVO = Path(__file__).parent / 'assets' / 'relatorio_convertido.csv'
resultado = ler_csv(CAMINHO_ARQUIVO)

if resultado:
    print(f"\n[RESULTADO] Total de linhas com diferença: {len(resultado['linhas_com_diferenca'])}")
    print(f"\n[Tipo de Aluno] {resultado['contagem_tipo_aluno']}")
    print(f"\n[Tipo de Pagamento] {resultado['contagem_tipo_pagamento']}")
    print(f"\n[Datas de Compra] De {resultado['data_mais_antiga']} até {resultado['data_mais_recente']}")


