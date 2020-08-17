# Cкилл «Эхо»

Скилл доступен по Webhook URL: https://ugl18yk86a.execute-api.us-east-1.amazonaws.com/production/webhook

Повторяет сообщение пользователя: `response.text` и `response.tts` равны полю `request.original_utterance` запроса.

Подробнее о создании скилов для Маруси можно узнать тут: [https://vk.com/dev/marusia_skill_docs](https://vk.com/dev/marusia_skill_docs)

## Деплой на AWS Lambda

1. [Установить Serverless Framework](https://www.serverless.com/framework/docs/providers/aws/guide/installation/) и [настроить AWS Credentials](https://www.serverless.com/framework/docs/providers/aws/guide/credentials/)
2. Выполнить `npm run deploy` в директории проекта. Присвоенный Webhook URL будет выведен в терминал в разделе `endpoints`.

## Локальный запуск

1. [Установить Serverless Framework](https://www.serverless.com/framework/docs/providers/aws/guide/installation/)
2. Установить зависимости выполнив `npm install` в директории проекта
3. Запустить локальный сервер, выполнив `npm run start` в директории проекта. Навык будет доступен по Webhook URL: http://localhost:3333/dev/webhook.
