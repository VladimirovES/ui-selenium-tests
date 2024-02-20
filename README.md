# ui-selenium-tests

Проект предназначен для автоматизации UI тестирования с использованием Selenium. Этот проект позволяет легко интегрировать и запускать тесты в различных средах CI/CD, таких как GitHub Actions и Jenkins.

## Установка зависимостей

Для установки необходимых зависимостей используйте следующую команду:

```bash
pip install -r requirements.txt
```

## Запуск тестов
**1. `GitHub Actions` настроен workflow в директории .github/workflows репозитория:**

* Ручной запуск
* По окончанию экшена из другого репозитория
* При пуше в main ветку
  
После окончания тестов Allure отчет деплоится на [GitHub Page](https://vladimiroves.github.io/ui-selenium-tests/#behaviors)


**2. Запуск тестов в `docker`:**

- Сборка docker образа
```bash
docker build -t ui-selenium-tests .
```

- Запуск контейнера в docker
```bash
docker run --name ui-tests ui-selenium-tests
```
- Пример команды для запуска тестов
```bash
pytest -s -n 3 --headless --alluredir=test_results
```

**3. Для запуска тестов в `Jenkins`, используйте Jenkinsfile с описаным pipeline.**
