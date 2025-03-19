# Minikube with Docker on Windows ☸️

## Introduction
This guide explains how to set up **Minikube** using **Docker** as the driver on Windows. You will learn how to deploy an **Nginx** application in a Kubernetes cluster, expose it, and access it via a web browser.

---

## 📌 Prerequisites
Make sure you have the following installed:

1. **Docker Desktop** 🐳 ([Download here](https://www.docker.com/products/docker-desktop))
   - Ensure that **WSL 2 backend** is enabled (recommended).
   - For Windows Pro/Enterprise, enable **Hyper-V**.

2. **Minikube** 📦 ([Install Guide](https://minikube.sigs.k8s.io/docs/start/))
   - If using **Chocolatey**, install it via:
     ```sh
     choco install minikube
     ```

3. **Kubectl** (Kubernetes CLI) 🖥️
   - Install via **Chocolatey**:
     ```sh
     choco install kubernetes-cli
     ```
   - Verify installation:
     ```sh
     kubectl version --client
     ```

---

## ✅ Step 1: Start Minikube with Docker Driver

Ensure **Docker Desktop** is running, then start Minikube:
```sh
minikube start --driver=docker
```

Verify Minikube status:
```sh
minikube status
```

If it’s running correctly, you should see output like:
```
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured
```

---

## ✅ Step 2: Deploy Nginx on Minikube 🚀

Create an **Nginx deployment**:
```sh
kubectl create deployment nginx --image=nginx
```

Check if the pod is running:
```sh
kubectl get pods
```
Expected output:
```
NAME                    READY   STATUS    RESTARTS   AGE
nginx-d6bf76b7b-xyz12   1/1     Running   0          10s
```

---

## ✅ Step 3: Expose Nginx Deployment

Expose the deployment using a **NodePort** service:
```sh
kubectl expose deployment nginx --type=NodePort --port=80
```

Verify the service is created:
```sh
kubectl get services
```
Expected output:
```
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
nginx        NodePort    10.98.120.150  <none>        80:xxxxx/TCP   5s
```

**Note:** `xxxxx` is the port number assigned to Nginx.

---

## ✅ Step 4: Get Service URL

Retrieve the service URL to access Nginx in a browser:
```sh
minikube service nginx --url
```

Expected output:
```
http://192.168.49.2:xxxxx
```
Copy the URL and open it in your browser. 🎉

---

## ✅ Step 5: Scale the Nginx Deployment

Increase the number of Nginx pods to **3**:
```sh
kubectl scale deployment nginx --replicas=3
```

Verify the pods:
```sh
kubectl get pods
```
Expected output:
```
NAME                    READY   STATUS    RESTARTS   AGE
nginx-d6bf76b7b-xyz12   1/1     Running   0          2m
nginx-d6bf76b7b-xyz34   1/1     Running   0          10s
nginx-d6bf76b7b-xyz56   1/1     Running   0          10s
```

---

## ✅ Step 6: Clean Up Resources 🧹

To delete the **Nginx** deployment and service:
```sh
kubectl delete service nginx
kubectl delete deployment nginx
```

To stop Minikube:
```sh
minikube stop
```

To completely delete the Minikube cluster:
```sh
minikube delete
```

---

## 🎯 Conclusion
By following this guide, you successfully:
- Installed Minikube and Docker 🐳
- Deployed an Nginx application 🚀
- Exposed it via a **NodePort** service 🌍
- Accessed it in a web browser 🖥️

Now, you can experiment further with Kubernetes! 💡⚡

---

🔗 **References:**
- [Minikube Documentation](https://minikube.sigs.k8s.io/docs/)
- [Kubernetes Official Docs](https://kubernetes.io/docs/)

