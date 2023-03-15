# Kenzie-Commerce-API

Kenzie commerce é uma api com o objetivo de gerenciar um e-commerce, onde possui as funcionalidades de CRUD de usuários, produtos, pedidos e carrinho.

API DOC: https://kenzie-commerce-api-production.up.railway.app/api/docs/redoc/

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

A URL base da aplicação: https://kenzie-commerce-api-production.up.railway.app

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
- [Products](#3-Products)
- [Orders](#4-Orders)
- [ShoppingCart](#5-ShoppingCart)

---

## 1. **Users**
[ Voltar para o topo ](#tabela-de-conteúdos)

### Endpoints

| Método   | Rota       | Descrição                               |
|----------|------------|-----------------------------------------|
| POST     | /api/users/     | Criação de um usuário.                  |
| GET      | /api/users/     | Lista todos os usuários                 |
| GET      | /api/users/:user_id/     | Lista um usuário usando seu ID como parâmetro |
| PATCH    | /api/users/:user_id/     | Editar as informações do usuário usando seu ID como parâmetro   |
| DELETE    | /api/users/:user_id/     | Deletar usuário usando seu ID como parâmetro   

---

### 1.1. **Criação de Usuário**

### `POST /api/users/`

### Exemplo de Request:
```
POST /api/users
Host: https://kenzie-commerce-api-production.up.railway.app
Authorization: None
Content-type: application/json
```

### Exemplo de Corpo da Requisição:
```json
{
	"email": "mitchell@gmail.com",
	"password": "mimi1234!",
	"first_name": "Mitchell",
	"last_name": "Mimi",
	"username": "Mitchu",
	"is_superuser": false,
	"is_saller": false,
	"address": {
		"state": "SP",
		"city": "Campinas",
		"district": "Taquaral",
		"street": "R. Vasco Fernandes Coutinho",
		"zip_code": "12345678",
		"plus_information": "ao lado do parque"
	}
}
```
Campos opcionais: plus_infomation e is_saller.

### Exemplo de Response:
```
201 Created
```

```json
{
	"id": "42652d8f-c47e-4ea7-8c90-ab3a460b7e01",
	"first_name": "Mitchell",
	"last_name": "Mimi",
	"email": "mitchell@gmail.com",
	"username": "Mitchu",
	"is_superuser": false,
	"is_saller": false,
	"createdAt": "2023-03-14T13:34:29.818991Z",
	"updatedAt": null,
	"address": {
		"id": "2f174250-b861-4cc9-8407-06141498fdcc",
		"state": "SP",
		"city": "Campinas",
		"district": "Taquaral",
		"street": "R. Vasco Fernandes Coutinho",
		"zip_code": "12345678",
		"plus_information": "ao lado do parque"
	},
	"cart_id": "dab23a7d-c264-4352-bec8-97457f91d09e"
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

### `GET /api/users/` 

### Exemplo de Request:
```
GET /api/users
Host: https://kenzie-commerce-api-production.up.railway.app
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
	"count": 8,
	"next": "http://kenzie-commerce-api-production.up.railway.app/api/users/?page=2",
	"previous": null,
	"results": [
		{
			"id": "42652d8f-c47e-4ea7-8c90-ab3a460b7e01",
			"first_name": "Mitchell",
			"last_name": "Mimi",
			"email": "mitchell@gmail.com",
			"username": "Mitchu",
			"is_superuser": false,
			"is_saller": false,
			"createdAt": "2023-03-14T13:34:29.818991Z",
			"updatedAt": null,
			"address": {
				"id": "2f174250-b861-4cc9-8407-06141498fdcc",
				"state": "SP",
				"city": "Campinas",
				"district": "Taquaral",
				"street": "R. Vasco Fernandes Coutinho",
				"zip_code": "12345678",
				"plus_information": "ao lado do parque"
			},
			"cart_id": "dab23a7d-c264-4352-bec8-97457f91d09e"
		},
		{
			"id": "4613b422-aae0-4411-bb4b-d8a0093c0542",
			"first_name": "Flavia",
			"last_name": "Saller",
			"email": "flaviasaller@gmail.com",
			"username": "flaviasaller",
			"is_superuser": false,
			"is_saller": true,
			"createdAt": "2023-03-13T21:01:43.272202Z",
			"updatedAt": null,
			"address": {
				"id": "90aea865-35ef-4aed-a5ad-2437b3c4cf18",
				"state": "SP",
				"city": "São Paulo",
				"district": "Sé",
				"street": "Rua dos Códigos, 337",
				"zip_code": "12345678",
				"plus_information": "Apto 524"
			},
			"cart_id": "dd4e87f4-7b7e-49f1-bfec-7d2fe81425db"
		}
	]
}
```
---

### 1.3. **Listar Usuário por ID**

### `GET /api/users/<user_id>/`

### Exemplo de Request:
```
GET/api/users/42652d8f-c47e-4ea7-8c90-ab3a460b7e01
Host: https://kenzie-commerce-api-production.up.railway.app
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
	"id": "42652d8f-c47e-4ea7-8c90-ab3a460b7e01",
	"first_name": "Mitchell",
	"last_name": "Mimi",
	"email": "mitchell@gmail.com",
	"username": "Mitchu",
	"is_superuser": false,
	"is_saller": false,
	"createdAt": "2023-03-14T13:34:29.818991Z",
	"updatedAt": null,
	"address": {
		"id": "2f174250-b861-4cc9-8407-06141498fdcc",
		"state": "SP",
		"city": "Campinas",
		"district": "Taquaral",
		"street": "R. Vasco Fernandes Coutinho",
		"zip_code": "12345678",
		"plus_information": "ao lado do parque"
	},
	"cart_id": "dab23a7d-c264-4352-bec8-97457f91d09e"
}
```

### Possíveis Erros:
| Código do Erro | Descrição |
|----------------|-----------|
| 404 Not Found   | Not found. |

---

### 1.4. **Editar Usuário por ID**

### `PATCH /api/users/<user_id>/`

### Exemplo de Request:
```
PATCH /api/users/42652d8f-c47e-4ea7-8c90-ab3a460b7e01
Host: https://kenzie-commerce-api-production.up.railway.app
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
	"email": "mitchell1@gmail.com",
	"username": "Mitchu-Mimi"
}
```
Todos os campos são opcionais. Campos que não podem ser editados: id, createdAt, UpdatedAt.

### Exemplo de Response:
```
200 OK
```
```json
{
	"id": "42652d8f-c47e-4ea7-8c90-ab3a460b7e01",
	"first_name": "Mitchell",
	"last_name": "Mimi",
	"email": "mitchell1@gmail.com",
	"username": "Mitchu-Mimi",
	"is_superuser": false,
	"is_saller": false,
	"createdAt": "2023-03-14T13:34:29.818991Z",
	"updatedAt": "2023-03-14T13:44:37.861476Z",
	"address": {
		"id": "2f174250-b861-4cc9-8407-06141498fdcc",
		"state": "SP",
		"city": "Campinas",
		"district": "Taquaral",
		"street": "R. Vasco Fernandes Coutinho",
		"zip_code": "12345678",
		"plus_information": "ao lado do parque"
	},
	"cart_id": "dab23a7d-c264-4352-bec8-97457f91d09e"
}
```

### Possíveis Erros:
| Código do Erro | Descrição |
|----------------|-----------|
| 401 Unauthorized   | Authentication credentials were not provided |
| 404 Not Found   | User not found. |

---

### 1.5. **Deletar Usuário por ID**

### `DELETE api/users/<user_id>` 

### Exemplo de Request:
```
DELETE/api/users/42652d8f-c47e-4ea7-8c90-ab3a460b7e01
Host: https://kenzie-commerce-api-production.up.railway.app
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
Host: https://kenzie-commerce-api-production.up.railway.app
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
	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3OTQwNjI3NiwiaWF0IjoxNjc4ODAxNDc2LCJqdGkiOiIzNzEwZDAwMWIwZTc0YzRiODdkNWEzOGUxZjE5ZGIxMSIsInVzZXJfaWQiOiI2YmFhNmQxYS1iNWNjLTQ2NTktYmJiNy02ODU0ZDVhYTllOTgifQ.inVyGxX46P5VXtOgNv3Tn8zVNDFMmVrdrA_AZwahWTA",
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc4ODU1NDc2LCJpYXQiOjE2Nzg4MDE0NzYsImp0aSI6IjQzODc4ZTMyN2I3NDQ4OTI5YmZkMTI2MzM5ZmZjZjdiIiwidXNlcl9pZCI6IjZiYWE2ZDFhLWI1Y2MtNDY1OS1iYmI3LTY4NTRkNWFhOWU5OCJ9.KHx27AQcEc8s3WleievZ_sWTOKf9kc9aHFwTN1-N3zk"
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
| POST     | /api/products/     | Criação de um produto.                  |
| GET      | /api/products/    | Lista todos os produtos.                 |
| GET      | /api/products/:product_id    | Lista produto por Id.                 |
| PATCH    | /api/product/:product_id/     | Editar as informações de um produto usando seu ID como parâmetro.   |

---

### 3.1. **Criação de produto**

### Exemplo de Request:
```
POST /api/products/
Host: https://kenzie-commerce-api-production.up.railway.app
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

O campo is_available não deve ser passado na requisição, será gerado automaticamente de acordo com a quantidade do estoque do produto.


### Possíveis Erros:
| Código do Erro | Descrição |
|----------------|-----------|
| 400 Bad request   |This field is required. (Invalid body) |
| 401 Unauthorized   | Authentication credentials were not provided. |
| 403 Forbiden   | You do not have permission to perform this action. |
| 404 Not Found   | User not found.  |

---

### 3.2. **Listando produtos**

### `GET /api/products` 

### Exemplo de Request:
```
GET /products
Host: https://kenzie-commerce-api-production.up.railway.app
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
			"id": "f1fc0e0b-d84b-47a9-a86f-fcd899acf643",
			"name_product": "Xbox one",
			"price": 1400.0,
			"stock": 10,
			"is_avaliable": true,
			"category": {
				"id": "7f8c1692-ab46-4eba-a699-e6d03c074032",
				"category": "eletronicos"
			},
			"user": "efde725b-cbe2-45e2-b87a-8db7a6128ca5"
		}
	]
}
```

Os produtos também podem ser pesquisados por parâmtro na requisição:

https://kenzie-commerce-api-production.up.railway.app/api/products/?category=67f132d9-057a-482c-af1c-f22f50eb6439

https://kenzie-commerce-api-production.up.railway.app/api/products/?name_product=Xbox%20One

https://kenzie-commerce-api-production.up.railway.app/api/products/?id=f1fc0e0b-d84b-47a9-a86f-fcd899acf643


### Possíveis Erros:
| Código do Erro | Descrição |
|----------------|-----------|
| 401 Unauthorized   | Authentication credentials were not provided. |

---

### 3.3. **Editar produto por ID** 

### `PATCH /api/products/<product_id>`

### Exemplo de Request:
```
PATCH /api/products/bc9a9325-08e6-4e8a-909b-26345b04eee7
Host: https://kenzie-commerce-api-production.up.railway.app
Authorization: Bearer token
Content-type: application/json
```

### Parâmetros da Requisição:
| Parâmetro   | Tipo        | Descrição                             |
|-------------|-------------|---------------------------------------|
| product_id     | string      | Identificador único do produto (Product) |

### Exemplo de Corpo da Requisição:
```json
{
	"stock": 20,
	"price": 5000
}
```

### Exemplo de Response:
```
200 OK
```

```json
{
	"id": "bc9a9325-08e6-4e8a-909b-26345b04eee7",
	"name_product": "Xbox one",
	"price": 5000.0,
	"stock": 20,
	"is_avaliable": true,
	"category": {
		"id": "7f8c1692-ab46-4eba-a699-e6d03c074032",
		"category": "eletronicos"
	},
	"user": "6baa6d1a-b5cc-4659-bbb7-6854d5aa9e98"
}
```


### Possíveis Erros:
| Código do Erro | Descrição |
|----------------|-----------|
| 401 Unauthorized   | Authentication credentials were not provided. |
| 403 Forbiden   | You do not have permission to perform this action. |
| 404 Not Found   | Not found.  |

---

### 3.4. **Listar produto por ID**

### `GET /api/products/<product_id>/`

### Exemplo de Request:
```
GET /api/products/f1fc0e0b-d84b-47a9-a86f-fcd899acf643
Host: https://kenzie-commerce-api-production.up.railway.app
Authorization: None
Content-type: None
```

### Parâmetros da Requisição:
| Parâmetro   | Tipo        | Descrição                             |
|-------------|-------------|---------------------------------------|
| product_id     | string      | Identificador único do produto (Product) |

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
	"id": "f1fc0e0b-d84b-47a9-a86f-fcd899acf643",
	"name_product": "Xbox one",
	"price": 1400.0,
	"stock": 10,
	"is_avaliable": true,
	"category": {
		"id": "7f8c1692-ab46-4eba-a699-e6d03c074032",
		"category": "eletronicos"
	},
	"user": "efde725b-cbe2-45e2-b87a-8db7a6128ca5"
}
```

