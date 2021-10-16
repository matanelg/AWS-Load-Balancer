# AWS-Load-Balancer

This repository comes to demonstrate how to serve applications on containers via aws load balancer.<br />
I used ansible for instances configuration and terraform for build the infrastructure As shown below.<br />

<p align="center">
  <img src="https://github.com/matanelg/AWS-Load-Balancer/blob/main/files/arc-00.png" width="100%" height="100%" />
</p>


## Quick Start

## 01. Export your aws access key & secret key (Make sure the user have premission to creating resources).
```bash
export AWS_ACCESS_KEY=""
export AWS_SECRET_KEY=""
```

## 02. Create two ssh key-pair with the names public-instance & private-instance .
```bash
ssh-keygen
ssh-keygen
cd ./code
```

### 03. Clone repository and run terraform as follow (Make sure you have terraform install).
```bash
git clone https://github.com/matanelg/AWS-Load-Balancer.git
cd AWS-Load-Balancer
terraform apply -auto-approve
```




