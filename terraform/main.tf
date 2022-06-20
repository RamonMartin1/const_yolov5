resource "google_storage_bucket" "bucket" {
  name     = "test-bucket"
  location = "US"
}

resource "google_storage_bucket_object" "archive" {
  name   = "Archive.zip"
  bucket = google_storage_bucket.bucket.name
  source = "./pysrc/Archive.zip"
}

resource "google_cloudfunctions_function" "yolo" {
  name        = "yolo"
  description = "yolo detector"
  runtime     = "python38"

  available_memory_mb   = 1024
  source_archive_bucket = google_storage_bucket.bucket.name
  source_archive_object = google_storage_bucket_object.archive.name
  trigger_http          = true
  timeout               = 60
  entry_point           = "main"
  labels = {
    my-label = "my-label-value"
  }

  environment_variables = {
    MY_ENV_VAR = "my-env-var-value"
  }
}

# IAM entry for a single user to invoke the function
resource "google_cloudfunctions_function_iam_member" "invoker" {
  project        = google_cloudfunctions_function.function.project
  region         = google_cloudfunctions_function.function.region
  cloud_function = google_cloudfunctions_function.function.name

  role   = "roles/cloudfunctions.invoker"
  member = "user:myFunctionInvoker@example.com"
}