### Possíveis Erros:
| Código do Erro | Descrição |
|----------------|-----------|
| 404 Not Found   | Not found. |

---

## 4. **Orders**
[ Voltar para o topo ](#tabela-de-conteúdos)

### Endpoints

| Método   | Rota       | Descrição                               |
|----------|------------|-----------------------------------------|
| POST     | /api/orders/     | Criação de um pedido.                  |
| GET      | /api/orders/user/     | Lista todos os pedidos do usuário logado.  | 
| GET    | /api/orders/product/list/     | Lista todos os produtos de um pedido.  | 
| PATCH    | /api/orders/:order_id/     | Editar as informações de um pedido usando seu ID como parâmetro.  |

---

### 4.1. **Criação de pedido** 

### Exemplo de Request:
```
POST /api/orders
Host: https://kenzie-commerce-api-production.up.railway.app
Authorization: Bearer token
Content-type: application/json
```

### Exemplo de Corpo da Requisição:
```json
Vazio
```

### Exemplo de Response:
```
201 Created
```

```json
{
	"message": "request completed successfully"
}
```

### Possíveis Erros:
| Código do Erro | Descrição |
|----------------|-----------|
| 401 Unauthorized   | Authentication credentials were not provided. |
| 400 Bad Request  |  The product's amount is not avaliable  |

---

### 3.2. **Listando pedidos**

### `GET /api/orders/` 

### Exemplo de Request:
```
GET api/orders/
Host: https://kenzie-commerce-api-production.up.railway.app
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
	"count": 1,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 2,
			"order_status": "Pedido Realizado",
			"ordered_at": "2023-03-14T20:43:59.531849Z",
			"product": "1b97b08e-0dfe-43cb-a23e-5b0236954f79",
			"ordered_by": {
				"id": "42652d8f-c47e-4ea7-8c90-ab3a460b7e01",
				"first_name": "Mitchell",
				"last_name": "Mimi",
				"email": "mitchell@gmail.com",
				"username": "Mitchu",
				"is_superuser": false,
				"is_saller": false,
				"createdAt": "2023-03-14T13:34:29.818991Z",
				"updatedAt": null,
				"address": {
					"id": "2f174250-b861-4cc9-8407-06141498fdcc",
					"state": "SP",
					"city": "Campinas",
					"district": "Taquaral",
					"street": "R. Vasco Fernandes Coutinho",
					"zip_code": "12345678",
					"plus_information": "ao lado do parque"
				},
				"cart_id": "dab23a7d-c264-4352-bec8-97457f91d09e",
				"amount": 1
			}
		}
	]
}
```

### Possíveis Erros:
| Código do Erro | Descrição |
|----------------|-----------|
| 403 Forbiden   | Authentication credentials were not provided |

---

### 3.3. **Listando pedidos do usuário logado**

### `GET /api/products/user/` 

### Exemplo de Request:
```
GET /api/products/user/
Host: https://kenzie-commerce-api-production.up.railway.app
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
	"count": 1,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 2,
			"order_status": "Pedido Realizado",
			"ordered_at": "2023-03-14T20:43:59.531849Z",
			"product": "1b97b08e-0dfe-43cb-a23e-5b0236954f79",
			"ordered_by": {
				"id": "42652d8f-c47e-4ea7-8c90-ab3a460b7e01",
				"first_name": "Mitchell",
				"last_name": "Mimi",
				"email": "mitchell@gmail.com",
				"username": "Mitchu",
				"is_superuser": false,
				"is_saller": false,
				"createdAt": "2023-03-14T13:34:29.818991Z",
				"updatedAt": null,
				"address": {
					"id": "2f174250-b861-4cc9-8407-06141498fdcc",
					"state": "SP",
					"city": "Campinas",
					"district": "Taquaral",
					"street": "R. Vasco Fernandes Coutinho",
					"zip_code": "12345678",
					"plus_information": "ao lado do parque"
				},
				"cart_id": "dab23a7d-c264-4352-bec8-97457f91d09e",
				"amount": 1
			}
		}
	]
}
```

### Possíveis Erros:
| Código do Erro | Descrição |
|----------------|-----------|
| 403 Forbiden   | Authentication credentials were not provided |

---

### 3.4. **Listando todos os pedidos dos pedidos do vendedor logado**

### `GET /api/product/list/` 

### Exemplo de Request:
```
GET /api/product/list/
Host: https://kenzie-commerce-api-production.up.railway.app
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
	{
	"count": 8,
	"next": "http://localhost:8000/api/orders/product/list/?page=2",
	"previous": null,
	"results": [
		{
			"id": 1,
			"order_status": "Pedido Realizado",
			"ordered_at": "2023-03-14T16:47:34.338474Z",
			"product": "dc58e29b-c286-4cb8-aa2f-55569a81e989",
			"ordered_by": {
				"id": "42652d8f-c47e-4ea7-8c90-ab3a460b7e01",
				"first_name": "Mitchell",
				"last_name": "Mimi",
				"email": "mitchell1@gmail.com",
				"username": "Mitchu-Mimi",
				"is_superuser": false,
				"is_saller": false,
				"createdAt": "2023-03-14T13:34:29.818991Z",
				"updatedAt": "2023-03-14T13:44:37.861476Z",
				"address": {
					"id": "2f174250-b861-4cc9-8407-06141498fdcc",
					"state": "SP",
					"city": "Campinas",
					"district": "Taquaral",
					"street": "R. Vasco Fernandes Coutinho",
					"zip_code": "12345678",
					"plus_information": "ao lado do parque"
				},
				"cart_id": "dab23a7d-c264-4352-bec8-97457f91d09e"
			}
		}
	]
}
```

### Possíveis Erros:
| Código do Erro | Descrição |
|----------------|-----------|
| 403 Forbiden   | Authentication credentials were not provided |

---

### 3.3. **Editar pedido por ID** 

### `PATCH /api/orders/:order_id/`

### Exemplo de Request:
```
PATCH /api/orders/32
Host: https://kenzie-commerce-api-production.up.railway.app
Authorization: Bearer token
Content-type: application/json
```

### Parâmetros da Requisição:
| Parâmetro   | Tipo        | Descrição                             |
|-------------|-------------|---------------------------------------|
| order_id     | string      | Identificador único do pedido (Order) |

### Exemplo de Corpo da Requisição:
```json
{
	"order_status": "Entregue"
}
```

### Exemplo de Response:
```
200 OK
```

```json
{
	"id": 32,
	"order_status": "Entregue",
	"ordered_at": "2019-08-24T14:15:22Z",
	"product": "e0588024-d851-42d5-ab9f-1b664ef352d4",
	"ordered_by": {
		"id": "42652d8f-c47e-4ea7-8c90-ab3a460b7e01",
		"first_name": "Mitchell",
		"last_name": "Mimi",
		"email": "mitchell1@gmail.com",
		"username": "Mitchu-Mimi",
		"is_superuser": false,
		"is_saller": false,
		"createdAt": "2023-03-14T13:34:29.818991Z",
		"updatedAt": null,
		"address": {
			"id": "2f174250-b861-4cc9-8407-06141498fdcc",
			"state": "SP",
			"city": "Campinas",
			"district": "Taquaral",
			"street": "R. Vasco Fernandes Coutinho",
			"zip_code": "12345678",
			"plus_information": "ao lado do parque"
	},
	"cart_id": "dab23a7d-c264-4352-bec8-97457f91d09e"
	},
	"amount": 2
}
```


### Possíveis Erros:
| Código do Erro | Descrição |
|----------------|-----------|
| 401 Unauthorized   | Authentication credentials were not provided. |
| 403 Forbiden   | You do not have permission to perform this action. |
| 404 Not Found   | Not found.  |

---


## 5. **Carrinho**
[ Voltar para o topo ](#tabela-de-conteúdos)

### Endpoints

| Método   | Rota       | Descrição                               |
|----------|------------|-----------------------------------------|
| POST     | /api/shopping_cart/:product_id/    | Adição de um produto no carrinho.  |
| GET      | /api/cart/:cart_id/   | Lista todos as perguntas.  |
| PATCH    | /api/shopping_cart_up/:shopping_cart_id/  | Editar a quantidade de um produto no carrinho usando seu ID como parâmetro. |
| DELETE    | /api/cart/:cart_id/  | Deleta todos os produtos de um carrinho. |  

---

### 5.1. **Adicionando produto ao carrinho** 

### Exemplo de Request:
```
POST /api/shopping_cart/7de60fa2-f668-4480-be83-dff06a9f3696/
Host: https://kenzie-commerce-api-production.up.railway.app
Authorization: Bearer token
Content-type: application/json
```

### Exemplo de Corpo da Requisição:
```json
{
	"amount": 2
}
```

### Exemplo de Response:
```
201 Created
```

```json
{
	"id": "56e0d136-e0a3-4abb-9f26-adf2b1d86a48",
	"cart": "dab23a7d-c264-4352-bec8-97457f91d09e",
	"product": "7de60fa2-f668-4480-be83-dff06a9f3696",
	"amount": 2
}
```

### Possíveis Erros:
| Código do Erro | Descrição |
|----------------|-----------|
| 401 Unauthorized   | Authentication credentials were not provided. |
| 400 Bad Request  | The product's amount is not avaliable |
| 403 Forbiden	| You do not have permission to perform this action. |
| 404 Not Found	| Not found. | 


---

### 5.2. **Editando quantidade de produto no carrinho**
### `PATCH /api/shopping_cart_up/:shopping_cart_id`

### Exemplo de Request:
```
PATCH api/shopping_cart_up/56e0d136-e0a3-4abb-9f26-adf2b1d86a48/
Host: https://kenzie-commerce-api-production.up.railway.app
Authorization: Bearer token
Content-type: application/json
```

### Parâmetros da Requisição:
| Parâmetro   | Tipo        | Descrição                             |
|-------------|-------------|---------------------------------------|
| shopping_cart_id     | string      | Identificador único do carrinho (ShoppingCart) |

### Exemplo de Corpo da Requisição:
```json
{
	"amount": 5
}
```

### Exemplo de Response:
```
200 OK
```

```json
{
	"id": "56e0d136-e0a3-4abb-9f26-adf2b1d86a48",
	"cart": "dab23a7d-c264-4352-bec8-97457f91d09e",
	"product": "7de60fa2-f668-4480-be83-dff06a9f3696",
	"amount": 5
}
```

### Possíveis Erros:
| Código do Erro | Descrição |
|----------------|-----------|
| 401 Unauthorized   | Authentication credentials were not provided. |
| 400 Bad Request  | The product's amount is not avaliable |
| 403 Forbiden	| You do not have permission to perform this action. |
| 404 Not Found	| Not found. | 

---

### 5.3. **Listando carrinho**

### `GET /api/cart/:cart_id/` 

### Exemplo de Request:

GET api/cart/dab23a7d-c264-4352-bec8-97457f91d09e/
Host: https://kenzie-commerce-api-production.up.railway.app
Authorization: Bearer token
Content-type: None

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
	"id": "dab23a7d-c264-4352-bec8-97457f91d09e",
	"cart_cart_products": [
		{
			"id": "c2a53eaf-cbbc-4e01-9696-20d9f27c55de",
			"amount": 2,
			"createdAt": "2023-03-14T14:21:13.518116Z",
			"cart": "dab23a7d-c264-4352-bec8-97457f91d09e",
			"product": "e0893e3a-a600-4480-bedb-85a37697c9e4"
		},

	],
	"products": [
		{
			"id": "f1fc0e0b-d84b-47a9-a86f-fcd899acf643",
			"name_product": "Xbox one",
			"price": 1400.0,
			"stock": 10,
			"is_avaliable": true,
			"user": "efde725b-cbe2-45e2-b87a-8db7a6128ca5",
			"category": "7f8c1692-ab46-4eba-a699-e6d03c074032"
		},
		{
			"id": "e0893e3a-a600-4480-bedb-85a37697c9e4",
			"name_product": "Como ficar milionário em 30 anos",
			"price": 5000.0,
			"stock": 0,
			"is_avaliable": false,
			"user": "4613b422-aae0-4411-bb4b-d8a0093c0542",
			"category": "61def0c2-3e64-4f52-8dde-33a3a0e12226"
		},

	]
}
```

### Possíveis Erros:
| Código do Erro | Descrição |
|----------------|-----------|
| 401 Unauthorized   | Authentication credentials were not provided. |
| 403 Forbiden	| You do not have permission to perform this action. |
| 404 Not Found	| Not found. | 

---

### 5.4. **Deletar todos os produtos do carrinho** 

### `DELETE api/cart/:cart_id` 

### Exemplo de Request:
```
DELETE api/cart/dab23a7d-c264-4352-bec8-97457f91d09e
Host: https://kenzie-commerce-api-production.up.railway.app
Authorization: Bearer token
Content-type: None
```

### Parâmetros da Requisição:
| Parâmetro   | Tipo        | Descrição                             |
|-------------|-------------|---------------------------------------|
| cart_id     | string      | Identificador único do carrinho (ShoppingCart) |

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
| 403 Forbiden	| You do not have permission to perform this action. |
| 404 Not Found	| Not found. | 

--- 

## 6. Desenvolvedores
[ Voltar para o topo ](#tabela-de-conteúdos)

[Felipe Nogueira](https://github.com/Flipsy1)

[Flavia Monteiro](https://github.com/FlaviaBMonteiro)

[Leonardo Neves](https://github.com/Leo-neves20)

[Victoria Milan](https://github.com/victoriamilans)




