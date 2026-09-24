# Poke-with-Text

Este pequeno projeto é parte do meu estudo recente sobre classes, herança e organização de código em Python,
junto com um menu simples em texto para interação no terminal.

🟦 Pokémon Terminal RPG
Um RPG de Pokémon feito em Python, rodando no terminal.
O jogador explora o mundo, captura Pokémon, batalha contra inimigos, ganha dinheiro e salva seu progresso.

🎮 Recursos Principais
Batalhas em turno com ataques exclusivos por tipo

Exploração com chance de encontrar Pokémon selvagens

Sistema de captura

Inimigos gerados aleatoriamente

Recompensas em dinheiro por vitória

Save/load usando pickle

Escolha de Pokémon inicial

Menu interativo no terminal

🧩 Estrutura do Projeto
Código
📁 pokemon-terminal-rpg/
│
├── pokemon.py      # Classes de Pokémon e ataques
├── pessoa.py       # Player, Inimigo e lógica de batalha
├── main.py         # Arquivo principal do jogo
├── database.db     # Save do jogador (gerado automaticamente)
└── README.md
⚔️ Sistema de Batalha
Combate baseado em turnos

Dano calculado pelo nível + fator aleatório

Vitória concede dinheiro

Derrota encerra o combate

🌎 Exploração
Chance de encontrar Pokémon selvagem

Jogador decide se tenta capturar

Captura com chance de sucesso

💾 Salvar Progresso
O jogo salva automaticamente:

Time do jogador

Dinheiro

Pokémons capturados

Arquivo: database.db

▶️ Como Executar
bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
python main.py
🛠️ Tecnologias
Python 3

Programação Orientada a Objetos

random

pickle

🚀 Possíveis Melhorias
Sistema de cura

Itens e loja

Evolução de Pokémon

Balanceamento de níveis

Interface gráfica (Tkinter/Pygame)

👤 Autor
Cauã Rodrigues  
Estudante de Cybersecurity e desenvolvedor Python.
