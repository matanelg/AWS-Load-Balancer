provider "aws" {
  region = var.aws_region
}

terraform {
  required_providers {
    tls = {
      source = "hashicorp/tls"
      version = "3.1.0"
    }
  }
}

provider "tls" {

}

