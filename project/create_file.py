from datetime import datetime

import loguru
import pytz


def create_file():
    with open(f'data/{datetime.now(tz=pytz.timezone("America/Sao_Paulo"))}.html', 'w'):
        loguru.logger.info(f'Arquivo criado com sucesso')
