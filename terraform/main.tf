provider "aws" {
  region = "us-east-1"
}
variable "region" {
  default = "eu-west-2"
}

variable "ami" {
  default = "ami-06178cf087598769c"
}


resource "aws_key_pair" "citadel-key" {
  public_key = file("/root/terraform-challenges/project-citadel/.ssh/ec2-connect-key.pub")
  key_name   = "citadel"
}

resource "aws_instance" "citadel-instance" {
  ami           = var.ami
  key_name      = aws_key_pair.citadel-key.key_name
  instance_type = "m5.large"
  user_data     = file("/root/terraform-challenges/project-citadel/install-nginx.sh")
}
resource "aws_eip" "citadel-eip" {
  instance = aws_instance.citadel-instance.id
  vpc      = true
  provisioner "local-exec" {
    command = "echo ${aws_eip.citadel-eip.public_dns} >> /root/citadel_public_dns.txt"
  }
}

