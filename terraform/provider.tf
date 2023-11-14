provider "google" {
  credentials = var.gcp_credentials
  project     = var.project
  region      = var.region
}
