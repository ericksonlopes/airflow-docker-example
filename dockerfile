FROM apache/airflow:2.7.1-python3.10

# Defina o locale para pt_BR.utf8
ENV LC_ALL pt_BR.utf8
ENV LANG pt_BR.utf8

# Copie o arquivo Pipfile e Pipfile.lock para o diretório de trabalho
COPY Pipfile /Pipfile
COPY Pipfile.lock /Pipfile.lock

# Instale o pipenv e as dependências do Pipfile
RUN pip install --user --upgrade pip
RUN pip install --upgrade pipenv && pipenv install --system
