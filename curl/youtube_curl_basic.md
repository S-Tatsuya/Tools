# Youtube curlコマンドの基本と使用例

## 学習メモ

### GETメソッド

- ファイルに出力

    ```bash
    ❯ curl -o ./get_logs/google.html https://www.google.com/
    % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                    Dload  Upload   Total   Spent    Left  Speed
    100 18833    0 18833    0     0  80041      0 --:--:-- --:--:-- --:--:-- 81176
    ```

- Request Headerの出力

    ```bash
    ❯ curl -v https://www.google.com
    *   Trying 142.250.196.100:443...
    * Connected to www.google.com (142.250.196.100) port 443 (#0)
    * ALPN: offers h2,http/1.1
    * TLSv1.3 (OUT), TLS handshake, Client hello (1):
    * TLSv1.3 (IN), TLS handshake, Server hello (2):
    * TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
    * TLSv1.3 (IN), TLS handshake, Certificate (11):
    * TLSv1.3 (IN), TLS handshake, CERT verify (15):
    * TLSv1.3 (IN), TLS handshake, Finished (20):
    * TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
    * TLSv1.3 (OUT), TLS handshake, Finished (20):
    * SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
    # もっと情報は出てくる
    ```

- Response Headerのみ出力

    ```bash
    ❯ curl -I https://www.google.com
    HTTP/2 200 
    content-type: text/html; charset=ISO-8859-1
    content-security-policy-report-only: object-src 'none';base-uri 'self';script-src 'nonce-hrqxLN89ZGS8h7og80F-Xg' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp
    p3p: CP="This is not a P3P policy! See g.co/p3phelp for more info."
    date: Tue, 04 Jul 2023 12:04:12 GMT
    server: gws
    x-xss-protection: 0
    x-frame-options: SAMEORIGIN
    expires: Tue, 04 Jul 2023 12:04:12 GMT
    cache-control: private
    set-cookie: 1P_JAR=2023-07-04-12; expires=Thu, 03-Aug-2023 12:04:12 GMT; path=/; domain=.google.com; Secure
    set-cookie: AEC=Ad49MVGecqgGRrT2NyLaealwDwfhH-AGZQmJAnlPZpiO3cLQy2c6_7YUHw; expires=Sun, 31-Dec-2023 12:04:12 GMT; path=/; domain=.google.com; Secure; HttpOnly; SameSite=lax
    set-cookie: NID=511=T8NfJrisujFdYVIeRMDpmqevgoR9KhsnM--q5-pxHNPtOLvoSaotIL73Tw6YlQT3OGwbAoaDPmBUoSfdQxi55UznhYOD-8JFwrDFJLNfLPHQu3GC0Slo4LKskR2ODHWHKK_XwwIY2W3v-qsEimj689IbMnNmWPFocGhtJ92EZLg; expires=Wed, 03-Jan-2024 12:04:12 GMT; path=/; domain=.google.com; HttpOnly
    alt-svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000
    ```

- グローバルIPの取得

    ```bash
    ❯ curl ipinfo.io
    {
    "ip": "118.83.68.225",
    "hostname": "118-83-68-225.htoj.j-cnet.jp",
    "city": "Hachiōji",
    "region": "Tokyo",
    "country": "JP",
    "loc": "35.6558,139.3239",
    "org": "AS4721 JCOM Co., Ltd.",
    "postal": "338-0006",
    "timezone": "Asia/Tokyo",
    "readme": "https://ipinfo.io/missingauth"
    } 
    ```

### POSTメソッド

- メソッドの指定: `-X`オプション
    - `-d`オプションでファイルを指定

    ```bash
    curl -X POST -d "token=XXXXXXXX" https://sample.com/api/hoge
    ```

- JSONファイルのPOST:
    - `-H`オプションでJsonを指定
    - `-d`オプションでファイルを指定

    ```bash
    curl -X POST -H "content-type: application/json" \ -d @hoge.json https://sample.com/
    ```

### ブラウザの操作

- cURLの取得
    - Chromeのデバッグツールの `Copy as cURL` を使うことでcurlコマンドを取得できる

### ベンチマーク

- レスポンスタイムの取得:
    - `-w`オプションで`-w"%{time_total}\n"`で取得できる

    ```bash
    curl https://sample.com -w"%{time_total}\n
    ```

### VSCodeの拡張機能

- [Thunder Client](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client)
