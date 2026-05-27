import os
import time

# Onde o robô vai olhar (Sua Mesa)
caminho_mesa = os.path.expanduser("~/Desktop")

# Calculando 3 dias atrás
segundos_em_3_dias = 3 * 24 * 60 * 60
tempo_limite = time.time() - segundos_em_3_dias

print("Verificando prints antigos na Mesa...")

# Olhando arquivo por arquivo
for arquivo in os.listdir(caminho_mesa):
    
    # Só mexe se for print (.png) e começar com "Captura de Tela"
    if arquivo.startswith("Captura de Tela") and arquivo.endswith(".png"):
        
        caminho_completo = os.path.join(caminho_mesa, arquivo)
        data_criacao = os.path.getctime(caminho_completo)
        
        # Se for mais velho que 3 dias
        if data_criacao < tempo_limite:
            print(f"Vou apagar: {arquivo}")
            # os.remove(caminho_completo) # <--- REMOVEREI O '#' DEPOIS DO TESTE
            