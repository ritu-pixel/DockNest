# 🍞 Bakery Foundation Project — Packer + AWS EC2 on Windows

## Overview
This project demonstrates how to **build a custom Amazon Machine Image (AMI)** using **Packer** on Windows, and then **launch and connect** to an AWS EC2 instance based on that AMI.

You will:
- Install and configure Packer & AWS CLI on Windows.
- Create a Packer template to install **Python 3.9** on Ubuntu 20.04.
- Build the AMI automatically with Packer.
- Launch an EC2 instance from the AMI.
- Connect to the instance using SSH.

---

## Prerequisites

Make sure you have:
- A Windows machine with Administrator access.
- An AWS account with an IAM user and programmatic access (AWS Access Key + Secret).
- A Key Pair (`.pem` file) for SSH connection.
- Basic AWS and PowerShell knowledge.

---

## Step 1: Install Tools

### 1.1 Install Packer
- Download Packer: [Packer Downloads](https://developer.hashicorp.com/packer/downloads).
- Extract it and move `packer.exe` to `C:\packer`.
- Add `C:\packer` to your **System PATH**.
- Verify installation:
  ```bash
  packer --version
  ```
![alt text](<Screenshot 2025-04-27 184142.png>)
![alt text](<Screenshot 2025-04-27 184149.png>)
### 1.2 Install AWS CLI
- Download: [AWS CLI Windows Installer](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
- Install it by following the setup wizard.
- Verify installation:
  ```bash
  aws --version
  ```
![alt text](<Screenshot 2025-04-27 204105.png>)

### 1.3 Configure AWS CLI
In PowerShell:
```bash
aws configure
```
Enter:
- AWS Access Key ID
- AWS Secret Access Key
- Default region (example: `us-east-1`)
- Default output format: `json`
![alt text](<Screenshot 2025-04-27 204105-1.png>)
---

## Step 2: Create a Packer Template

### 2.1 Create HCL Template (`bakery.pkr.hcl`)

```hcl
packer {
  required_plugins {
    amazon = {
      source  = "github.com/hashicorp/amazon"
      version = ">= 1.0.0"
    }
  }
}

variable "aws_region" {
  default = "us-east-1"
}

source "amazon-ebs" "python39" {
  ami_name      = "bakery-foundation-python39-${formatdate("YYYYMMDD-HHmmss", timestamp())}"
  instance_type = "t2.micro"
  region        = var.aws_region
  source_ami    = "ami-xxxxxxxxxxxxxxx"  # (Replace with latest Ubuntu 20.04 AMI ID)
  ssh_username  = "ubuntu"
}

build {
  sources = ["source.amazon-ebs.python39"]

  provisioner "shell" {
    inline = [
      "sudo apt-get update",
      "sudo apt-get install -y python3.9 python3.9-venv python3.9-dev"
    ]
  }
}
```


📝 Save this file as:  
```text
C:\packer\bakery.pkr.hcl
```
![alt text](<Screenshot 2025-04-27 205238.png>)
---

### 2.2 Find the Latest Ubuntu 20.04 AMI

Run:
```bash
aws ec2 describe-images --owners 099720109477 --filters "Name=name,Values=ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*" --query "Images | sort_by(@, &CreationDate)[-1].ImageId" --output text
```
👉 Replace `source_ami` in `bakery.pkr.hcl` with the AMI ID you find.

---

## Step 3: Build the AMI

### 3.1 Initialize and Validate

```bash
cd C:\packer
packer init .
packer validate bakery.pkr.hcl
```
![alt text](<Screenshot 2025-04-27 204312.png>)
![alt text](<Screenshot 2025-04-27 204327.png>)
✅ Expected output:  
```text
The configuration is valid.
```
![alt text](<Screenshot 2025-04-27 204855.png>)

### 3.2 Build the AMI

```bash
packer build bakery.pkr.hcl
```
![alt text](<Screenshot 2025-04-27 205325.png>)
![alt text](<Screenshot 2025-04-27 205356.png>)
![alt text](<Screenshot 2025-04-27 210548.png>)
Packer will:
- Launch a temporary EC2 instance.
- Install Python 3.9.
- Create an AMI.
- Terminate the instance automatically.

---

## Step 4: Launch and Test the AMI

### 4.1 Find Your Custom AMI

- Open the AWS Management Console.
- Go to EC2 → **AMIs** (Make sure the correct region is selected).
- Find the AMI with name like:  
  ```
  bakery-foundation-python39-YYYYMMDD-HHmmss
  ```
![alt text](<Screenshot 2025-04-27 210536.png>)
### 4.2 Launch EC2 Instance from AMI

- Click **Launch Instance**.
- Under **My AMIs**, select your custom AMI.
- Choose instance type (e.g., `t2.micro`).
- Select your Key Pair (or create a new one).
- Set security group to allow SSH (port 22).
- Launch the instance.
![alt text](<Screenshot 2025-04-27 210818.png>)

---

## Step 5: Connect to the Instance

After your instance is running:
- Find its **Public IPv4 address** in EC2 Console.

Connect via SSH:

```bash
ssh -i "C:\path\to\your-key.pem" ubuntu@your-public-ip
```

Example:
```bash
ssh -i "C:\Users\Ritu Rajput\Downloads\streamlit.pem" ubuntu@44.192.120.21
```
![alt text](<Screenshot 2025-04-27 211753.png>)
⚠️ If you see **"Connection timed out"**, make sure:
- Instance is running (not terminated).
- Security group allows inbound SSH on port 22.
- Public IP exists.

---

## Step 6: Verify Python 3.9 Installation

Inside the server:

```bash
python3.9 --version
```

✅ You should see:
```text
Python 3.9.x
```
![alt text](<Screenshot 2025-04-27 211847.png>)
### Notes:

- `python3` will point to default Ubuntu Python 3.8.
- `python3.9` is installed separately via apt.

---

## Troubleshooting

| Issue | Solution |
|:------|:---------|
| Instance is terminated | Build new AMI and launch again |
| SSH Timeout | Check Security Group, Public IP, and instance state |
| PEM file errors | Ensure correct path and permissions of `.pem` file |

---

## Conclusion

🎉 You have successfully:
- Set up Packer on Windows.
- Created a custom AWS AMI.
- Deployed an EC2 instance from it.
- Connected and verified Python 3.9 installation.

---
