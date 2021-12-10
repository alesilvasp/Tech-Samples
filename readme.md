## CADASTRO DE USUÁRIOS

### Criação de usuário (_administrador_)

`POST /signup - FORMATO DA REQUISIÇÃO`

```json
{
  "name": "admin",
  "email": "admin@mail.com",
  "is_admin": true,
  "password": "1234"
}
```

Caso dê tudo certo o retorno será:

`POST /signup - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "id": 1,
  "name": "admin",
  "email": "admin@mail.com",
  "is_admin": true
}
```

Obs: o usuário _admin_ será o **super user** criado para o cliente final

### Criação de usuário (_analista_)

`POST /admin/new_analyst - FORMATO DA REQUISIÇÃO`

```json
{
  "name": "analyst",
  "email": "analyst@mail.com",
  "is_admin": false,
  "password": "1234"
}
```

Caso dê tudo certo o retorno será:

`POST /admin/new_analyst - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "id": 1,
  "name": "analyst",
  "email": "analyst@mail.com",
  "is_admin": false
}
```

Caso já exista o email cadastrado, o retorno será:

`POST /admin/new_analyst - FORMATO DA RESPOSTA - STATUS 409`

```json
{
  "Error": "email already registred"
}
```

Obs: Somente o usuário _admin_ poderá criar novos usuários _analistas_, caso o analista tente criar novo usuário, o retorno será:

`POST /admin/new_analyst - FORMATO DA RESPOSTA - STATUS 403`

```json
{
  "Error": "User not allowed"
}
```

## LOGIN

`POST /login - FORMATO DA REQUISIÇÃO`

```json
{
  "email": "alesilvasp@gmail.com",
  "password": "1234"
}
```

Caso dê tudo certo, o retorno será:

`POST /login - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzOTA1NzQ0NiwianRpIjoiMTYyYzFlOTctN2E1Zi00YWYxLWE2MjUtYzQ2MjAxY2E1YTY5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6MSwibmFtZSI6IkFsZXgiLCJlbWFpbCI6ImFsZXNpbHZhc3BAZ21haWwuY29tIiwiaXNfYWRtaW4iOnRydWV9LCJuYmYiOjE2MzkwNTc0NDYsImV4cCI6MTYzOTA1ODM0Nn0.tnZZDuejjh18PNSTSPsZQfbMmykirmByRlTQc3Mrxy4"
}
```

Caso algum valor esteja errado, o retorno será:

`POST /login - FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "Not Found": "Verify email or password"
}
```

### Criação de classes

`POST /classes - FORMATO DA REQUISIÇÃO`

```json
{
  "name": "refrigerante",
  "admin_id": 1
}
```

Caso dê tudo certo o retorno será:

`POST /classes - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "id": 1,
  "name": "refrigerante",
  "types": []
}
```

Caso já exista o classe cadastrada, o retorno será:

`POST /classes - FORMATO DA RESPOSTA - STATUS 409`

```json
{
  "error": "Class already exists"
}
```

Caso o admin_id não exista o retorno será:

`POST /classes - FORMATO DA RESPOSTA - STATUS 422`

```json
{
  "error": "DETAIL:  Key (admin_id)=(2) is not present in table \"users\"."
}
```

Caso o admin_id ou name não seja informada o retorno será:

`POST /classes - FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "error": "Invalid input data keys, avaliable keys: name, admin_id"
}
```

Caso o admin_id nao seja um inteiro ou name não seja uma string o retorno será:

`POST /classes - FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "error": "Invalid input data values, name must be of type string and class_id must be of type int"
}
```

### Visualização de classes

`GET /classes `

Caso dê tudo certo o retorno será:

`GET /classes - FORMATO DA RESPOSTA - STATUS 200`

```json
[
  {
    "id": 1,
    "name": "refrigerante",
    "types": []
  },
  {
    "id": 2,
    "name": "salgadinho",
    "types": []
  }
]
```

### Criação de types

`POST /classes/types - FORMATO DA REQUISIÇÃO`

```json
{
  "name": "fisico-quimico",
  "class_id": 1
}
```

Caso dê tudo certo o retorno será:

`POST /classes/types - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "id": 1,
  "name": "fisico-quimico",
  "parameters": []
}
```

Caso o class_id não exista o retorno será:

`POST /classes/types - FORMATO DA RESPOSTA - STATUS 422`

```json
{
  "error": "DETAIL:  Key (class_id)=(1) is not present in table \"classes\"."
}
```

Caso o class_id ou name não seja informada o retorno será:

`POST /classes/types - FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "error": "Invalid input data keys, avaliable keys: name, class_id"
}
```

Caso o class_id nao seja um inteiro ou name não seja uma string o retorno será:

`POST /classes/types - FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "error": "Invalid input data values, name must be of type string and class_id must be of type int"
}
```

### Atualizar type

`POST /classes/types/id - FORMATO DA REQUISIÇÃO`

```json
{
  "name": "microbiológicos"
}
```

Caso dê tudo certo o retorno será:

`POST /classes/types/id - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "id": 1,
  "name": "microbiologicos",
  "parameters": []
}
```

Caso o name não seja uma string o retorno será:

`POST /classes/types/id - FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "error": "Only the key name must be informed and it must be of type string"
}
```

Caso o type_id não exista o retorno será:

`POST /classes/types/id - FORMATO DA RESPOSTA - STATUS 404`

```json
{
 "error": "Type not found
}
```

## Analysis

### Criação

`POST /analysis - FORMATO DA REQUISIÇÂO`

