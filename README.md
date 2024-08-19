# 軌跡蓄積を行うサーバ

> [!IMPORTANT]
> 環境変数は[こちらから](https://kjlb.esa.io/posts/6068)確認してください

## 実行方法

```
make app-up
```

## その他

### DB コンテナに入りたいとき

```bash
make db
```

### ER 図生成

```
make spy-up
```

`http://localhost:8080/public/relationships.html`にアクセスすると ER 図を閲覧できます
