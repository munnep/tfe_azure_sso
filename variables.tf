variable "tag_prefix" {
  description = "default prefix of names"
}

variable "vnet_cidr" {
  description = "which private subnet do you want to use for the VPC. Subnet mask of /16"
}

variable "security_rules" {
  type = map(any)
  default = {
    dashboard = {
      port                  = 8800,
      source_address_prefix = "*",
      priority              = 100
    }
    tfe_app_https = {
      port                  = 443,
      source_address_prefix = "*",
      priority              = 101
    }
    tfe_app_http = {
      port                  = 80,
      source_address_prefix = "*",
      priority              = 102
    }
    tfe_postgresql = {
      port     = 5432,
      priority = 103
    }
    tfe_ssh = {
      port                  = 22,
      source_address_prefix = "*",
      priority              = 104
    }
    tfe_application_gateway = {
      port                  = "65200-65535",
      source_address_prefix = "*",
      priority              = 105
    }
  }
}