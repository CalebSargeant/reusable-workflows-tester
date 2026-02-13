# Example Workflow Snippet for reusable-workflows Repository

This is an example of how to trigger this test repository from the reusable-workflows repo.

## Setup Required in reusable-workflows Repo

1. Create a Personal Access Token (PAT) or GitHub App with the following permissions:
   - Repository: `CalebSargeant/reusable-workflows-tester`
   - Permissions: `contents: read` and `actions: write`

2. Add the token as a secret in the reusable-workflows repository:
   - Name: `DISPATCH_TOKEN`

## Workflow Example

Add this to a workflow in the reusable-workflows repository (e.g., `.github/workflows/pr-checks.yml`):

```yaml
name: PR Checks and Test Dispatch

on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  dispatch-tests:
    name: Trigger Tests in reusable-workflows-tester
    runs-on: ubuntu-latest
    steps:
      - name: Trigger test repository
        uses: peter-evans/repository-dispatch@v3
        with:
          token: ${{ secrets.DISPATCH_TOKEN }}
          repository: CalebSargeant/reusable-workflows-tester
          event-type: run-ci-tests
          client-payload: |
            {
              "ref": "${{ github.head_ref || github.ref }}",
              "pr_number": "${{ github.event.pull_request.number }}",
              "run_number": "${{ github.run_number }}",
              "sha": "${{ github.event.pull_request.head.sha }}",
              "repository": "${{ github.repository }}",
              "sender": "${{ github.event.sender.login }}"
            }

      - name: Log dispatch
        run: |
          echo "Dispatched tests to reusable-workflows-tester"
          echo "PR: #${{ github.event.pull_request.number }}"
          echo "Ref: ${{ github.head_ref || github.ref }}"
```

## Alternative: Using workflow_dispatch

If you prefer to manually trigger tests or want more control:

```yaml
name: Manual Test Trigger

on:
  workflow_dispatch:
    inputs:
      ref:
        description: 'Ref to test in reusable-workflows-tester'
        required: false
        default: 'main'

jobs:
  dispatch-tests:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger test repository
        uses: peter-evans/repository-dispatch@v3
        with:
          token: ${{ secrets.DISPATCH_TOKEN }}
          repository: CalebSargeant/reusable-workflows-tester
          event-type: run-ci-tests
          client-payload: |
            {
              "ref": "${{ github.event.inputs.ref }}",
              "run_number": "${{ github.run_number }}",
              "repository": "${{ github.repository }}"
            }
```

## Monitoring the Results

After dispatching, you can:

1. Visit the [Actions tab](https://github.com/CalebSargeant/reusable-workflows-tester/actions) in this repository
2. Look for workflow runs triggered by `repository_dispatch`
3. Check the `Repository Dispatch Handler` workflow for event details
4. Check the `Test Container CI` workflow for actual test results

## Event Types

This repository responds to the following event types:
- `run-ci-tests`: Runs the full CI pipeline (lint, test, docker build)
- `test-reusable-workflow`: Alternative event type for testing
