# Sistema de Gerenciamento de Estoque — Microserviços com Flask e Docker

Este projeto implementa um **sistema baseado em microserviços** para gerenciar produtos, controlar o estoque e registrar vendas, desenvolvido com **Flask** e orquestrado com **Docker Compose**.

| Tecnologia      | Função                      |
| --------------- | --------------------------- |
| Flask           | Backend em Python           |
| Docker          | Isolamento dos serviços     |
| Docker Compose  | Orquestração dos containers |
| HTML + CSS + JS | Interface web               |
| Jinja2          | Templates Flask             |

---

## Funcionalidades

* Listagem de produtos (catálogo)
* Compra de produtos com integração entre microserviços
* Atualização automática do estoque após a compra
* Registro de vendas no serviço de relatórios
* Interface web estilizada para cada módulo

---

## Como Executar o Projeto

### Pré-requisitos

Certifique-se de ter instalado:

* **Docker** → [https://docs.docker.com/get-docker](https://docs.docker.com/get-docker)
* **Docker Compose** (já incluso nas versões recentes do Docker Desktop)

Verifique as versões instaladas:

```bash
docker --version
docker compose version
```

---

### Construir e iniciar os containers

Dentro da pasta `microservices-demo`, execute:

```bash
docker compose up --build
```

O Docker irá **construir as imagens** e iniciar **3 containers**:

| Serviço        | Porta Local                             | Função                         |
| -------------- | --------------------------------------- | ------------------------------ |
| **Catálogo**   | [localhost:5000](http://localhost:5000) | Interface principal de compras |
| **Estoque**    | [localhost:5001](http://localhost:5001) | Gerenciamento do estoque       |
| **Relatórios** | [localhost:5002](http://localhost:5002) | Exibição de vendas registradas |

Durante a inicialização, você verá logs de cada serviço no terminal.

---

### Atualizar uma imagem após mudança no código

Se você alterar o código de um serviço, reconstrua apenas ele:

```bash
docker compose build nome_do_servico
docker compose up nome_do_servico
```

---

### Encerrar o sistema

Para parar os containers:

* Pressione `CTRL + C` no terminal, ou
* Use o comando:

```bash
docker compose down
```

---

## Licença

Este projeto é livre para uso e aprendizado.
Sinta-se à vontade para estudar, modificar e expandir.
