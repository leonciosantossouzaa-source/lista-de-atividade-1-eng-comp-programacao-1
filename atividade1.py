# Atividade 1 - Coletar nome do aluno e 3 notas e salvar em notas.txt
import os

# Usa a pasta onde este arquivo está, para achar os .txt
os.chdir(os.path.dirname(os.path.abspath(__file__)))

nome = input("Digite seu nome: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

print("\n--- Dados do aluno ---")
print("Nome do aluno:", nome)
print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Nota 3:", nota3)

