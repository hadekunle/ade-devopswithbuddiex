terraform {
  required_version = ">= 1.0.0"
}

locals {
  numbers = [for n in range(1, 11) : n]
}

output "numbers_1_to_10" {
  value = local.numbers
}
