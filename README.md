# Serverless Framework で SNS + Lambda の Slack 通知を簡単に作るサンプル

# デプロイ

## 1. config の用意

以下の形式の `config.*.json` を用意する

```json
{
  "WEBHOOK_URL": "https://hooks.slack.com/services/XXXXXXXX/XXXXXXXX/XXXXXXXX"
}
```

```bash
$ ls config*
config.dev.json  config.stg.json
```

## 2. デプロイ

[Serverless Framework](https://www.serverless.com/) を使って、以下のコマンドでデプロイする

```bash
$ sls deploy -v             # dev 環境へのデプロイ
$ sls deploy -v --stage stg # stg 環境へのデプロイ
```
