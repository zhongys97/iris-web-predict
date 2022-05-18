# Overview

This app, based on Flask, predicts the flower species of the iris dataset.


# To Deploy on AWS

1. Launch an AWS EC2 instance (Linux 2 AMI t2.micro). Besides the default SSH access, add new security group with HTTP TCP anywhere for IPv4 (and IPv6).
2. In the terminal, SSH into the EC2 instance. Run `sudo yum update`
3. `sudo yum install docker`
4. `sudo systemctl start docker` to start the Docker Daemon
5. `sudo usermod -a -G docker ec2-user` to allow using Docker commands without the `sudo` keyword afterwards.
6. In a separate terminal, copy the local repo to EC2 via `scp -i YOUR_KEY_PAIR_PEM_FILE -r iris-web-predict  ec2-user@YOUR_PUBLIC_DNS:/home/ec2-user` (Assuming the PEM file and the iris-web-predict directory are in the same directory). In the first terminal, confirm a new directory `iris-web-predict` is created.
7. In the first terminal, cd into `iris-web-predict` and run `docker build -t iris-flask`.
8. Set an an instance of the container: `docker run -p 80:80 iris-flask`
9. Identify the public IPv4 address of the EC2 instance, and open in browser.



# To Deploy Locally

1. Start Docker Daemon
2. In the terminal, cd to the directory, run `docker build -t iris-flask`.
3. Set an an instance of the container: `docker run -p 80:80 iris-flask`
4. Open web browser: `http://127.0.0.1`. The default port of http is already 80.