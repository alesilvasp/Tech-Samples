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
