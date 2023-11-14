variable "project" {
  description = "The Google Cloud project ID"
  type        = string
}

variable "region" {
  description = "The Google Cloud region"
  type        = string
}

variable "gcp_credentials" {
  description = "Google Cloud credentials in JSON format"
  type        = string
}

variable "bucket_name" {
  description = "Name of the Google Cloud Storage bucket"
  type        = string
  default     = "cloudcv_function"
}

variable "zip_file" {
  description = "Name of the ZIP file containing the Cloud Function"
  type        = string
}
