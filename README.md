# reusable-workflows-tester

CI & other tests for the reusable-workflows repo

## Overview

This repository serves as a test harness for validating the [reusable-workflows](https://github.com/CalebSargeant/reusable-workflows) repository. It includes:

- Python package with sample code for testing
- Comprehensive CI/CD workflows
- Docker container builds
- Linting, testing, and type checking
- Automated dependency updates

## Repository Dispatch Integration

This repository is designed to receive `repository_dispatch` events from the reusable-workflows repository. When a PR is opened in the reusable-workflows repo, it can trigger CI checks here to validate that the workflows function correctly.

### Setting up Repository Dispatch

To enable repository dispatch from the reusable-workflows repo:

1. **Create a Personal Access Token (PAT)** or use GitHub App authentication:
   - Go to GitHub Settings → Developer settings → Personal access tokens → Fine-grained tokens
   - Create a token with `contents: read` and `actions: write` permissions for this repository

2. **Add the token as a secret** in the reusable-workflows repository:
   - Repository Settings → Secrets and variables → Actions
   - Add a new secret named `DISPATCH_TOKEN`

3. **Use the dispatch in your workflow**:
```yaml
- name: Trigger tests in reusable-workflows-tester
  uses: peter-evans/repository-dispatch@v3
  with:
    token: ${{ secrets.DISPATCH_TOKEN }}
    repository: CalebSargeant/reusable-workflows-tester
    event-type: run-ci-tests
    client-payload: |
      {
        "ref": "${{ github.head_ref }}",
        "pr_number": "${{ github.event.pull_request.number }}",
        "run_number": "${{ github.run_number }}"
      }
```

### Dispatch Event Types

This repository responds to the following dispatch event types:
- `run-ci-tests`: Runs the full CI pipeline (lint, test, docker build)
- `test-reusable-workflow`: Alternative event type for workflow testing

## Development

### Prerequisites

- Python 3.11+
- Docker (for container builds)

### Setup

```bash
# Install dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov

# Run linter
ruff check src/ tests/

# Run type checker
mypy src/
```

### Docker Build

```bash
# Build using docker bake
docker buildx bake -f docker-bake.hcl

# Build development container
docker buildx bake -f docker-bake.hcl test-container-dev

# Run tests in container
docker run --rm ghcr.io/calebsargeant/reusable-workflows-tester:dev
```

## CI/CD Workflows

### test-container.yml
Main CI workflow that runs:
- Code linting (Ruff)
- Type checking (MyPy)
- Unit tests (pytest) on multiple Python versions
- Docker container builds
- Status reporting for repository dispatch events

Triggered by:
- Repository dispatch events from reusable-workflows
- Pull requests
- Pushes to main/master
- Manual workflow dispatch

### repository-dispatch-handler.yml
Logs and handles repository dispatch events, providing visibility into the integration between repositories.

## Dependabot

Automated dependency updates are configured for:
- Python dependencies (weekly)
- GitHub Actions (weekly)
- Docker base images (weekly)

## License

MIT
