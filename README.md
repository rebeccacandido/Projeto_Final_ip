# Projeto Final – Introdução à Programação

Este projeto é uma aplicação web desenvolvida como trabalho final da disciplina **Introdução à Programação**, utilizando o microframework **Flask** em Python. A aplicação consiste em um **glossário interativo**, onde o usuário pode adicionar, visualizar e excluir termos e suas definições.

## 📚 Funcionalidades

- 🔍 **Visualizar termos**: Exibe todos os termos cadastrados em uma tabela com numeração, termo e definição.
- ➕ **Adicionar termo**: Formulário para inserir um novo termo e sua definição. Termos duplicados não são permitidos.
- ❌ **Excluir termo**: Cada termo listado possui um botão "Apagar", permitindo sua remoção do glossário com confirmação.
- 💾 **Persistência em arquivo**: Todos os dados são armazenados no arquivo `bd_glossario.csv` com separador `;`.

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Flask**
- **HTML5**
- **Bootstrap (CSS)**
- **CSV (para armazenamento de dados)**

## 📁 Estrutura do Projeto

```
Projeto_Final_ip_cc/
│
├── static/                  # Arquivos CSS (estilo visual)
├── templates/               # Páginas HTML (modelo, glossário, etc.)
│   ├── modelo.html
│   └── glossario.html
│
├── bd_glossario.csv         # Base de dados com os termos
├── app.py                   # Código principal da aplicação Flask
├── README.md                # Este arquivo
└── LICENSE                  # Licença MIT
```

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Uuiskas/Projeto_Final_ip_cc.git
   cd Projeto_Final_ip_cc
   ```

2. Crie um ambiente virtual e instale o Flask:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   pip install flask
   ```

3. Execute o app:
   ```bash
   flask run
   ```

4. Acesse no navegador:  
   `http://127.0.0.1:5000/glossario`

## 📝 Observações

- A aplicação não usa banco de dados SQL, optando por um arquivo `.csv` para manter o projeto simples e didático.
- O projeto é ideal para iniciantes que desejam aprender Flask e manipulação de arquivos em Python.

## 📄 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais detalhes.
