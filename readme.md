## CADASTRO DE USUÁRIOS

### Criação de usuário (*administrador*)

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

Obs: o usuário *admin* será o **super user** criado para o cliente final

### Criação de usuário (*analista*)

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

Obs: Somente o usuário *admin* poderá criar novos usuários *analistas*, caso o analista tente criar novo usuário, o retorno será:

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
	"email" : "alesilvasp@gmail.com",
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