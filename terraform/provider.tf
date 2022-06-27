provider "google" {
  project     = "yolo52"
  region      = "us-central1"
  zone        = "us-central1-c"
  credentials = file("terraform/yolo52-922327199c2c.json")
}