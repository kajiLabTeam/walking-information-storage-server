# 歩行情報蓄積及び現在位置推定サーバ

> [!IMPORTANT]
> 環境変数は[こちらから](https://kjlb.esa.io/posts/6068)確認してください

## 実行方法

### 開発環境

#### 0. `uv`のインストール

```shell
brew install uv
```

#### 1. サーバの起動

```shell
uv run uvicorn main:app --reload
```

### 本番環境

> [!NOTE]
> 梶研サーバで実行する場合の方法です
>
> 実行の際は、`walking-information-walking-trajectory-db`が起動していることを確認してください

#### 1. サーバにログイン

サーバの管理者に聞きながら`kajilab-realtime-particle-filter-server`に SSH 接続をできるようにしてください

#### 2. ディレクトリの移動

```
cd src/walking-information-storage-server
```

#### 3. Docker ネットワークの作成

すでに作成してあるならこの手順は飛ばしてください

```
make create-network
```

#### 4. docker コンテナの立ち上げ

```
make up
```
