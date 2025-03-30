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

### **Step 2: Enable Kubernetes Dashboard (Optional)**
```sh
minikube dashboard
```

### **Step 3: Verify Minikube Status**
```sh
minikube status
```

---

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

### **Step 2: Verify Deployment and Services**
Check deployments:
```sh
kubectl get deployments
```
Check running pods:
```sh
kubectl get pods
```
Check services:
```sh
kubectl get services
```

### **Step 3: Access the API Gateway**
Run:
```sh
minikube service api-gateway
```
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

---

## Cleanup
To delete all resources and stop Minikube:
```sh
kubectl delete all --all
minikube stop
minikube delete
```

---

## Future Enhancements
- Add more microservices
- Implement CI/CD pipeline
- Improve security with RBAC and network policies

---

## License
This project is licensed under the MIT License.

