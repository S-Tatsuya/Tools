# 【AWS EC2入門】クラウド上にサーバを構築！SSH接続してFlaskのWebアプリをデプロイしてみよう！〜初心者向け〜

[Youtuber サプーの Youtube講座の学習記録](https://www.youtube.com/watch?v=AGmkG0wJ8LA&list=WL&index=2)

## やること

- 目標:EC2を使ってサーバーを立ててその中に簡単なWebアプリをデプロイする
- 手順1. AWSのアカウントの登録
- 手順2. キーペアの作成
  - キーペア名: `aws_private_account`
  - `/Users/sakuraitatsuya/.ssh` にキーペアのファイルを格納
  - `chmod 400 ~/.ssh/aws_private_account.pem` を実行する
    - このファイルを無くさない。他の人に触られないようにするため
- 手順3: EC2インスタンスを作成する
  - EC2名: `supu_server`
- 手順4: SSHで接続する
  - SSHの接続コマンド `ssh -i ${キーペアファイルパス} ${user_name}@${host_name}`
  - 実際に使ったコマンド(AWSのサイトに載っている) `ssh -i "~/.ssh/aws_private_account.pem" ubuntu@ec2-54-250-156-204.ap-northeast-1.compute.amazonaws.com`
- 手順5: サーバーの準備
  - pythonコマンドでpython3を動作させられるようにする。 `sudo apt install python-is-python3`
  - `script.py` を作成してpythonを実行してみる
- 手順6: VSCodeでEC2インスタンスにアクセスする
  - 拡張機能のインストール: `Remote - SSH`
  - アクティビティバー - リモート エクスプローラーをクリック
  - SSH - `+`ボタン をクリック
  - SSH接続コマンドを設定
  - `~/.ssh/config` に設定を追加
  - 追加されたEC2インスタンス( `ec2-54-250-156-204.ap-northease-1.compute.amazonaws.com` )の新しいWindowで接続を選択
  - VSCodeのエクスプローラーで `/home/ubuntu/` を開く
- 手順7: Flaskを使ったデモの実施
  - Flaskのインストール
    - `sudo apt update`
    - `sudo apt install python3-pip`
    - `sudo pip install flask`
  - Webサーバーを実装
    - 詳細は後ほど・・・
  - `sudo flask --app flaskr run --port 80 --host 0.0.0.0
- 手順8: Webサーバーにアクセス
  - Flaskが出力するIPアドレスではWebサーバーにアクセス出来ない
  - EC2インスタンスの詳細画面の `パブリック IPv4 アドレス` でアクセスする必要がある
- 手順9: EC2の停止と終了
  - EC2のコンソールから対象のEC2を選択して `インスタンスの状態` で停止を選択する
  - EC2のコンソールから対象のEC2を選択して `インスタンスの状態` で終了を選択する

## 学んだこと
