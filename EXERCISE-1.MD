# EXERCISE-1.MD
- [EXERCISE-1.MD](#exercise-1md)
  - [Test plan](#test-plan)
    - [Core features](#core-features)
    - [Non functional tests](#non-functional-tests)
  - [Test strategy](#test-strategy)
  - [Test accounts](#test-accounts)
    - [Compatibility tests](#compatibility-tests)
      - [Out of scope](#out-of-scope)
    - [Test data](#test-data)

This page covers the test plan.

## Test plan

Web app targeted for testing: https://www.saucedemo.com/

### Core features

The following features features are in scope:

- Log in
- Log out
- Product filtering
- Product listing page
- Product details page
- Cart
- Checkout
- Social media links

### Non functional tests

* performance: web app performs at a high level across all screens & interactions
* usability: minimal or zero UI issues are encountered during user sessions

## Test strategy

* automated: create automated tests covering each of the features in scope, focusing on functionality & state management behaviour
* manual: run exploratory tests with different users across each of the features in scope, focusing on non-functional & graphical behaviour

## Test accounts

* use `standard_user` to login as a user with default app & user state
* use `locked_out_user` to login as a user that's locked
* use `problem_user` to login with several functionality defects
* use `performance_glitch_user` to login as a user with lower-spec network conditions
* use `error_user` to login with several functionality defects
* use `visual_user` to login with several UI defects

### Compatibility tests

* Tests will be targeted to run on Chrome, Firefox & Safari.

#### Out of scope

* mobile or tablet device covergae

### Test data

* user accounts have been provided on login page
* products are available once logged in
* no end user ability to update/create/delete products