# 歩行情報蓄積及び現在位置推定サーバ

> [!IMPORTANT]
> 環境変数は[こちらから](https://kjlb.esa.io/posts/6068)確認してください

## 実行方法

### 開発環境

#### 0. `uv`のインストール

```shell
brew install uv
```

#### 1. `db`コンテナの立ち上げ

このコマンドは`docker-compose.yml`が存在するディレクトリで実行してください

```shell
make app-up
```

#### 2. `server`ディレクトリに移動

```shell
cd server
```

#### 3. サーバの起動

```shell
uv run uvicorn main:app --reload
```

### 本番環境

> [!NOTE]
> 梶研サーバで実行する場合の方法です

#### 1. サーバにログイン

サーバの管理者に聞きながら`kajilab-realtime-particle-filter-server`に SSH 接続をできるようにしてください

#### 2. ディレクトリの移動

```
cd src/walking-information-storage-server
```

#### 3. docker コンテナの立ち上げ

```
sudo docker-compose build && sudo docker-compose up
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
