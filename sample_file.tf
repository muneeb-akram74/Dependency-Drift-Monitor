module "web_server" {
    source  = "terraform-aws-modules/ec2-instance/aws"
    version = "3.0.0"  
}
module "database" {
    source  = "terraform-aws-modules/rds/aws"
    version = "3.20.0"  
}
