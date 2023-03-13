# Kenzie-Commerce-API

## Tabela de Conteúdos

- [Visão Geral](#1-visão-geral)
- [Diagrama ER](#2-diagrama-er)
- [Início Rápido](#3-início-rápido)
    - [Instalando Dependências](#31-instalando-dependências)
    - [Variáveis de Ambiente](#32-variáveis-de-ambiente)
    - [Migrations](#33-migrations)
    - [Scripts](#34-scripts)
- [Endpoints](#4-endpoints)
- [Desenvolvedores](#5-desenvolvedores)

## 1. Visão Geral

Tecnologias usadas.

- [Python](https://www.python.org/)
- [Django Restframework SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)

A URL base da aplicação: 

---

## 2. Diagrama ER
[ Voltar para o topo ](#tabela-de-conteúdos)

Diagrama ER da API representando as relações entre as tabelas do banco de dados.

<p align="center">
   <img src="https://user-images.githubusercontent.com/106447484/224553388-c3a1935a-087d-466a-b7a0-5d3f25712a6c.png"  width="500" height="500"/>
</p>

---

## 3. Início Rápido
[ Voltar para o topo ](#tabela-de-conteúdos)


### 3.1. Instalando Dependências

Clone o projeto em sua máquina e crie o ambiente virtual usando o comando:

```shell
python -m venv venv
```
Em seguida, instale as dependencias usando o comando: 

```shell
pip install -r requirements.txt
```

### 3.2. Variáveis de Ambiente

Crie um arquivo **.env**, copiando o formato do arquivo **.env.example**

Configure suas variáveis de ambiente com suas credenciais do Postgres e uma nova database.

### 3.3. Migrations

Execute as migrations com o comando:

```
python manage.py migrate
```
---

### 3.4. Scripts

Executar aplicação em ambiente de desenvolvimento:

```
python manage.py runserver
```

## 4. Endpoints

[ Voltar para o topo ](#tabela-de-conteúdos)

### Índice

- [Users](#1-Users)
- [Login](#2-Login)
- [Orders](#3-Orders)
- [Products](#4-Products)
- [ShoppingCart](#5-ShoppingCart)

---

## 1. **Users**
[ Voltar para o topo ](#tabela-de-conteúdos)

### Endpoints

| Método   | Rota       | Descrição                               |
|----------|------------|-----------------------------------------|
| POST     | /users     | Criação de um usuário.                  |
| GET      | /users     | Lista todos os usuários                 |
| GET      | /users/:user_id     | Lista um usuário usando seu ID como parâmetro |
| PATCH    | /users/:user_id     | Editar as informações do usuário usando seu ID como parâmetro   |
| DELETE    | /users/:user_id     | Deletar usuário usando seu ID como parâmetro   

---

### 1.1. **Criação de Usuário**

### `POST/api/users/`

### Exemplo de Request:
```
POST /users
Host: 
Authorization: None
Content-type: application/json
```

### Exemplo de Corpo da Requisição:
```json
{
      "email": "user@gmail.com",
      "password": "userPassword",
      "first_name": "User",
      "last_name": "Newuser",
      "username": "User1234",
      "is_superuser": true,
      "is_saller": false,
      "address": {
        "state": "SP",
        "city": "São Paulo",
        "district": "Jardins",
        "street": "Holanda",
        "zip_code": "12345678",
        "plus_information": ""
	}
}
```
Campos opcionais: plus_infomation, is_saller

### Exemplo de Response:
```
201 Created
```

```json
{
	{
      "id": "92dcd8e3-9fe7-496a-873c-29215fd98720",
      "first_name": "User",
      "last_name": "Newuser",
      "email": "user@gmail.com",
      "username": "User1234",
      "is_superuser": true,
      "is_saller": false,
      "createdAt": "2023-03-08T16:21:03.500714Z",
	    "updatedAt": null,
      "address": {
        "id": "34723b86-f30b-454f-8e6a-18edd044746f",
        "state": "SP",
        "city": "São Paulo",
        "district": "Jardins",
        "street": "Holanda",
        "zip_code": "12345678",
        "plus_information": ""
      },
      "cart_id": "c329ddae-9fad-4f49-85a7-1a56f87e7348"
}
}
```
O campo password não deve ser retornado, os campos is_saller (possui o valor false como default), updatedAt, createdAt e id (do tipo uuid e gerado automaticamente no banco de dados) não são passados na requisição mas devem ser retornados na reposta.
Ao criar um usuário, um carrinho será criado e associado ao usuário automáticamente. 

### Possíveis Erros:
| Código do Erro | Descrição |
|----------------|-----------|
| 400 Bad Request   | user with this email already exists. |
| 400 Bad Request   | A user with that username already exists. |

---

### 1.2. **Listando Usuários**

### `GET/api/users/` 

### Exemplo de Request:
```
GET/users
Host: 
Authorization: None
Content-type: None
```

### Corpo da Requisição:
```json
Vazio
```

### Exemplo de Response:
```
200 OK
```
```json
{
    "count": 5,
    "next": null,
    "previous": null,
    "results": [
        {
           "id": "92dcd8e3-9fe7-496a-873c-29215fd98720",
            "first_name": "User",
            "last_name": "Newuser",
            "email": "user@gmail.com",
            "username": "User1234",
            "is_superuser": true,
            "is_saller": false,
            "createdAt": "2023-03-08T16:21:03.500714Z",
	          "updatedAt": null,
            "address": {
              "id": "34723b86-f30b-454f-8e6a-18edd044746f",
              "state": "SP",
              "city": "São Paulo",
              "district": "Jardins",
              "street": "Holanda",
              "zip_code": "12345678",
              "plus_information": ""
            },
            "cart_id": "c329ddae-9fad-4f49-85a7-1a56f87e7348"
        },
        {
            "id": "1d12a854-0dc3-49f7-8852-623e3a956d55",
            "first_name": "Gan",
            "last_name": "dalf",
            "email": "gandalf@gmail.com",
            "username": "Gandalf14",
            "is_superuser": false,
            "is_saller": false,
            "createdAt": "2023-03-08T16:21:03.500714Z",
	          "updatedAt": null,
            "address": {
                "id": "53aa1fbc-2f09-4fea-a752-73c69bfe1cb6",
                "state": "SP",
                "city": "São Paulo",
                "district": "Jardins",
                "street": "França",
                "zip_code": "12345678",
                "plus_information": ""
            },
            "cart_id": "74b3fec3-b38f-47c8-a566-b8155cb820c9"
        },
    ]
}
```
---

### 1.3. **Listar Usuário por ID**

### `GET/api/users/<user_id>/`

### Exemplo de Request:
```
GET/api/users/92dcd8e3-9fe7-496a-873c-29215fd98720
Host: 
Authorization: None
Content-type: None
```

### Parâmetros da Requisição:
| Parâmetro   | Tipo        | Descrição                             |
|-------------|-------------|---------------------------------------|
| user_id     | string      | Identificador único do usuário (User) |

### Corpo da Requisição:
```json
Vazio
```

### Exemplo de Response:
```
200 OK
```
```json
{
       "id": "92dcd8e3-9fe7-496a-873c-29215fd98720",
       "first_name": "Hanzo",
       "last_name": "Hanzo",
       "email": "hanzo@gmail.com",
       "username": "Hanzo",
       "is_superuser": false,
       "is_saller": false,
       "createdAt": "2023-03-08T16:21:03.500714Z",
	     "updatedAt": null,
       "address": {
         "id": "34723b86-f30b-454f-8e6a-18edd044746f",
         "state": "SP",
         "city": "Campinas",
         "district": "Taquaral",
         "street": "Guerra Junqueira",
         "zip_code": "12345678",
         "plus_information": ""
        },
        "cart_id": "c329ddae-9fad-4f49-85a7-1a56f87e7348"
 }
```

### Possíveis Erros:
| Código do Erro | Descrição |
|----------------|-----------|
| 404 Not Found   | Not found. |

---

### 1.4. **Editar Usuário por ID**

### `PATCH/api/users/<user_id>/`

### Exemplo de Request:
```
PATCH/users/9cda28c9-e540-4b2c-bf0c-c90006d37893
Host: 
Authorization: Bearer token
Content-type: application/json
```

### Parâmetros da Requisição:
| Parâmetro   | Tipo        | Descrição                             |
|-------------|-------------|---------------------------------------|
| user_id     | string      | Identificador único do usuário (User) |

### Corpo da Requisição:
```json
{
    "email": "hanzo15@gmail.com",
    "first_name": "hanzo",
    "last_name": "the cat"
}
```
Todos os campos são opcionais. Campos que não podem ser editados: id, createdAt, UpdatedAt.

### Exemplo de Response:
```
200 OK
```
```json
{
    "id": "5b77936e-f69b-4fdc-a26f-10c5b0b79d66",
    "first_name": "hanzo",
    "last_name": "the cat",
    "email": "hanzo15@gmail.com",
    "username": "Hanzo",
    "is_superuser": true,
    "is_saller": false,
    "createdAt": "2023-03-08T16:21:03.500714Z",
    "updatedAt": "2023-03-12T15:52:41.298754Z",
    "address": {
           "id": "34723b86-f30b-454f-8e6a-18edd044746f",
           "state": "SP",
           "city": "Campinas",
           "district": "Taquaral",
           "street": "Guerra Junqueira",
           "zip_code": "12345678",
           "plus_information": ""
          },
          "cart_id": "c329ddae-9fad-4f49-85a7-1a56f87e7348"
}
```

### Possíveis Erros:
| Código do Erro | Descrição |
|----------------|-----------|
| 401 Unauthorized   | Authentication credentials were not provided |
| 404 Not Found   | User not found. |

---

### 1.5. **Deletar Usuário por ID**

### `DELETE/users/<user_id>` 

### Exemplo de Request:
```
DELETE/api/users/9cda28c9-e540-4b2c-bf0c-c90006d37893
Host: 
Authorization: Bearer token
Content-type: None
```

### Parâmetros da Requisição:
| Parâmetro   | Tipo        | Descrição                             |
|-------------|-------------|---------------------------------------|
| user_id     | string      | Identificador único do usuário (User) |

### Corpo da Requisição:
```json
Vazio
```

### Exemplo de Response:
```
204 No content
```
```json
Vazio
```

### Possíveis Erros:
| Código do Erro | Descrição |
|----------------|-----------|
| 401 Unauthorized   | Authentication credentials were not provided. |
| 404 Not Found   | User not found. |

---

## 2. **Login**
[ Voltar para o topo ](#tabela-de-conteúdos)

### Endpoints

| Método   | Rota       | Descrição                               |
|----------|------------|-----------------------------------------|
| POST     | /login     | Autentica o usuário para ter acesso ao sistema.       |

### `POST/api/login`

### Exemplo de Request:
```
POST/login
Host: 
Authorization: None
Content-type: application/json
```

### Exemplo de Corpo da Requisição:
```json
{
	"email": "user@mail.com",
	"password": "User@1234",
}
```

### Exemplo de Response:
```
200 Ok
```

```json
{
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc0FkbSI6dHJ1ZSwiaWF0IjoxNjczNzg4MzQ5LCJleHAiOjE2NzM4NzQ3NDksInN1YiI6IjhjZTUxYjgxLTU5ODUtNDMzYy05MDg3LTg3MTQ3NmU3NjQyNSJ9.uxrYGh7bRtbNx_Kqk-ec7L3P1J5lBjGsXafQnaN1qzg"
}
```

### Possíveis Erros:
| Código do Erro | Descrição |
|----------------|-----------|
| 401 Unauthorized   | No active account found with the given credentials |

---

## 3. **Products**
[ Voltar para o topo ](#tabela-de-conteúdos)

### Endpoints

| Método   | Rota       | Descrição                               |
|----------|------------|-----------------------------------------|
| POST     | /products/     | Criação de um produto.                  |
| GET      | /products/    | Lista todos os produtos.                 |
| PATCH    | /answers/:product_id/     | Editar as informações de um produto usando seu ID como parâmetro.   |
| DELETE    | /answers/:answer_id/     | Deleta um produto usando seu ID como parâmetro.   

---

### 3.1. **Criação de produto**

### Exemplo de Request:
```
POST/api/products/
Host: 
Authorization: Bearer token
Content-type: application/json
```

### Exemplo de Corpo da Requisição:
```json
{
	"name_product": "TV Plasma",
	"stock": 8,
	"price": 999,	
	"category": {
		"category": "eletrodomesticos"
	},
	"user": "e93fbab0-33af-4434-ac10-d01b06a970e2"
}
```

### Exemplo de Response:
```
201 Created
```

```json
{

	"id": "2559f156-cf82-48e0-b973-ec0e519cd7fe",
	"name_product": "TV Plasma",
	"price": 999.0,
	"stock": 8,
	"is_avaliable": true,
	"category": {
		"id": "04c0b134-e256-4fa5-834a-12610b41e3c1",
		"category": "eletrodomesticos"
	},
	"user": "077ecb07-abcb-4f6a-9afc-98ad924362f8"
}
```


### Possíveis Erros:
| Código do Erro | Descrição |
|----------------|-----------|
| 400 Bad request   |This field is required. (Invalid body) |
| 401 Unauthorized   | Authentication credentials were not provided. |
| 404 Not Found   | User not found.  |

---

### 3.2. **Listando produtos**

### `GET/api/products` 

### Exemplo de Request:
```
GET/answers
Host: 
Authorization: Bearer token
Content-type: None
```

### Corpo da Requisição:
```json
Vazio
```

### Exemplo de Response:
```
200 OK
```
```json
{
	"count": 3,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": "2559f156-cf82-48e0-b973-ec0e519cd7fe",
			"name_product": "TV Plasma",
			"price": 999.0,
			"stock": 8,
			"is_avaliable": true,
			"category": {
				"id": "04c0b134-e256-4fa5-834a-12610b41e3c1",
				"category": "eletrodomesticos"
			},
			"user": "077ecb07-abcb-4f6a-9afc-98ad924362f8"
		},
		{
			"id": "ce3baf4f-060a-4450-9d69-aa93aab1e508",
			"name_product": "Geladeira",
			"price": 3229,
			"stock": 28,
			"is_avaliable": true,
			"category": {
				"id": "04c0b134-e256-4fa5-834a-12610b41e3c1",
				"category": "eletrodomesticos"
			},
			"user": "077ecb07-abcb-4f6a-9afc-98ad924362f8"
		}
	]
}
```

### Possíveis Erros:
| Código do Erro | Descrição |
|----------------|-----------|
| 401 Unauthorized   | Authentication credentials were not provided. |
| 403 Forbiden   | Missing admin authorization. |

---