```json
{
  "batch": "123",
	"made": "01-01-2021",
	"category": "Category",
	"class_id": 1
}
```

Caso dê tudo certo, o retorno será:

`POST /analysis - FORMATO DA RESPOSTA - STATUS 201`

```json
{
  "id": 1,
  "batch": "123",
	"made": "01-01-2021",
	"category": "Category",
  "is_concluded": false,
	"class_id": 1,
  "analyst_id": 1
}
```

Caso chaves inválidas estejam no corpo da requisição, o retorno será:

`POST /analysis - FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "error": "One or more invalid keys were given."
}
```

Caso chaves estejam faltando no corpo da requisição, o retorno será:

`POST /analysis - FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "error": "One or more keys are missing."
}
```

Caso chaves tenham o tipo errado na requisição, o retorno será:

`POST /analysis - FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "error": "One or more keys have the wrong type."
}
```

Caso o id de classe dada não esteja cadastrada no banco de dados, o retorno será:

`POST /analysis - FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "error": "One or more foreign keys were not found."
}
```

Caso o usuário não esteja cadastrado, o retorno será:

`POST /analysis - FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "error": "Analyst with id 1 was not found."
}
```

Caso o usuário seja um administrador, o retorno será:

`POST /analysis - FORMATO DA RESPOSTA - STATUS 401`

```json
{
  "error": "User 1 is not a analyst."
}
```

Caso a análise já esteja cadastrada no banco de dados, o retorno será:

`POST /analysis - FORMATO DA RESPOSTA - STATUS 409`

```json
{
  "error": "Analysis with batch id 123 already exists."
}
```

### Ler todas as análises

Caso de tudo certo, o retorno será:

`GET /analysis - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "concluded_analysis": [
    {
      "id": 1,
      "batch": "123",
	    "made": "01-01-2021",
	    "category": "Category",
      "is_concluded": true,
	    "class_id": 1,
      "analyst_id": 1
    }
  ],
  "pending_analysis": [
    {
      "id": 2,
      "batch": "1234",
	    "made": "01-01-2021",
	    "category": "Category",
      "is_concluded": false,
	    "class_id": 1,
      "analyst_id": 1
    }
  ]
}
```

Caso o usuário não esteja cadastrado, o retorno será:

`GET /analysis - FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "error": "Analyst with id 1 was not found."
}
```

Caso o usuário seja um administrador, o retorno será:

`GET /analysis - FORMATO DA RESPOSTA - STATUS 401`

```json
{
  "error": "User 1 is not a analyst."
}
```

### Ler análise pelo ID

Caso de tudo certo, o retorno será:

`GET /analysis/id - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "id": 1,
  "batch": "123",
	"made": "01-01-2021",
	"category": "Category",
  "is_concluded": false,
	"class_id": 1,
  "analyst_id": 1
}
```

Caso o usuário não esteja cadastrado, o retorno será:

`GET /analysis/id - FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "error": "Analyst with id 1 was not found."
}
```

Caso o usuário seja um administrador, o retorno será:

`GET /analysis/id - FORMATO DA RESPOSTA - STATUS 401`

```json
{
  "error": "User 1 is not a analyst."
}
```

Caso a análise não esteja cadastrada no banco de dados, o retorno será:

`GET /analysis/id - FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "error": "Analysis with id 1 was not found."
}
```

Caso o usuário não seja o responsável pela análise, o retono será:

`GET /analysis/id - FORMATO DA RESPOSTA - STATUS 401`

```json
{
  "error": "Analyst with id 1 has no access to analysis 123"
}
```

### Atualizar análise

`PATCH /analysis/id - FORMATO DA REQUISIÇÃO`

```json
{
	"made": "02-02-2021",
	"category": "Category",
  "is_concluded": true,
	"class_id": 2,
  "analyst_id": 2  
}
```

Caso de tudo certo, a resposta será:

`PATCH /analysis/id - FORMATO DA RESPOSTA - STATUS 200`

```json
{
  "id": 1,
	"made": "02-02-2021",
	"category": "Category",
  "is_concluded": true,
	"class_id": 2,
  "analyst_id": 2
}
```

Caso chaves inválidas estejam no corpo da requisição, o retorno será:

`PATCH /analysis/id - FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "error": "One or more invalid keys were given."
}
```

Caso chaves tenham o tipo errado na requisição, o retorno será:

`PATCH /analysis/id - FORMATO DA RESPOSTA - STATUS 400`

```json
{
  "error": "One or more keys have the wrong type."
}
```

Caso o id de classe dada não esteja cadastrada no banco de dados, o retorno será:

`PATCH /analysis/id - FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "error": "One or more foreign keys were not found."
}
```

Caso o usuário não esteja cadastrado, o retorno será:

`PATCH /analysis/id - FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "error": "Analyst with id 1 was not found."
}
```

Caso o usuário seja um administrador, o retorno será:

`PATCH /analysis/id - FORMATO DA RESPOSTA - STATUS 401`

```json
{
  "error": "User 1 is not a analyst."
}
```

Caso a análise não esteja cadastrada no banco de dados, o retorno será:

`PATCH /analysis/id - FORMATO DA RESPOSTA - STATUS 404`

```json
{
  "error": "Analysis with id 1 was not found."
}
```

Caso o usuário não seja o responsável pela análise, o retono será:

`PATCH /analysis/id - FORMATO DA RESPOSTA - STATUS 401`

```json
{
  "error": "Analyst with id 1 has no access to analysis 123"
}
```