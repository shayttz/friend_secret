import random
import base64

# ==============================================================================
# CONFIGURAÇÕES GERAIS
# ==============================================================================
# Usuário e repositório fornecidos pelo usuário
GITHUB_USER = "shayttz"
REPO_NAME = "friend_secret"
BASE_URL = f"https://{GITHUB_USER}.github.io/{REPO_NAME}/"

# ==============================================================================
# LISTA DE PARTICIPANTES, TAMANHOS E VERSÕES DE NOME
# ==============================================================================
# ATENÇÃO:
# - 'file': Deve ser minúsculo e sem espaços (para a foto).
# - 'display': Deve ser como o nome aparecerá na tela.
# - 'tamanho': O número do chinelo (ajuste o fictício).
participantes = [
    {"file": "guilherme", "display": "Guilherme", "tamanho": "42/43"},
    {"file": "laura", "display": "Laura", "tamanho": "39"},
    {"file": "thais", "display": "Thais", "tamanho": "37"},
    {"file": "nicolas", "display": "Nicolas", "tamanho": "41"},
    {"file": "paulo", "display": "Paulo", "tamanho": "41"},
    {"file": "rodrigo", "display": "Rodrigo", "tamanho": "41/42"},
    {"file": "juliana", "display": "Juliana", "tamanho": "36"},
    {"file": "marialuiza", "display": "Maria Luiza", "tamanho": "35"}, # Display arrumado!
    {"file": "daniel", "display": "Daniel", "tamanho": "41/42"},
    {"file": "elizete", "display": "Elizete", "tamanho": "36"},
    {"file": "luiz", "display": "Luiz", "tamanho": "41/42"},
    {"file": "ana", "display": "Ana", "tamanho": "39/40"},
    {"file": "henrique", "display": "Henrique", "tamanho": "41/42"},
    {"file": "nil", "display": "Nil", "tamanho": "41/42"},
    {"file": "ellen", "display": "Ellen", "tamanho": "35/36"},
    {"file": "rute", "display": "Rute", "tamanho": "35/36"},
    {"file": "cesar", "display": "Cesar", "tamanho": "41/42"},
    {"file": "mineiro", "display": "Mineiro", "tamanho": "40/41}",
    {"file": "bruna", "display": "Bruna", "tamanho": "37/38"},
    {"file": "alexsander", "display": "Alexsander", "tamanho": "45/46"}
]

# ==============================================================================
# LÓGICA DO SORTEIO
# ==============================================================================
def realizar_sorteio():
    if len(participantes) < 2:
        print("Erro: É preciso pelo menos 2 pessoas para o sorteio!")
        return

    random.shuffle(participantes)
    total = len(participantes)
    
    print("\n" + "="*60)
    print("🎄🩴 LINKS PARA O AMIGO OCULTO DE CHINELOS 🩴🎄")
    print("="*60)
    print("⚠️  OBS: Copie o link e mande APENAS para a pessoa indicada.")
    print("🤫 NÃO CLIQUE nos links dos outros!\n")

    for i in range(total):
        tirador = participantes[i]
        indice_sorteado = (i + 1) % total
        sorteado = participantes[indice_sorteado]

        # O SEGREDO AGORA ENVIA 3 INFORMAÇÕES:
        # 1. Nome do arquivo (file)
        # 2. Nome de exibição (display)
        # 3. Tamanho (tamanho)
        dados_para_esconder = f"{sorteado['file']}|{sorteado['display']}|{sorteado['tamanho']}"

        segredo_codificado = base64.b64encode(dados_para_esconder.encode('utf-8')).decode('utf-8')
        
        link = f"{BASE_URL}?k={segredo_codificado}"
        
        # Usamos o nome de DISPLAY para mostrar no log
        print(f"🎁 Para {tirador['display'].upper()} (Enviar no WhatsApp):")
        print(f"{link}")
        print("-" * 40 + "\n")
    
    print("="*60)
    print("✅ Sorteio finalizado! Verifique se todos têm um link.")
    print("="*60)

if __name__ == "__main__":
    realizar_sorteio()
