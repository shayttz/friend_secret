# 🎄✨ Amigo Oculto da Família 🎅🎁

![O Grinch no Natal](https://cornerstonecounselingpb.com/wp-content/uploads/2020/12/how-the-grinch-stole-christmas.jpg)

> *"O Natal não é um momento nem uma estação, senão um estado de espírito. Valorizar a paz e a generosidade e ter graça é compreender o verdadeiro significado de Natal."*

---

## ❤️ Um Ano de Conexões e Esperança

Mais um ciclo se fecha e o espírito natalino nos convida a olhar para trás com gratidão. Este ano foi marcado não apenas pelos desafios superados, mas pela força do nosso **companheirismo**.

Vimos **novas amizades se firmarem**, laços antigos se fortalecerem e a família — seja de sangue ou de coração — se tornar o nosso porto seguro. Que este Amigo Oculto seja mais do que uma troca de presentes: que seja a celebração da nossa união, da esperança em dias cada vez melhores e da alegria de estarmos juntos.

Vamos celebrar o presente de ter uns aos outros! 🥂✨

---

## 🚀 Como fazer a Mágica Acontecer

Este projeto usa **Python + GitHub Actions** para realizar o sorteio de forma 100% sigilosa e **GitHub Pages** para revelar o amigo oculto de forma interativa.

Siga os passos abaixo para configurar tudo corretamente:

### 📸 Passo 1: As Fotos (`/fotos`)

Para que o rosto do amigo apareça na revelação, você precisa subir as fotos:
1.  Crie uma pasta chamada `fotos` na raiz do projeto.
2.  Adicione a foto de cada participante.
3.  **Regra de Ouro:** O nome do arquivo deve ser o primeiro nome da pessoa, em **minúsculo**, sem acentos e em formato `.jpg`.
    * Exemplo: `maria.jpg`, `joao.jpg`, `guilherme.jpg`.

### 📝 Passo 2: A Lista de Nomes (`sorteio.py`)

Abra o arquivo `sorteio.py` e edite as seguintes linhas no início do código:

```
python
# 1. Coloque seu usuário e nome do repositório
GITHUB_USER = "SeuUsuarioGitHub"
REPO_NAME = "NomeDoSeuRepositorio"

# 2. Atualize a lista de participantes (deve ser igual ao nome das fotos)
participantes = [
    "guilherme",
    "maria",
    "joao",
    "ana"
]
```

🌐 Passo 3: Ativar o Site 
Para o link funcionar, o site precisa estar no ar:

Vá na aba Settings (Configurações) do repositório.

No menu lateral esquerdo, clique em Pages.

Em Build and deployment > Branch, selecione main (ou master) e a pasta / (root).

Clique em Save.

Aguarde uns instantes e o GitHub te dará o link do site.

⚠️ Importante: Copie esse link gerado e verifique se a variável BASE_URL no sorteio.py está montada corretamente.

🎲 Passo 4: Rodar o Sorteio
Agora é a hora da verdade! Ninguém precisa baixar nada.

Vá na aba Actions no topo do repositório.

Na esquerda, clique em Gerar Links Amigo Oculto.

Na direita, clique no botão cinza Run workflow.

O script vai rodar na nuvem do GitHub.

💌 Passo 5: Enviar os Links
Quando o workflow terminar (ficar verde ✅), clique nele.

Clique na etapa Rodar Sorteio para ver os logs (o texto preto).

Lá estarão os links prontos!

Exemplo: 🎁 Para GUILHERME: https://...

Copie o link e envie no WhatsApp de cada um.

⚠️ Aviso de Segurança (Anti-Curiosos)
Organizador: Ao copiar os links, NÃO CLIQUE NELES! Se você clicar, vai descobrir quem a pessoa tirou e estragar a surpresa. Apenas copie e mande.

O Segredo: Os nomes estão codificados na URL para evitar spoilers visuais, mas não é criptografia militar. O objetivo é a diversão e a honestidade! 😉

🎅 Feliz Natal e Bom Sorteio! 🎄
