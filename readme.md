# Tech Samples

<h2>Tabela de Conteúdos</h2>

1. [ Sobre ](#sobre)
2. [ Links Relevantes ](#links)
3. [ O Problema a ser solucionado ](#problema)
4. [ A Solução ](#solucao)
5. [ Tecnologias](#techs)
6. [ Instalação ](#install)
7. [ Desenvolvedores ](#devs)
8. [ termos de uso ](#termos)

<a name="sobre"></a>

## 1. Sobre

O projeto foi desenvolvido no terceiro módulo curso de Desenvolvimento Full Stack da Kenzie Academy Brasil, e colocou em prática tanto nossos conhecimentos técnicos quanto a capacidade de trabalho em equipe dos alunos desenvolvedores. A aplicação é uma API que permite funções como Cadastro e Login com diferentes perfis de usuário, criação de classes de amostra, cadrastro de análises com base nas classes existentes , emissão de laudos e mais.

<a name="links"></a>

## 2. Links Relevantes

- <a name="documentação-api" href="https://documenter.getpostman.com/view/18741402/UVR4PANK" target="_blank">Documentação API</a>

<a name="problema"></a>

## 3. O Problema A Ser Solucionado

Identificamos uma escassez de propostas que visam soluções na automatização dos processos de análise e emissão de laudos com foco em laboratórios industriais e particulares.
Atualmente a emissão de laudos é feita em sua maioria de forma manual através de uma planilha padrão de excel e exportado para PDF gerando os seguintes problemas:

- Grande probabilidade de falha operacional ( falhas de digitação, despadronização da planilha, validação manual dos resultados das análises )
- Probabilidade de indisponibilidade do arquivo padrão parando todo o fluxo de análise ( exclusão acidental da planilha, perda do histórico de análises caso o arquivo seja corrompido )
- Dificuldade em levantamentos a assertividade de indicadores ( quantidade de análises mensais, análises mais solicitadas)
- Planilha centralizada, duas análises não conseguem ser feitas ao mesmo tempo por pessoas diferentes podendo travar o fluxo de análise de um colaborador

<a name="solucao"></a>

## 4. A Solução

Uma API que permite o gerenciamento de todo o fluxo de análise e visa resolver ou mitigar os problemas citados acima focando em disponibilidade de dados, agilidade, confidencialidade e garantia dos resultados.

<a name="techs"></a>

## 5. Tecnologias

- <a name="python" href="https://docs.python.org/3/" target="_blank">Python</a>
- <a name="flask" href="https://flask.palletsprojects.com/en/2.0.x/" target="_blank">Flask</a>
- <a name="flask-m" href="https://flask-migrate.readthedocs.io/en/latest/" target="_blank">Flask Migrate</a>
- <a name="flask=sql" href="https://flask-sqlalchemy.palletsprojects.com/en/2.x/" target="_blank">Flask SQLAlchemy</a>
- <a name="flask-jwt" href="https://flask-jwt-extended.readthedocs.io/en/stable/" target="_blank">Flask-jwt-extended</a>
- <a name="python.env" href="https://pypi.org/project/python-dotenv/" target="_blank">python-dotenv</a>
- <a name="postgreSQL" href="https://www.postgresql.org/docs/" target="_blank">PostgreSQL</a>

<a name="install"></a>

## 6. Instalação e uso

### 6.1 Requisitos:

- Python a partir da versão 3.9.6
- Gerenciador de pacotes <a name="pip" href="https://pip.pypa.io/en/stable/" target="_blank">PIP</a>
- Banco de dados PostgreSQL

### 6.2 Instalação:

6.2.1 - Crie um novo banco chamado klab_database no PostgreSQL

6.2.2 - Após o clone no repositório crie um ambiente virtual na pasta do projeto

`python -m venv venv`

6.2.3 - Para ativar o ambiente virtual utilize:

`source venv/bin/activate`

6.2.4 - Instale as dependências necessárias para o projeto utilizando o PIP:

`pip install -r requirements.txt`

6.2.5 - crie um arquivo na raiz no projeto chamado .env e faça as configurações das variáveis de ambiente abaixo com base no .env.example do projeto

```
FLASK_ENV=development
DATABASE=postgresql://seu_usuario:sua_senha@localhost:5432/klab_database
SECRET_KEY=secret_key
```

6.2.5 - Para rodar o projeto utilize o comando `flask run` no terminal, caso de tudo certo recebera uma mensagem parecida com essa:

```
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 427-052-945
```

<a name="devs"></a>

## 7. Deselvolvedores

- <a name="alex" href="https://www.linkedin.com/in/alesilva-dev/" target="_blank">Alexander Silva</a>
- <a name="eduardo" href="https://www.linkedin.com/in/eduardoparraga/" target="_blank">Eduardo Parraga</a>
- <a name="felipe" href="https://www.linkedin.com/in/felipe-silva-98ads/" target="_blank">Felipe Silva</a>
- <a name="fernando" href="https://www.linkedin.com/in/nandorodrigo/" target="_blank">Fernando Rodrigo</a>
- <a name="lucas" href="https://www.linkedin.com/in/lucas-bravo-rozado-a80b36213/" target="_blank">Lucas Bravo</a>

<a name="termos"></a>

## 8. Termos de uso

Este é um projeto Open Source para fins educacionais e não comerciais, **Tipo de licença** - <a name="mit" href="https://opensource.org/licenses/MIT" target="_blank">MIT</a>
