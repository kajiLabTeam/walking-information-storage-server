# 歩行情報蓄積及び現在位置推定サーバ

> [!IMPORTANT]
> 環境変数は[こちらから](https://kjlb.esa.io/posts/6068)確認してください
> 
> 事前準備：https://kjlb.esa.io/posts/7326

## 実行方法

> [!NOTE]
> 開発・本番ともに実行の際は、`walking-information-walking-trajectory-db`が起動していることを確認してください

### 開発環境

#### 1. Docker ネットワークの作成

すでに作成してあるならこの手順は飛ばしてください

```
make create-network
```

#### 2. サーバの起動

```shell
make up
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

#### 3. Docker ネットワークの作成

すでに作成してあるならこの手順は飛ばしてください

```
make create-network
```

#### 4. docker コンテナの立ち上げ

```
make up
```
