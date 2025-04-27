# Minikube Microservices

This repository contains a microservices-based architecture deployed on Minikube using Kubernetes. It includes various services such as `api-gateway` and other microservices, along with configurations for deployment and networking.

---

## Prerequisites

Ensure you have the following installed:
- [Docker](https://docs.docker.com/get-docker/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [Kubectl](https://kubernetes.io/docs/tasks/tools/)

---

## Setting Up Minikube

### **Step 1: Start Minikube**
```sh
minikube start --driver=docker
```
![Screenshot 2025-03-22 120608](https://github.com/user-attachments/assets/8ecdd5bb-7bce-422a-a4bb-e2804e321b57)

### **Step 2: Enable Kubernetes Dashboard (Optional)**
```sh
minikube dashboard
```
![Screenshot 2025-03-22 182109](https://github.com/user-attachments/assets/2c773ace-9a3f-44ba-86fe-011013da9a07)

### **Step 3: Verify Minikube Status**
```sh
minikube status
```

---
![Screenshot 2025-03-22 120620](https://github.com/user-attachments/assets/e3145ac2-aace-47f1-b0ba-bfa8bc5154d6)

## Deploying Microservices

### **Step 1: Apply Deployment and Service Configurations**
Ensure you have the necessary YAML files for deployment. If not, create `api-gateway-deployment.yml`:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-gateway
  labels:
    app: api-gateway
spec:
  replicas: 1
  selector:
    matchLabels:
      app: api-gateway
  template:
    metadata:
      labels:
        app: api-gateway
    spec:
      containers:
        - name: api-gateway
          image: <your-docker-image>
          ports:
            - containerPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  name: api-gateway
spec:
  selector:
    app: api-gateway
  ports:
    - protocol: TCP
      port: 8080
      targetPort: 8080
  type: NodePort
```

Apply the configurations:
```sh
kubectl apply -f api-gateway-deployment.yml
```
![Screenshot 2025-03-22 182119](https://github.com/user-attachments/assets/af146adb-19f7-46af-8a47-65a4aa64514b)
![Screenshot 2025-03-22 182132](https://github.com/user-attachments/assets/9182b355-9643-4f21-95cd-9c07a8a72906)


### **Step 2: Verify Deployment and Services**
Check deployments:
```sh
kubectl get deployments
```
Check running pods:
```sh
kubectl get pods
```
![Screenshot 2025-03-22 182241](https://github.com/user-attachments/assets/1933a8f3-38d1-48eb-a8f4-8f1f48a42a95)

Check services:
```sh
kubectl get services
```
![Screenshot 2025-03-22 182158](https://github.com/user-attachments/assets/e42277ea-8810-4176-b21a-873ca65e6fe7)

### **Step 3: Access the API Gateway**
Run:
```sh
minikube service api-gateway
```
![Screenshot 2025-03-22 182230](https://github.com/user-attachments/assets/3239eb94-5b74-4f67-9f27-a281cb5e26ee)

This will expose the API Gateway and provide a URL.

---

## RBAC Configuration (Optional)
If Role-Based Access Control (RBAC) is required, create `rbac.yml`:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: api-gateway-role
rules:
- apiGroups: [""]
  resources: ["pods", "services", "endpoints"]
  verbs: ["get", "watch", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: api-gateway-rolebinding
  namespace: default
subjects:
- kind: ServiceAccount
  name: default
  namespace: default
roleRef:
  kind: Role
  name: api-gateway-role
  apiGroup: rbac.authorization.k8s.io
```
Apply RBAC settings:
```sh
kubectl apply -f rbac.yml
```

---

## Troubleshooting

### **1. Service Not Found Error**
If running `minikube service api-gateway` gives an error:
```sh
kubectl get services --all-namespaces
```
Ensure the service is listed and running.

### **2. Deployment Not Found**
If `kubectl logs deployment/api-gateway` fails, check existing deployments:
```sh
kubectl get deployments --all-namespaces
```

### **3. Check Pod Logs**
To check pod logs:
```sh
kubectl logs <pod-name>
```
Find the pod name using:
```sh
kubectl get pods
```
![Screenshot 2025-03-22 182253](https://github.com/user-attachments/assets/10a06cb9-959c-4f8c-b8a3-46c25bee04ba)
![Screenshot 2025-03-22 182305](https://github.com/user-attachments/assets/6658de9c-8ef1-4931-bc71-0ebf6ba6db03)

---

## Cleanup
To delete all resources and stop Minikube:
```sh
kubectl delete all --all
minikube stop
minikube delete
```
![Screenshot 2025-03-22 182329](https://github.com/user-attachments/assets/bda3e399-0fe6-451b-8f44-36afbee195f6)

---

## Future Enhancements
- Add more microservices
- Implement CI/CD pipeline
- Improve security with RBAC and network policies

---

## License
This project is licensed under the MIT License.

