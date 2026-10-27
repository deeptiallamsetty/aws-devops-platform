terraform {
  required_version = ">= 1.16.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region  = "eu-north-1"
  profile = "devops-project"

  allowed_account_ids = [var.aws_account_id]
}