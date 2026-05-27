import os
import time

caminho_mesa = os.path.expanduser("~/Desktop")

# Defina aqui os dias
dias_limite = 1
tempo_limite = time.time() - (dias_limite * 24 * 60 * 60)

print("Verificando prints antigos na Mesa...")

for arquivo in os.listdir(caminho_mesa):
    nome_minusculo = arquivo.lower()
    
    if "captura" in nome_minusculo and "tela" in nome_minusculo:
        if nome_minusculo.endswith((".png", ".jpg", ".jpeg")):
            
            caminho_completo = os.path.join(caminho_mesa, arquivo)
            data_criacao = os.path.getctime(caminho_completo)
            
            if data_criacao < tempo_limite:
                print(f"Apagando: {arquivo}")
                os.remove(caminho_completo)
