provider "aws" {
  region = "us-east-1"
}
resource "aws_s3_bucket" "hello_bucket" {
  bucket = "hello-world-bucket"
  acl    = "private"
}