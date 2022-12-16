# 問題点

## Section6
Mac環境と `minikube` の組み合わせではHostPathの確認ができない。
`minikube` で指定できるPathは[Documentation](https://minikube.sigs.k8s.io/docs/handbook/persistent_volumes/)より、制限されている。
2022/12月のMac Versionでは対象のPathでディレクトリを作ることができないためである。
