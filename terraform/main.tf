resource "google_storage_bucket" "file_dump" {
  name     = "file-dump-bucket"
  location = "US"
}

resource "google_storage_bucket" "file_dump2" {
  name     = "file-dump-bucket2"
  location = "US"
}

resource "google_storage_bucket" "code_load" {
  name     = "code-load-bucket"
  location = "US"
}

resource "google_storage_bucket_object" "archive" {
  name   = "Archive.zip"
  bucket = google_storage_bucket.code_load.name
  source = "./pysrc/Archive.zip"
}

resource "google_cloudfunctions_function" "yolo" {
  name        = "yolo"
  description = "yolo detector"
  runtime     = "python38"

  available_memory_mb   = 2048
  source_archive_bucket = google_storage_bucket.code_load.name
  source_archive_object = google_storage_bucket_object.archive.name
  trigger_http          = true
  timeout               = 60
  entry_point           = "main"
  labels = {
    my-label = "my-label-value"
  }
  timeouts {
    create = "15m"
    {{{{
  }

  # environment_variables = {
  #   MY_ENV_VAR = "my-env-var-value"
  # }
}

# IAM entry for a single user to invoke the function
resource "google_cloudfunctions_function_iam_member" "invoker" {
  project        = google_cloudfunctions_function.yolo.project
  region         = google_cloudfunctions_function.yolo.region
  cloud_function = google_cloudfunctions_function.yolo.name

  role   = "roles/cloudfunctions.invoker"
  member = "user:rlew631@gmail.com"
}
