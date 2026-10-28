# Atividade 2 - Ler notas.txt, calcular a média e separar em 3 arquivos
import os

# Usa a pasta onde este arquivo está, para achar os .txt
os.chdir(os.path.dirname(os.path.abspath(__file__)))

aprovados = open("aprovados.txt", "w", encoding="utf-8")
exame = open("exame.txt", "w", encoding="utf-8")
reprovados = open("reprovados.txt", "w", encoding="utf-8")

arquivo = open("notas.txt", "r", encoding="utf-8")
for linha in arquivo:
    dados = linha.strip().split(";")
    nome = dados[0]
    nota1 = float(dados[1])
    nota2 = float(dados[2])
    nota3 = float(dados[3])
    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
        aprovados.write(f"{nome};{media:.2f};Aprovado\n")
    elif media >= 5:
        exame.write(f"{nome};{media:.2f};Exame\n")
    else:
        reprovados.write(f"{nome};{media:.2f};Reprovado\n")
arquivo.close()

aprovados.close()
exame.close()
reprovados.close()
