// Docker Bake file for building test containers
// https://docs.docker.com/build/bake/

variable "TAG" {
  default = "latest"
}

variable "REGISTRY" {
  default = "ghcr.io"
}

variable "IMAGE_NAME" {
  default = "calebsargeant/reusable-workflows-tester"
}

group "default" {
  targets = ["test-container"]
}

target "test-container" {
  context = "."
  dockerfile = "Dockerfile"
  tags = [
    "${REGISTRY}/${IMAGE_NAME}:${TAG}",
    "${REGISTRY}/${IMAGE_NAME}:latest"
  ]
  platforms = ["linux/amd64", "linux/arm64"]
  labels = {
    "org.opencontainers.image.source" = "https://github.com/CalebSargeant/reusable-workflows-tester"
    "org.opencontainers.image.description" = "Test container for reusable-workflows CI/CD validation"
    "org.opencontainers.image.licenses" = "MIT"
  }
}

target "test-container-dev" {
  inherits = ["test-container"]
  tags = [
    "${REGISTRY}/${IMAGE_NAME}:dev"
  ]
  platforms = ["linux/amd64"]
}
