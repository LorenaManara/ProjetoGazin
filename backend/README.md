<!-- usado para explicar as coisas no git -->

# API de Níveis e Desenvolvedores
Esta é uma API de demonstração criada com o framework FastAPI para gerenciar informações de níveis e desenvolvedores.

## Requisitos
* Python 3.9 ou superior
* FastAPI 0.70.0 ou superior
* SQLAlchemy 1.4.0 ou superior
* uvicorn 0.15.0 ou superior

## Instalação

Para executar esta API localmente, siga os seguintes passos:
#### 1. Clone este repositório em sua máquina local:
```
git clone https://github.com/LorenaManara/ProjetoGazin.git
```

#### 2. Crie um ambiente virtual e instale as dependências:
```
cd backend
python3 -m venv venv
source venv/bin/activate  # no Windows, use "venv\Scripts\activate"
pip install -r requirements.txt
```

#### 3. Execute a aplicação:


```
uvicorn main:app --reload
```

#### 4. Acesse a API em seu navegador ou ferramenta de testes, em http://localhost:8000/docs

## Rotas

### Níveis
* GET /niveis: Retorna todos os níveis cadastrados.
* GET /niveis/{id}: Retorna o nível com o ID especificado.
* POST /niveis: Cria um novo nível.
* PUT /niveis/{id}: Atualiza o nível com o ID especificado.
* DELETE /niveis/{id}: Deleta o nível com o ID especificado.

### Desenvolvedores

* GET /desenvolvedores: Retorna todos os desenvolvedores cadastrados.
* GET /desenvolvedores/{id}: Retorna o desenvolvedor com o ID especificado.
* POST /desenvolvedores: Cria um novo desenvolvedor.
* PUT /desenvolvedores/{id}: Atualiza o desenvolvedor com o ID especificado.
* DELETE /desenvolvedores/{id}: Deleta o desenvolvedor com o ID especificado.

## Exemplos de Uso

### Criação de um novo nível

Para criar um novo nível, faça uma requisição POST para a rota /niveis com o seguinte corpo:

```
{
    "nivel": "Júnior"
}
```

### Criação de um novo desenvolvedor

Para criar um novo desenvolvedor, faça uma requisição POST para a rota /desenvolvedores com o seguinte corpo:

```
{
    "nome": "João",
    "idNivel": 1
    "sexo": "M",
    "dataNascimento": "10/10/2003",
    "idade": 19,
    "hobby": "Jogar"
}
```