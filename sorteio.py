import random
import base64

# CONFIGURAÇÃO: Coloque o seu usuário do GitHub aqui para montar o link certo
GITHUB_USER = "shayttz"
REPO_NAME = "friend_secret"
BASE_URL = f"https://{GITHUB_USER}.github.io/{REPO_NAME}/"

# Lista de nomes (devem bater com o nome dos arquivos na pasta fotos/)
participantes = [
    "guilherme",
    "laura"
]

def realizar_sorteio():
    random.shuffle(participantes)
    total = len(participantes)
    
    print("="*50)
    print("🎄 LINKS PARA ENVIAR NO WHATSAPP 🎄")
    print("="*50)
    print("OBS: Copie o link e mande APENAS para a pessoa dona do nome.")
    print("NÃO CLIQUE nos links se não quiser saber o resultado!\n")

    for i in range(total):
        tirador = participantes[i]
        indice_sorteado = (i + 1) % total
        sorteado = participantes[indice_sorteado]

        # Codifica o nome do sorteado em Base64 para "esconder" na URL
        # Ex: "maria" vira "bWFyaWE="
        segredo = base64.b64encode(sorteado.encode('utf-8')).decode('utf-8')
        
        link = f"{BASE_URL}?k={segredo}"
        
        print(f"🎁 Para {tirador.upper()}:")
        print(f"{link}")
        print("-" * 30)

if __name__ == "__main__":
    realizar_sorteio()
