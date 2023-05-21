# AWSの使い方を学ぶ

## AWSについて

以下のような様々なサービスを提供している

- `IaaS`(Infrastructure as a Service)  
- `PaaS`(Platform as a Service)
- `FaaS`(Function as a Service)

### AWSの操作方法

- マネジメントコンソール
- AWS CLI
- ツール
- SDK

### AWSでアプリケーションの実行環境

#### 概要

- 実行環境の例
  - サーバ:EC2
  - コンテナ:ECS
  - Lambda

コンテナはサーバーの中で動く。  
サーバレスでの構築もできる。

#### 典型的なWebアプリケーションの構成例

- 講座の最終目標:EC on Fargate を複数とRDSを使う(Auto Scaling)

``` plantuml
@startuml
package "VPC" {
    package "Auto Scaling" #FFA500 {
        ECSonFargate_A -[hidden]- ECSonFargate_B
    }
    ELB -> ECSonFargate_A
    ELB -> ECSonFargate_B
    ECSonFargate_A <-> RDS
    ECSonFargate_B <-> RDS
}
@enduml
```

- 参考:★EC2を複数とRDSを使う(Auto Scaling)★

``` plantuml
@startuml
package "VPC" {
    package "Auto Scaling" #FFA500 {
        EC2_A -[hidden]- EC2_B
    }
    ELB -> EC2_A
    ELB -> EC2_B
    EC2_A <-> RDS
    EC2_B <-> RDS
}
@enduml
```

##### その他の構成

- 前提:Webアプリケーションの構成

``` plantuml
@startuml
class Webアプリケーション

Webアプリケーション -> データベース
Webアプリケーション <- データベース
@enduml
```

- AWS:EC2一つの場合

``` plantuml
@startuml
package "VPC" {
    class EC2
}

note right of EC2
一つのEC2の中でWebアプリとDBを両方動かす。
[デメリット]
DBをサーバにインストールすると
パッチ、バックアップなど対応するべきことが多い
endnote
@enduml
```

- AWS:EC2とRDSを使う

``` plantuml
@startuml
package "VPC" {
    class EC2
    EC2 <-> RDS
}

note right of RDS
DBを分けるパターン
[メリット]
DBの管理をクラウド事業者に任せることができる。
endnote
@enduml
```

- AWS:EC2を複数とRDSを使う

``` plantuml
@startuml
package "VPC" {
    EC2_A <-> RDS
    EC2_B <-> RDS
    EC2_A -[hidden]- EC2_B
}
@enduml
```

- ★AWS:EC2を複数とRDSを使う(Auto Scaling)★

``` plantuml
@startuml
package "VPC" {
    package "Auto Scaling" #FFA500 {
        EC2_A -[hidden]- EC2_B
    }
    ELB -> EC2_A
    ELB -> EC2_B
    EC2_A <-> RDS
    EC2_B <-> RDS
}

note top of ELB
Auto Scalingを補助して、
適切なスケールを行ってくれるサービス
endnote
@enduml
```

- ★AWS:EC2を複数とRDSを使う(Auto Scaling)★

``` plantuml
@startuml
package "VPC" {
    package "Auto Scaling" #FFA500 {
        ECSonFargate_A -[hidden]- ECSonFargate_B
    }
    ELB -> ECSonFargate_A
    ELB -> ECSonFargate_B
    ECSonFargate_A <-> RDS
    ECSonFargate_B <-> RDS
}
@enduml
```

### AWSの料金体系

