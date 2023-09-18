# Airflow Docker

Este documento fornece uma descrição passo a passo do script usado para instalar o Apache Airflow usando o Docker
Compose. O script realiza as seguintes tarefas:

## Pré-requisitos

- Este script presume que você possui um ambiente Linux com o `apt-get` instalado.
- Você deve ter permissões de administrador (ou usar `sudo`) para executar as etapas que exigem privilégios de
  superusuário.
- Caso o Docker Compose não esteja instalado em seu sistema, você pode instalá-lo executando o seguinte comando:

   ```bash
   apt-get install docker-compose
   ```

## Passos

1. **Atualização de Repositórios**:

   ```bash
   apt-get update -y
   ```

   Este comando atualiza a lista de pacotes disponíveis no sistema operacional.

2. **Criação de Diretórios**:

   ```bash
   mkdir -p ./dags ./logs ./plugins ./config ./data
   ```

   Este comando cria diretórios para armazenar diferentes componentes e configurações do Apache Airflow.

    - `./dags`: Usado para armazenar as definições das tarefas do fluxo de trabalho.
    - `./logs`: Onde os logs do Airflow serão armazenados.
    - `./plugins`: Para plugins personalizados.
    - `./config`: Para arquivos de configuração personalizados.
    - `./data`: Para armazenamento de dados temporários ou persistentes.

3. **Definição da Variável de Ambiente AIRFLOW_UID**:

   ```bash
   echo -e "AIRFLOW_UID=$(id -u)" > .env
   ```

   Isso define a variável de ambiente `AIRFLOW_UID` com o ID de usuário atual. Essa variável é usada posteriormente pelo
   Docker Compose.

4. **Construção da Imagem Docker**:

   ```bash
   docker build . --tag extending_airflow:latest
   ```

   Esse comando cria uma imagem Docker do Apache Airflow com base no Dockerfile local. A imagem é marcada
   como `extending_airflow:latest`.

5. **Execução do Docker Compose**:

   ```bash
   docker compose up -d --build
   ```

   Este comando inicia a instância do Apache Airflow em um contêiner Docker. A opção `-d` significa "em segundo plano".
   A opção `--build` garante que a imagem Docker seja reconstruída, se necessário.

   O Apache Airflow será executado com base nas configurações especificadas no arquivo `docker-compose.yml` no diretório
   atual.

## Notas Adicionais

- Antes de executar o script, é importante garantir que o Docker e o Docker Compose estejam instalados no sistema.
- Certifique-se de que o usuário que está executando o script tenha permissões para usar o Docker sem usar `sudo`. Isso
  pode exigir adicionar o usuário ao grupo `docker`.
- Este script instala uma versão específica do Docker Compose (2.21.0). Caso o Docker Compose não esteja instalado, você
  pode instalá-lo conforme mencionado nos pré-requisitos.

Lembre-se de personalizar o script e os diretórios de acordo com seus requisitos específicos antes de executá-lo. Este
documento fornece uma visão geral do que o script faz e como ele funciona.