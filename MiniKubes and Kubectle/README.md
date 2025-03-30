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
     ![Screenshot 2025-03-19 222046](https://github.com/user-attachments/assets/ce216b3d-35c6-472a-8c67-e2345de8fba4)
![Screenshot 2025-03-19 222116](https://github.com/user-attachments/assets/3135a906-5bdb-42b3-ae8e-0c45f3413dab)


3. **Kubectl** (Kubernetes CLI) 🖥️
   - Install via **Chocolatey**:
     ```sh
     choco install kubernetes-cli
     ```
     ![Screenshot 2025-03-19 222150](https://github.com/user-attachments/assets/cbcfdf27-d1dc-4a14-af8c-746cf8e8a595)

   - Verify installation:
     ```sh
     kubectl version --client
     ```
![Screenshot 2025-03-19 222213](https://github.com/user-attachments/assets/0f481204-f31f-418f-a38d-9e261acf49e3)

---

## ✅ Step 1: Start Minikube with Docker Driver

Ensure **Docker Desktop** is running, then start Minikube:
```sh
minikube start --driver=docker
```
![Screenshot 2025-03-19 222803](https://github.com/user-attachments/assets/40bdca22-1fad-4ffa-8709-58182f317b3a)

Verify Minikube status:
```sh
minikube status
```
![Screenshot 2025-03-19 224033](https://github.com/user-attachments/assets/716473a4-2c1c-4b9c-be53-fab082283f5f)

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
![Screenshot 2025-03-19 224033](https://github.com/user-attachments/assets/caebb752-cad2-4cb8-82e6-651eaff158eb)

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
![Screenshot 2025-03-19 224649](https://github.com/user-attachments/assets/89071529-16ec-4a1c-b9ff-b61907b0496d)

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
![Screenshot 2025-03-19 225229](https://github.com/user-attachments/assets/cc3b447a-1ef9-412b-9845-fd9cde400b92)

---
![Screenshot 2025-03-19 224135](https://github.com/user-attachments/assets/83570e6b-d240-4582-9828-d5d4bcd1b445)
![Screenshot 2025-03-19 224156](https://github.com/user-attachments/assets/60c0aa3d-f905-48f8-982e-2425879e8a6a)


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
![Screenshot 2025-03-19 225319](https://github.com/user-attachments/assets/da086a9d-35b4-4188-a6fb-68ad8f2cf540)
![Screenshot 2025-03-19 225407](https://github.com/user-attachments/assets/07aa5378-ba00-4438-beb0-15b230b7b348)


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

