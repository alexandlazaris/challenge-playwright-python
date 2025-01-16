# challenge-playwright-python

Playwright UI tests against https://www.saucedemo.com/

- [challenge-playwright-python](#challenge-playwright-python)
  - [Dependencies](#dependencies)
  - [Setting up env](#setting-up-env)
  - [Running tests](#running-tests)
    - [Video](#video)
  - [Wrapping up](#wrapping-up)

## Dependencies

- python3
- pip
- mac
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

### Video
* append `--video on` to the run command to capture video recordings of each test

## Wrapping up

Run `deactivate` in your cli tab running this repo to exit the venv.