# AWS DevOps Platform

**An end-to-end AWS DevOps project built with Python, FastAPI, Docker, Terraform, and GitHub Actions.**

## Project Overview

This project demonstrates the design and implementation of an AWS-hosted containerized application using Infrastructure as Code and automated CI/CD.

The application is a lightweight task-management REST API built with FastAPI. The main focus of the project is the DevOps engineering lifecycle: containerization, automated testing, cloud infrastructure provisioning, deployment, and monitoring.

**Status:** In development. The application and Docker image have been tested locally, and the initial AWS networking infrastructure has been deployed using Terraform.

## Technology Stack

| Area | Technology |
|---|---|
| Application | Python, FastAPI, Uvicorn |
| Testing | Pytest |
| Containerization | Docker |
| Cloud | AWS |
| Infrastructure as Code | Terraform |
| Version Control | Git, GitHub |
| CI/CD (planned) | GitHub Actions |
| Container Deployment (planned) | Amazon ECR, ECS Fargate |
| Networking (planned) | Application Load Balancer, private subnets |
| Database (planned) | Amazon RDS PostgreSQL |
| Monitoring (planned) | Amazon CloudWatch |

## Architecture

### Current Infrastructure

The initial AWS networking environment has been provisioned in the `eu-north-1` region.

- VPC: `10.0.0.0/16`
- Public subnet A: `10.0.1.0/24` (`eu-north-1a`)
- Public subnet B: `10.0.2.0/24` (`eu-north-1b`)
- Internet Gateway attached to the VPC
- Public route table with a default route to the Internet Gateway
- Explicit route table associations for both public subnets

The two public subnets provide the network foundation for a future internet-facing Application Load Balancer.

### Target Architecture

GitHub → GitHub Actions → Docker Build → Amazon ECR → ECS Fargate → FastAPI Application

The target deployment will also include an Application Load Balancer, private application networking, an RDS PostgreSQL database, and CloudWatch monitoring.

These components will be implemented incrementally.

## Application Functionality

The FastAPI application provides a simple task-management API.

Current endpoints include:

- `GET /health` — application health check
- `GET /tasks` — retrieve tasks
- `POST /tasks` — create a task
- `GET /tasks/{task_id}` — retrieve a task by ID

Tasks are currently stored in memory. Persistent storage is planned for a later phase.

## Running Locally

### Python

Create and activate a Python virtual environment, install dependencies, and start the FastAPI application with Uvicorn.

The interactive API documentation is available at:

`http://localhost:8000/docs`

### Docker

Build the image:

```bash
docker build -t task-api:1.0 .
```

Run the container:

```bash
docker run -d -p 8000:8000 --name task-api-container task-api:1.0
```

Test the health endpoint:

`http://localhost:8000/health`

## Terraform Infrastructure

Terraform is used to provision and manage AWS infrastructure.

The current configuration includes:

- VPC
- Public subnets across two Availability Zones
- Internet Gateway
- Public route table and default internet route
- Route table associations

Terraform provider configuration includes an allowed AWS account ID check to reduce the risk of deploying into the wrong account.

The account ID is supplied externally rather than hardcoded into the public repository.

### Validation

Infrastructure was validated using:

```bash
terraform fmt
terraform validate
terraform plan
terraform apply
```

Deployed resources were verified through the AWS Console. A subsequent `terraform plan` reported no changes, confirming that the infrastructure matched the Terraform configuration at the time of validation.

**Security note:** Terraform state files, local provider directories, and variable files containing sensitive values are excluded from version control.

## Challenges and Troubleshooting

### AWS Region and Service Control Policy Restrictions

An initial VPC deployment attempt was blocked by an AWS Organizations Service Control Policy.

Investigation showed that the AWS account's available deployment region was restricted. The Terraform provider was updated to use `eu-north-1`, after which the networking resources were successfully provisioned.

This provided practical experience in distinguishing IAM permissions from organization-level restrictions.

## Development Roadmap

- [x] Create FastAPI application
- [x] Implement basic API tests
- [x] Containerize application using Docker
- [x] Provision AWS VPC and public networking using Terraform
- [x] Publish project source code to GitHub
- [ ] Implement private subnets and security groups
- [ ] Configure Amazon ECR
- [ ] Deploy application to Amazon ECS Fargate
- [ ] Configure Application Load Balancer
- [ ] Integrate persistent database storage
- [ ] Automate testing and deployment using GitHub Actions
- [ ] Implement monitoring and logging
- [ ] Document deployment verification and architecture trade-offs

## Learning Objectives

This project is intended to demonstrate practical experience in:

- Managing cloud infrastructure through Terraform
- Understanding AWS networking and routing
- Building and running containerized applications
- Implementing automated testing and deployment workflows
- Applying infrastructure security and configuration management practices
- Troubleshooting real-world AWS deployment issues

The project will continue to evolve as additional infrastructure and CI/CD components are implemented.