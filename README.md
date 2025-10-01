# challenge-playwright-python

[![Run playwright tests](https://github.com/alexandlazaris/challenge-playwright-python/actions/workflows/run-tests.yml/badge.svg)](https://github.com/alexandlazaris/challenge-playwright-python/actions/workflows/run-tests.yml)

- [challenge-playwright-python](#challenge-playwright-python)
  - [Dependencies](#dependencies)
  - [Setting up env](#setting-up-env)
  - [Running tests](#running-tests)
  - [Workflows](#workflows)
  - [Wrapping up](#wrapping-up)

## Dependencies

- python3, pip
- https://playwright.dev/python/docs/intro

## Setting up env

Development has been performed within a virtual python environment, isolating impact and dependencies from the host system.

1. clone the repo
2. run `python3 -m venv venv` to create a virtual env
3. run `source venv/bin/activate` to activate the virtual env
4. run `pip install ./requirements.txt` to install all python dependencies

## Running tests

* `pytest` -> cli output only, runs on 1 headless browser
* `pytest --html=report.html --self-contained-html` -> generate html report
* `pytest --tracing on` -> run with tracing to view test step breakdown and logs during execution
* `pytest --headed --browser webkit --browser firefox --browser chromium` -> runs headed on all browsers 
* append `--video on` to the run command to capture video recordings of each test

## Workflows

For each PR raised, there is a workflow to run all tests and for 2 artficats to be stored stored post-completion:
1. video recording of tests
2. html report of test suite

## Wrapping up

Run `deactivate` in your cli tab running this repo to exit the venv.