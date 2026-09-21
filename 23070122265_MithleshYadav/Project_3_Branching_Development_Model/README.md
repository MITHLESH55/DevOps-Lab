# Project 3 - Branching Development Model

## Objective
Build a Git branching model for faster team development and code integration.

## Branching Model

```text
main
  |
  +-- develop
      +-- feature/login
      +-- feature/dashboard
          +-- release/v1.0
              +-- main

main
  |
  +-- hotfix/security-fix
      +--> main
      +--> develop
```

## Branches Used

- main
- develop
- feature/login
- feature/dashboard
- release/v1.0
- hotfix/security-fix

## Workflow

1. Create feature branches from develop.
2. Merge completed features into develop.
3. Create a release branch from develop.
4. Merge the release into main.
5. Create hotfix branches from main.
6. Merge hotfixes into main and develop.

## Result

The Git branching model was successfully implemented and pushed to GitHub.
