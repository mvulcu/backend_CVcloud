
# Cloud Storage bucket for Cloud Function code
resource "google_storage_bucket" "cloud_function_bucket" {
  name          = "${var.bucket_name}_vulcu" 
  location      = var.region
  force_destroy = true
  storage_class = "REGIONAL"
}

# Cloud Function
resource "google_cloudfunctions_function" "current_number_visitors" {
  name                  = "current_number_visitors"
  runtime               = "python39"
  available_memory_mb   = 128
  timeout               = 60
  entry_point           = "current_number_visitors"
  source_archive_bucket = google_storage_bucket.cloud_function_bucket.name
  source_archive_object = var.zip_file
  trigger_http          = true
  project               = var.project
  region                = var.region
}

# Public access to the Cloud Function
resource "google_cloudfunctions_function_iam_member" "public_access_current_number_visitors" {
  project        = var.project
  region         = var.region
  cloud_function = google_cloudfunctions_function.current_number_visitors.name
  role           = "roles/cloudfunctions.invoker"
  member         = "allUsers"
}
