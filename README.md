# Airflow Docker

# Documentação do Script de Configuração e Inicialização do Apache Airflow com Docker Compose

Este documento fornece um passo a passo para configurar e iniciar o Apache Airflow com Docker Compose usando o
script `setup_script_start.sh`, que está disponível no GitHub
em [https://github.com/ericksonlopes/airflow-docker-example](https://github.com/ericksonlopes/airflow-docker-example). O
script é um arquivo de shell (`.sh`) e é projetado para ser executado em sistemas Linux. Se você estiver usando Windows,
será necessário o Windows Subsystem for Linux (WSL) para executá-lo. O script realiza as seguintes tarefas:

## Uso do Script

Siga estas etapas para configurar e iniciar o Apache Airflow usando o repositório do GitHub:

1. **Clone o Repositório**:

   Abra um terminal no seu sistema Linux ou no Windows Subsystem for Linux (WSL) e execute o seguinte comando para
   clonar o repositório do GitHub para o seu sistema:

   ```bash
   git clone https://github.com/ericksonlopes/airflow-docker-example.git
   ```

   Isso criará uma cópia do repositório no diretório atual.

2. **Acesse o Diretório do Projeto**:

   Entre no diretório do projeto clonado usando o seguinte comando:

   ```bash
   cd airflow-docker-example
   ```

3. **Permissões de Execução**:

   Certifique-se de que o script `setup_script_start.sh` tenha permissões de execução. Você pode conceder permissões de
   execução com o seguinte comando:

   ```bash
   chmod +x setup_script_start.sh
   ```

4. **Execute o Script**:

   Execute o script `setup_script_start.sh` com o seguinte comando:

   ```bash
   ./setup_script_start.sh
   ```

   Isso iniciará o processo de configuração e inicialização do Apache Airflow no seu sistema Linux ou no WSL em sistemas
   Windows.

## Passos do Script

Aqui estão as etapas detalhadas realizadas pelo script `setup_script_start.sh`:

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

   Este comando cria uma imagem Docker do Apache Airflow com base no Dockerfile local. A imagem é marcada
   como `extending_airflow:latest`.

5. **Execução do Docker Compose**:

   ```bash
   docker compose up -d --build
   ```

   Este comando inicia a instância do Apache Airflow em um contêiner Docker. A opção `-d` significa "em segundo plano".
   A opção `--build` garante que a imagem Docker seja reconstruída, se necessário.

   O Apache Airflow será executado com base nas configurações especificadas no arquivo `docker-compose.yml` no diretório
   atual.

Certifique-se de personalizar o script e os diretórios de acordo com suas necessidades específicas antes de executá-lo.
Este documento fornece uma visão geral do que o script faz e como ele funciona, tornando mais fácil configurar e iniciar
o Apache Airflow usando Docker Compose a partir do repositório GitHub. Lembre-se de que o script é destinado a sistemas
Linux e requer o Windows Subsystem for Linux (WSL) para ser executado em sistemas Windows.