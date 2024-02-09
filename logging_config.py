import logging
import sys

import json
import allure


def configure_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)  # Уровень логирования для консоли
    ch.setFormatter(formatter)

    logger.addHandler(ch)


def deep_set_to_list(obj):
    if isinstance(obj, set):
        return list(obj)
    elif isinstance(obj, list):
        return [deep_set_to_list(e) for e in obj]
    elif isinstance(obj, dict):
        return {k: deep_set_to_list(v) for k, v in obj.items()}
    else:
        return obj


def allure_response_and_payload(response, payload, method):
    """
    Аттачим ответ и данные (payload или params) в Allure отчёт.
    :param response: Ответ от сервера.
    :param payload: payload или params.
    :param method: HTTP метод.
    """

    # Преобразовываем все множества в списки перед сериализацией
    if payload is not None:
        payload = deep_set_to_list(payload)
        formatted_data = json.dumps(payload, indent=4, ensure_ascii=False)
        html_data = f"<pre><code>{formatted_data}</code></pre>"
        allure.attach(html_data, name=f" ➡️ {method} - Data ", attachment_type=allure.attachment_type.HTML)
    else:
        allure.attach("Data is None", name=f"payload - {method}", attachment_type=allure.attachment_type.TEXT)

    try:
        formatted_response = json.dumps(json.loads(response.text), indent=4, ensure_ascii=False)
        html_response = f"<pre><code>{formatted_response}</code></pre>"
    except ValueError:  # Если response.text не является JSON
        html_response = f"<pre>{response.text}</pre>"

    allure.attach(html_response, name=f"⬅️ {method} {response.status_code} -  Response",
                  attachment_type=allure.attachment_type.HTML)
