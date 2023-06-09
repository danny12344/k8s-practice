# K8s Practice

To start minikube: 
```bash
minikube start
```

Creating an ubuntu pod:
1st create yaml file name `ubuntu-pod.yaml`
Contents:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: ubuntu-pod
spec:
  containers:
  - name: ubuntu-container
    image: ubuntu
    command:
    - sleep
    - "3600"
```

Run command to start the pod:

```bash
kubectl apply -f ubuntu-pod.yaml
```

To check pod is running:

```bash
kubectl get pods
```

To access the pod:

```
kubectl exec -it ubuntu-pod -- /bin/bash
```

Pod has no cli tools except `apt` - to install python dependencies first run:

```bash
sudo apt install software-properties-common
```

and install python dependencies from source:

```bash
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
```

install python 3.9 source code using `wget`:

```bash
wget https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tgz
```


install node:

```bash
curl -fsSL https://deb.nodesource.com/setup_lts.x
sudo apt install -y nodejs
```