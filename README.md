# E2E Тестирование с Playwright

Репозиторий использует библиотеки **Playwright** and **pytest**, готовые к запуску в Докер-контейнере.

## Требования к запуску

- [Docker](https://www.docker.com/get-started) установлен в системе.

---

## Собрать Docker Image

```bash
docker build -t e2e:tests .
```

## Запустить тесты

```bash
docker run -it --name test e2e:tests
```