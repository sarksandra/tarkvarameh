name: python-ci
on: [push]
jobs:
  build:
    runs-on:ubuntu-latest

  steps:
    -uses: actions/checkout@v2
    -name: pythonei instalerimine
    -uses: actions/setup-pytjon@v2
    with:
      pythone-version: 3.9

      -name: installida Dependencies:
      run: pytest

    
