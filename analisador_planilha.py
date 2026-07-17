# Simulador de Data Annotation: Validação de dados de horários
import csv

def validar_planilha(nome_arquivo):
    print(f"Analisando anomalias no arquivo: {nome_arquivo}")
    linhas_com_erro = 0
    
    try:
        with open(nome_arquivo, 'r') as arquivo:
            leitor = csv.reader(arquivo)
            for numero_linha, linha in enumerate(leitor, start=1):
                for item in linha:
                    if item.strip() == '':
                        print(f"⚠️ Anomalia na linha {numero_linha}: campo vazio!")
                        linhas_com_erro += 1
                        break
        print(f"\n✅ Análise concluída. Total de anomalias: {linhas_com_erro}")
    except FileNotFoundError:
        print("❌ Arquivo não encontrado. Crie um .csv para testar.")

if __name__ == "__main__":
    validar_planilha("dados_teste.csv")