- [料金説明](https://aws.amazon.com/jp/pricing/?aws-products-pricing.sort-by=item.additionalFields.productNameLowercase&aws-products-pricing.sort-order=asc&awsf.Free%20Tier%20Type=*all&awsf.tech-category=*all)
- [無料枠](https://aws.amazon.com/jp/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all)

## クラウドの定義

### 定義

クラウドコンピューティングは、共用の構成可能なコンピューティングリソース（ネットワーク、サー
バー、ストレージ、アプリケーション、サービス）の集積に、どこからでも、簡便に、必要に応じて、ネ
ットワーク経由でアクセスすることを可能とするモデルであり、最小限の利用手続きまたはサービス
プロバイダとのやりとりで速やかに割当てられ提供されるものである。このクラウドモデルは 5 つの
基本的な特徴と 3 つのサービスモデル、および 4 つの実装モデルによって構成される。

- オンデマンド・セルフサービス
- 幅広いネットワークアクセス
- リソースの共用
- スピーディな拡張性
- サービスが計測可能であること

### 参考資料

- [NISTの定義](https://www.ipa.go.jp/files/000025366.pdf)

## 1. VPCの作成

### 手順

- VPCの作成
  - `お使いのVPC -> VPCを作成 -> 以下の設定でVPCを作成` をクリック
    - VPCで料金はかからない
- RDSの作成
  - RDSのページに行く
  - 左のメニューから `サブネットグループ-> DBサブネットグループ を作成` を選択してサブネットグループを作成する
    - サブネットは各AZのプライベートサブネットを選択する。
  - 左のメニューから`データベース -> データベースの作成` を選択してデータベースを作成する。
- インスタンスとストレージは異なる料金が取られて
  - RDSを停止してもストレージの料金はかかる
    - ストレージに保存している内容はそのまま
  - RDSは停止してもインスタンスを7日後に自動で再起動する
    - 長期間使わないRDSのインスタンスは削除してしまっても良い

### VPCとは

`Virtual Private Cloud`のことAWS内の仮想ネットワーク環境

### VPCの仕組み

- リージョンとは
AWSのデータセンターがある地域を「リージョン」と呼ぶ  
- アベイラビリティゾーンとは
Availability Zoneはリージョンの中で電力やネットワークが独立している単位

- VPCはリージョン内に構築できる
  - アベイラビリティゾーンをまたがって構築できる。
    - 停電やネットワーク障害に強い環境にするため複数のAZにまたがるシステムが良い
- サブネットとはVPCを構成する単位
  - Public Subnet: インターネットから直接接続する必要がある部分
  - Private Subnet: インターネットから直接接続させたくない部分
- サブネットは `AZ` の単位で作成する必要がある。
  - AZ同士が通信するため？

### RDS

`Relational Database Service` のこと

## 2. コンテナの作成

### コンテナの作成手順

1. イメージをAWS Cloud9環境で作成する
    - `Cloud9 -> Create Environment` で環境を構築する
    - サーバのインスタンスが必要になる
    - Timeoutの設定でWebブラウザを閉じてから停止するまでの時間
    - `Cloud9` も停止してもストレージの料金がかかる
2. コンテナレジストリ( `ESR` )にイメージをPushする
    - `ECS -> リポジトリ -> リポジトリの作成` でDocker ImageをPushした
    - `リポジトリを選択 -> プッシュコマンドの表示` の指示に従ってDocker ImageをPushした
3. AWSのサーバ( `ES2` )でイメージをダウンロードしてコンテナを起動する
    - EC2からECRにアクセスする設定(イメージのダウンロード)
        - EC2を作成する。
        - EC2にアクセスする。
        - docker loginをしてECSにアクセスする権限を取得する
            - IAM Roleを作成する
    - ブラウザからEC2にアクセスする設定(ファイアウォール)の設定
        - EC2のパブリックIPアドレスにアクセスするとエラーになる
        - EC2のセキュリティのインバウンドルールを編集する
            - HTTPへのアクセスを許可する
    - EC2からRDSにアクセスする設定(データベースとの情報のやり取り)
        - Host URIを指定する
            - RDSのエンドポイントの内容を指定する
            - RDSのセキュリティのインバウンドルールを編集する

    ``` plantuml
    @startuml
    package VPC {
        EC2 -> RDS
        note on link
        RDSのセキュリティルール設定
        end note
    }
    EC2 <-- User
    note on link
    EC2のセキュリティルール設定
    end note
    ECR <-- EC2
    note on link
    ECRのセキュリテイルール設定
    end note
    @enduml
    ```

### AWS Cloud9とは

AWSが提供しているWebブラウザ上でコード実装できるサービス

### EC2とは

Amazon Machine Imageをもとにしたインスタンス
サーバの役割を担う

### AWS IAMとは

Identity and Access Management サービス。  
誰にどのリソースへのどのアクションを許可するかを管理するサービス。  
主に以下の4つの機能を使う

- IAM Policy: どのリソースへのどのアクションを許可するかの管理。JSON形式で設定する
- IAM User: AWSのユーザ。IAM Policyを設定する箱。誰に該当する。ユーザに対して設定する
  - アクセスキー、シークレットアクセス機を払い出すことで外部からアクセスすることが出来る
- IAM Role: AWSのリソース間のどのリソースへのどのアクションを許可するかに使う。EC2インスタンスなどAWSのリソースに設定する。

#### エラーの内容

``` bash
# awscliをインストールしていないとエラーになる

# awscliをインストール後
ubuntu@ip-10-0-2-81:~$ aws --version
aws-cli/1.22.34 Python/3.10.6 Linux/5.15.0-1028-aws botocore/1.23.34
ubuntu@ip-10-0-2-81:~$ aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin 076288582636.dkr.ecr.ap-northeast-1.amazonaws.com

# IAM Roleの設定前はアクセスの権限がないので失敗する
Unable to locate credentials. You can configure credentials by running "aws configure".
Error: Cannot perform an interactive login from a non TTY device

# dockerコマンドの前にsudoをつけていないため
ubuntu@ip-10-0-2-81:~$ aws ecr get-login-password --region ap-northeast-1 | docker login --username AWS --password-stdin 076288582636.dkr.ecr.ap-northeast-1.amazonaws.com
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/auth": dial unix /var/run/docker.sock: connect: permission denied

# 成功
ubuntu@ip-10-0-2-81:~$ aws ecr get-login-password --region ap-northeast-1 | sudo docker login --username AWS --password-stdin 076288582636.dkr.ecr.ap-northeast-1.amazonaws.com
WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
```

## ECS on Fargate

複数のサーバーでコンテナを使うことで `スケール` がしやすく、`冗長性` が高くなる。  
ただし、複数のコンテナの連携やオートスケールを手動で実行する必要があり、運用コストが高くなってしまう。  
上記課題を解決をするためには `コンテナオーケストレーション` というツールを使う必要がある。
これが ECS on Fargate !!(サーバーの管理が不要になる。ECS on EC2だとサーバーの管理が必要)
(Kubernetesも同じ、AWSのEKSはKubernetesを使うサービスである)

- 用語の整理
  - `サーバー` に複数の `コンテナ` を起動することが出来る
  - 複数の `サーバー` の塊が `クラスタ`
  - `コンテナオーケストレーション` で `クラスタ` に対して `コンテナ` を自動で `デプロイ` してくれる

### 基本概念

- クラスタ：複数のコンピュータの集まり(サーバー、サービスの塊、入れ物)
- タスク：タスク≒コンテナ。
- タスク定義：CPUやメモリのサイズ。コンテナのポートや環境変数などの設定。  
タスクを起動するのに使う
- サービス：起動するタスクの数、ロードバランサーの設定、デプロ時の設定などがある  
サービスはサーバーレスでのサーバーの代わり？

``` plantuml
@startuml
package クラスタ {
    package サービス {
        class タスクA {
        }
        class タスクB {
        }
    }
}

タスク定義 -> タスクA
タスク定義 -> タスクB
@enduml
```

## 教材

- [AWSコンテナサービス入門-AWSの基本からECS・Copilot・CI/CD・App Runnerまで](https://www.udemy.com/course/aws-container/learn/lecture/35553834?start=0#overview)

## GitHub Actions Runnerとして使用

``` bash
# Authentication


√ Connected to GitHub

# Runner Registration

Enter the name of the runner group to add this runner to: [press Enter for Default] 

# GitHubで表示される名前になる
Enter the name of runner: [press Enter for ip-10-0-12-150] 

# Labelの追加後からでも編集は出来る
This runner will have the following labels: 'self-hosted', 'Linux', 'X64' 
Enter any additional labels (ex. label-1,label-2): [press Enter to skip] aws-runner  

√ Runner successfully added
√ Runner connection is good

# Runner settings

Enter name of work folder: [press Enter for _work] 

√ Settings Saved.

ubuntu@ip-10-0-12-150:~/actions-runner$ ./run.sh

√ Connected to GitHub

Current runner version: '2.303.0'
2023-03-26 07:26:26Z: Listening for Jobs
```
