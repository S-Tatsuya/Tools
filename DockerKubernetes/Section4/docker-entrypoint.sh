#! /bin/sh

env

# Dockerコマンドの引数を受け取る
# このコマンドをコメントアウトするとDockerfileの`CMD`が実行されない
exec "$@"
