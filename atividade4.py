# Atividade 4 - Ler aprovados.txt e reprovados.txt e mostrar a situação de cada aluno
import os

# Usa a pasta onde este arquivo está, para achar os .txt
os.chdir(os.path.dirname(os.path.abspath(__file__)))

for nome_arquivo in ["aprovados.txt", "reprovados.txt"]:
    arquivo = open(nome_arquivo, "r", encoding="utf-8")
    for linha in arquivo:
        dados = linha.strip().split(";")
        if len(dados) == 4:
            print(f"Aluno: {dados[0]} | Nota do exame: {dados[3]} | Média: {dados[1]} | Situação: {dados[2]}")
        else:
            print(f"Aluno: {dados[0]} | Média: {dados[1]} | Situação: {dados[2]}")
    arquivo.close()
