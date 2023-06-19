# Udemy IT基礎知識とAWSの基礎力を習得する講座

- [講座URL](https://www.udemy.com/course/awsit-nb/learn/lecture/20315147#overview)
- 上記講座の学習記録を残す

## セッション2: サーバーを理解する

- サーバーとは何か
- 公開鍵認証方式とは何か
- EC2でサーバーを立てる(ハンズオン)

### EC2を起動してSSHに接続する

- 概要

    ``` plantuml
    @startuml
    class EC2{
        Public IP Address
    }

    Client -> EC2: ssh
    note top on link
    PrivateKeyを使ってアクセスする
    end note

    Client -> EC2: ブラウザでアクセス
    Client <- Apacheサーバー: ブラウザに応答する
    PublicKey --> EC2
    PrivateKey --> Client
    KeyPair <|-- PublicKey
    KeyPair <|-- PrivateKey
    EC2 o-- Apacheサーバー
    @enduml
    ```

- 作業手順
    1. EC2の作成
        - キーペアを作成する
            - `*.pem` ファイルをダウンロードする
    2. SSHで接続する
        - `pemファイル` を `.sshフォルダ` に移動
        `mv ~/Downloads/udemy-basic-keypair.pem ~/.ssh`
        - キーペアの権限を変更
        `❯ chmod 400 ~/.ssh/udemy-basic-keypair.pem`
        - SSH接続アクセス
        `❯ ssh -i ~/.ssh/udemy-basic-keypair.pem ec2-user@54.250.60.125`

    3. WEBサーバーの構築
        - Apacheサーバーをインストールする

            ``` bash
            # スーパーユーザーになる
            [ec2-user@ip-172-31-39-174 ~]$ sudo su
            # パッケージのアップデート
            [root@ip-172-31-39-174 ec2-user]# yum update -y
            # Apacheのインストール: httpd パッケージ
            [root@ip-172-31-39-174 ec2-user]# yum install httpd -y
            ```

        - Workspaceに移動する

            ``` bash
            [root@ip-172-31-39-174 ec2-user]# cd /var/www/html
            [root@ip-172-31-39-174 html]# ls
            ```

        - index.htmlを作成する

            ``` bash
            [root@ip-172-31-39-174 html]# ls
            [root@ip-172-31-39-174 html]# vim index.html
            [root@ip-172-31-39-174 html]# ls
            index.html
            [root@ip-172-31-39-174 html]# cat index.html
            <html><h1>hello world!!</h1></html>
            ```

        - サーバーの起動

            ``` bash
            [root@ip-172-31-39-174 html]# systemctl start httpd
            # EC2インスタンスが起動するとApacheサーバーを起動するように設定
            [root@ip-172-31-39-174 html]# systemctl enable httpd
            ```

## セッション3

- ネットワークの基礎
    - DNSサーバー
    - NAT
    - IPマスカレード
    - ISP
    - DHCPサーバー
    - IPアドレス
    - MACアドレス
- サブネット、サブネットマスク
    - サブネットマスクの使い方。運用方法。

### ネットワークの基礎

- `リクエスト` を送るには `住所(URL) -> IPアドレス` が必要
- `レスポンス` を送るためにも `住所(URL) -> IPアドレス` が必要
- `パケット` 送信するデータの単位
- `プロトコル` 通信方式のルール -> `HTTPプロトコル`
    - `HTTPプロトコル`: Webサーバとクライアントの間の通信プロトコル
        - 送信者 / 送信先のアドレス
        - データの送信順序
        - メッセージID
    - `HTTPSプロトコル`: HTTPをよりセキュアにしたプロトコル(推奨)
    - `FTPプロトコル`: ファイル転送を行うための通信プロトコル
- `DNSサーバー(Domain Name System)` IPアドレスとURLの対応関係を管理する
    - URL -> IPアドレスの変換をしてくれる  
    DNSサーバーと接続できないと `URL` でアクセスすることができない。

        ``` plantuml
        @startuml
        Client -> DNSサーバー: URL
        DNSサーバー -> DNSサーバー: Convert URL into IPアドレス 
        DNSサーバー -> Service: IPアドレス
        @enduml
        ```

    - DNSサーバーの階層構造

        ``` plantuml
        @startmindmap
        + root
        ++ jp
        +++ co
        ++++ yahoo
        +++++ mail
        +++++ www
        ++++ google
        +++++ maps
        +++ ne
        ++ com
        +++ facebook
        @endmindmap
        ```

- `ドメイン` の構成
    - <https://www.mercari.co.jp/blog/index>
        - トップレベルドメイン: jp
        - セカンドレベルドメイン: co
        - サードレベルドメイン: mercari
        - ホスト名: www
        - プロトコル: https
        - スキーム: https://
        - ディレクトリ: blob
        - ファイル名: index

- `ISP業者(インターネットサービスプロバイダ)` インターネットの接続を提供する
    - `ドメイン登録` をしてくれる
    - `DNSサーバ` を運用してくれる

- `Webブラウザの通信` の仕組み
    - `URI`: Uniform Resource Identifier URLとURNの総称
    - `HTML`: Webブラウザの画面表示に使う言語

- `インターネット` と `イーサネット`
    - `インターネット` 世界中に接続されたネットワークを指す言葉
    - `イーサネット` インターネットを構成するネットワークの接続方式
        - `LAN(Local Area Network)` ケーブルを使って接続する

- `中継機器` ネットワークの中継
    - `ISP` が世界規模の接続ができるようにDNSサーバーを使って宛先を決めている。
    - `モデム` 家庭内のネットワークの中継をしている。Private Network内の宛先を決めている。

- `デフォルトゲートウェイ` 最初に送信される場所。外部との接触点。
    - `ルーティングテーブル` で接続先を決めている

- `MACアドレス` の使い道
    - ネットワーク接続機器に製造時に設定されるアドレス。
    - 変更できない。(仮想のMACアドレスを付与した場合は変更できる)
    - 物理アドレスと言われる
    - イーサネット上の機器を区別するために使う。
    - 近いネットワークの機器と通信する際に利用する
    - バケツリレーのように通信する
    - `IPアドレス` はネットワーク上で追加で設定されるアドレス。
        - 変更可能。(意図的に固定しないと変更される)
        - 論理アドレス
        - 遠くのネットワークに接続するために使う
    - 通信イメージ

    ``` plantuml
    @startuml
    class MacAddress1{}
    MacAddress1 -> MacAddress2
    MacAddress2 -> MacAddress3
    MacAddress3 -> MacAddress4

    MacAddress1 -- IPAddress1
    MacAddress1 -- IPAddress2
    MacAddress4 --- IPAddress3
    IPAddress1 --> IPAddress3

    note top of MacAddress1
    Macアドレスでの通信はバケツリー
    MacAddress1からMacAddress4にアクセスする場合は
    途中の機器を経由する必要がある
    endnote

    note bottom of IPAddress1
    IPアドレスは遠くの機器と直接通信するイメージ
    IPAddress1からIPAddress3にアクセスする場合は
    途中の機器を経由する必要がない(実際はMACアドレスを使ってアクセスする)
    endnote
    @enduml
    ```

    - 実際の通信のイメージ

    ``` plantuml
    @startuml
    Client -> モデム: MACアドレス
    モデム -> DNSサーバー: MACアドレス
    DNSサーバー -> 中継機: MACアドレス
    中継機 -> 目的のサーバー: MACアドレス
    Client --> 目的のサーバー: IPアドレス
    note right
    Clientから目的のサーバに
    IPアドレスを使ってアクセスする場合も
    MACアドレスで機器を経由してアクセスする
    end note
    @enduml
    ```

- `グローバルIPアドレス`
    - IPv4形式の `134.128.24.16` の形式のIPアドレス
        - 枯渇している。足りていない
    - IPv6形式の `2001:268:c05f:c203:e0f5:fd5c:9c4f:d7d` の形式のIPアドレス
        - 徐々にこちらに移行している
    - インターネット上でのやり取りに利用するIPアドレス

- `プライベートIPアドレス`
    - 限られたエリアで利用する `IPアドレス`
    - IPアドレスは自由に付与することができる
    - `グローバルIPアドレス` への変換は `NAT` で行われる
        - `IPマスカレード` 複数のプライベートIPアドレスを一つの `グローバルIPアドレス` に変換する

    ``` plantuml
    @startuml
    class ルータ {
        IPマスカレード()
        NAT()
        DHCP()
    }

    グローバルIPアドレス <-- ルータ
    ルータ --> プライベートIPアドレス
    @enduml
    ```

- `DHCPサーバー` を使って `プライベートIPアドレス` が付与される

- プライベートネットワークの構成
    - ネットワークの範囲を決めるのは `IPアドレス` + `サブネットマスク`
        - `10.0.1.0/16` の `/16` の部分
    - `サブネットマスク` の使い方
        - `CIDR(Classless Inter-Domain Routing)(サイダー)` で範囲を指定する
        - 数字が使えるネットワークの範囲を決める
            - 8 : 左から8桁目までをロックする。10進の1セット  
            **xx**.xx.xx.xx
            - 16: 左から16桁目までをロックする。10進の2セット分
            **xx**.**xx**.xx.xx
            - 24: 左から24桁目までをロックする。10進の3セット分
            **xx**.**xx**.**xx**.xx
            - 32: 左から16桁目までをロックする。10進の4セット分。一意のIPアドレスのみ認める。
            **xx**.**xx**.**xx**.**xx**
        - 一覧表

            |サブネットマスク|IPアドレス数|
            |---|---|
            |/18|16384|
            |/20|4096|
            |/22|1024|
            |/24|256|
            |/26|64|
            |/28|16|
        - ローカルなネットワークのグループ分に使うことができる

    ``` plantuml
    @startuml
    package AZ <<Rectangle>> {
        package VPC <<Rectangle>> {
            class IPアドレス {
                10.0.1.0/16
            }
            note bottom: 10.0.xx.xxの範囲を使える
            package パブリックネットワーク <<Rectangle>> {
            class IPアドレス {
                10.0.1.0/24
            }
            note bottom: 10.0.1.xxの範囲を使える
                class publicEC2
            }
            package プライベートネットワーク <<Rectangle>> {
            class IPアドレス {
                10.0.2.0/24
            }
            note bottom: 10.0.2.xxの範囲を使える
                class privateEC2
            }
        }
    }
    @enduml
    ```

- メールの通信のルール
    - `SMTPサーバー` 送信用のサーバ
        - `SMTPプロトコル(Simple Mail Transfer Protocol)` メール送信用のプロトコル
    - `POP/IMAPサーバー` 受信用のサーバ
        - `POP(Post Office Protocol)` メール受信用のプロトコル

- `OSI参照モデル` 通信ルールの規約
    1. アプリケーション層:
        - Chromeなど  
        - `POP/SMTP` プロトコルが関わってくる
        - `HTTP/HTTPS` プロトコルが関わってくる
    2. プレゼンテーション層:
        - 文字コード・圧縮・暗号/復号方法など
        - `SSL` 暗号通信プロトコル
    3. セッション層:
        - アプリケーションのセッション(連続した処理)に関わる処理
    4. トランスポート層:
        - ノード間のデータ転送における `コネクション`。
        - ポート番号の割り当ての規定  
        - `TCP` 通信プロトコル
        - `コネクション`: 論理的な回線を接続する。
        - `セッション`: 通信の開始から終了まで
    5. ネットワーク層:
        - `IP` アドレスを利用した割り当てなどを行う
        - ルーティングもここで行なっている
    6. データリンク層:
        - MACアドレスによるノード間の通信の規定
        - ネットワーク回線上で直接接続されたノード間の通信の規定
    7. 物理層:
        - ビット(`0`,`1`)を使った実際のコンピュータが送受信する伝送方式のプロトコルを規定

- ポート番号
    - 通信の出入り口になるのがポート
    - `エンドポイント` である
    - `コンピュータ` のソフトウェアごとにポート番号が設定される

- `VPC(Virtual Private Cloud)` 仮想のネットワーク環境

### ハンズオン: AWSネットワークを作る

Route 53についてはDomainの取得ができなかったので未対応

1. VPCを作成する
    - CIDR: 10.0.0.0/16
2. インターネットゲートウェイを作る
    - ルータの役割を持っていてVPCとインターネットを接続する役割を持つ
3. インターネットゲートウェイをVPCにアタッチする
4. サブネットを作る
    - blue, red, greenの3つのサブネットを作成
5. サブネットのルートテーブルを設定する
    - サブネットを外部と接続するため
    - ルートテーブルを編集する
    - `0.0.0.0/0` への通信を2.で作ったインターネットゲートウェイを通して実行できるようにした
6. セキュリティグループの設定
    - HTTP, HTTPS, SMTPを許可する
    - EC2にアクセスすることはできなかった。。。
        - HTTPプロトコルではアクセスできた
        - HTTPSプロトコルではできなかった
