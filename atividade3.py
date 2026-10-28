# Atividade 3 - Ler exame.txt, pegar a nota do exame e atualizar os resultados
import os

# Usa a pasta onde este arquivo está, para achar os .txt
os.chdir(os.path.dirname(os.path.abspath(__file__)))

arquivo = open("exame.txt", "r", encoding="utf-8")
for linha in arquivo:
    dados = linha.strip().split(";")
    nome = dados[0]
    media_anterior = float(dados[1])

    nota_exame = float(input(f"Nota do exame de {nome}: "))
    nova_media = (media_anterior + nota_exame) / 2

    if nova_media >= 5:
        aprovados = open("aprovados.txt", "a", encoding="utf-8")
        aprovados.write(f"{nome};{nova_media:.2f};Aprovado após exame;{nota_exame}\n")
        aprovados.close()
    else:
        reprovados = open("reprovados.txt", "a", encoding="utf-8")
        reprovados.write(f"{nome};{nova_media:.2f};Reprovado após exame;{nota_exame}\n")
        reprovados.close()
arquivo.close()
