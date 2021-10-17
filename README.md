# AWS-Load-Balancer

This repository comes to demonstrate how to serve applications on containers via aws load balancer.<br />
I used ansible for instances configuration and terraform for build the infrastructure As shown below.<br />

<p align="center">
  <img src="https://github.com/matanelg/AWS-Load-Balancer/blob/main/files/arc-00.png" width="100%" height="100%" />
</p>


## Application

The application build with docker-compose for scalability purpose as we create two replicas of container app's.<br />
One container run flask (python) as a web server and return to the client the instance hostname & container id.<br />
On the second container run nginx as reverse proxy and move traffic to flask from host.<br />
Combine together the apps replicas and nginx as a reverse proxy and we get internal load balancer.<br />


## Quick Start

### 01. Export your aws access key & secret key 
(Make sure the user have premission to creating resources).
```bash
export AWS_ACCESS_KEY=""
export AWS_SECRET_KEY=""
```

### 02. Create two ssh key-pair with the names public-instance & private-instance
```bash
ssh-keygen
ssh-keygen
```

### 03. Clone repository and run terraform as follow 
(Make sure you have terraform install).
```bash
git clone https://github.com/matanelg/AWS-Load-Balancer.git
cd AWS-Load-Balancer
terraform apply -auto-approve
```

## Demo
https://user-images.githubusercontent.com/64362937/137604710-ba174d43-2075-44cd-b807-3448c58d11a7.mp4


