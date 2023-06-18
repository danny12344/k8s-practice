# K8s Practice

To start minikube: 
```bash
minikube start
```

To stop minikubes:

```bash
minikube stop
```

To delete minikubes:

```bash
minikube delete
```

minikube status

To get logs:

```bash
kubectl logs <pod-name>
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
kubectl apply -f ubuntu-service.yaml
kubectl apply -f ubuntu-pod.yaml
```
<!-- kubectl apply -f ubuntu-pod.yaml --port=8000 -->


To check pod is running:

```bash
kubectl get pods
```

```bash
kubectl port-forward ubuntu-pod 4200:4200
```

http://localhost:8000/send-hi

To access the pod:

```bash
kubectl exec -it ubuntu-pod -- /bin/bash
```

Pod has no cli tools except `apt` - to install python dependencies first run:

```bash
sudo apt install software-properties-common
```

and install python dependencies from source:

```bash
apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
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


```bash
apt install python3-pip
apt install python3.10-venv
python3 -m venv myenv
```


TO DELETE MINIKUBE:
```bash
minikube stop; minikube delete &&
docker stop $(docker ps -aq) &&
rm -rf ~/.kube ~/.minikube &&
sudo rm -rf /usr/local/bin/localkube /usr/local/bin/minikube &&
launchctl stop '*kubelet*.mount' &&
launchctl stop localkube.service &&
launchctl disable localkube.service &&
sudo rm -rf /etc/kubernetes/ &&
docker system prune -af --volumes
```