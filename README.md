# 📂 Sistema de Cadastro de Produtos

Este é um projeto web desenvolvido com **Python Flask**, que oferece um sistema CRUD (Create, Read, Update, Delete) para gestão de produtos.

## 📅 Funcionalidades

- Cadastro de produtos
- Listagem de todos os produtos
- Edição de produtos existentes
- Remoção de produtos
- Tratamento de erro 404 com página personalizada

## 📊 Tecnologias Utilizadas

- Python 3
- Flask
- SQLite
- HTML

## 📁 Estrutura do Projeto

```
/
├── app.py                 # Arquivo principal da aplicação Flask
├── database/
│   └── db-produtos.db     # Banco de dados SQLite (criado automaticamente)
├── templates/
│   ├── cadastrar.html     # Formulário para cadastrar produtos
│   ├── editar.html        # Formulário para editar produtos
│   ├── listar.html        # Listagem de produtos
│   └── 404.html           # Página personalizada de erro 404
```

## 🚀 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. (Opcional) Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows
```

3. Instale as dependências:

```bash
pip install flask
```

4. Execute a aplicação:

```bash
python app.py
```

5. Acesse pelo navegador:

[http://localhost:5000/produtos/listar](http://localhost:5000/produtos/listar)

## 📝 Banco de Dados

O banco é criado automaticamente no diretório `database/` ao executar o app pela primeira vez. A tabela `produtos` possui os seguintes campos:

- `idproduto`: inteiro, chave primária
- `descricao`: texto
- `precocompra`: real
- `precovenda`: real
- `datacriacao`: data atual

## 💼 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais informações.

