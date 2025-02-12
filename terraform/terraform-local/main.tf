terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.0"
    }
  }
}

provider "local" {}

# Create a local file
resource "local_file" "hello_file" {
  filename = "${path.module}/hello.txt"
  content  = "Hello, World! Created by Terraform."
}

# Run a local shell script
resource "null_resource" "run_script" {
  provisioner "local-exec" {
    command = "bash ${path.module}/script.sh"
  }

  depends_on = [local_file.hello_file]
}
