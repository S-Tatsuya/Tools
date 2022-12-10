# Dockerイメージのベースイメージの指定
FROM centos:7

# ホストPCからコピーするファイルを決める
COPY docker-entrypoint.sh /var/tmp

# Docker内で実行するコマンド
RUN mv /var/tmp/docker-entrypoint.sh /usr/local/bin; \
    chmod +x /usr/local/bin/docker-entrypoint.sh;

# Docker開始時に実行されるコマンド
ENTRYPOINT [ "docker-entrypoint.sh" ]

# ENTRYPOINT実行後に実行されるコマンド
# Docker実行時のコマンドで書き換え可能
CMD [ "echo", "Hellow world!!"]
