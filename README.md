# 🎭 Polako E2E & API Automation Testing Framework

[![Python](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/playwright-v1.49+-green.svg)](https://playwright.dev/python/)
[![pytest](https://img.shields.io/badge/pytest-v8.0+-purple.svg)](https://docs.pytest.org/)
[![Allure](https://img.shields.io/badge/allure-framework-orange.svg)](https://github.com/allure-framework)

This repository contains a comprehensive **E2E and API automation testing framework** built for the **Polako** web platform. 

This is a **collaborative team project** developed by a team of QA Automation Engineers. The framework is engineered using the **Page Object Model (POM)** pattern to ensure high scalability, clean code separation, and reliable parallel test execution.

---

## 👥 Team Collaboration & Git Workflow

This framework is built and maintained as a team effort. To ensure high code quality and prevent conflicts in our automated suites, we follow a strict enterprise Git workflow:
* **Branch Strategy:** Feature development takes place in isolated `feature/*` or `fix/*` branches, which are then integrated into the main `develop` branch via Pull Requests.
* **Code Reviews:** Every PR undergoes peer code reviews to ensure alignment with our framework patterns and locator strategies.
* **Shared Infrastructure:** The team works against a shared staging environment, leveraging robust authorization mechanisms to run tests concurrently without session cross-contamination.

---

## 🎯 Test Coverage & Scope

Our automated test suite is divided into layered functional areas to ensure comprehensive coverage across both UI and API layers:

### 🛡️ 1. Authentication & User Management
* **Registration Flows:** Positive manager and organizer registrations, validation for existing emails, and handling invalid enterprise data.
* **Authentication:** Secure UI login validation, boundary testing for malformed emails, and password recovery workflows (`forgot_password`).
* **Profile & Security:** Comprehensive coverage of the User Profile area including full/partial data updates, field validation, and secure password changes (verifying match and strength rules).

### 📅 2. Event Management & E2E Checkout
* **Event Creation & Lifecycle:** Validating event generation, multi-step editing, preview generation in isolated browser contexts, and deletion protocols.
* **Ticket Selection & Cart:** End-to-end purchasing simulations (covering specific ticket variants like `test`, `testo123`, and `test321`), validating real-time cart inclusion, and verifying checkout countdown visibility.

### ⚙️ 3. API Integration Layer
* **Token Management:** Isolated API clients (e.g., `AuthApi`) to generate and handle session tokens, skipping expensive UI steps for preconditions.

---

## 📐 Architecture & Framework Design

The framework enforces a strict separation between test definitions and UI structural layouts:

1. **`BasePage`:** Standardized wrapper class encapsulating low-level Playwright interactions (`click`, `fill`, visibility checks), providing reliable element waiting mechanisms.
2. **`Page Objects`:** (e.g., `UserProfilePage`, `RegistrationPage`) High-level page representations mapping exact UI locators and chainable business flows.
3. **`BaseTest` & Fixtures:** Central test class executing automated fixture-driven page initializations. 
4. **Cookie Authentication:** To guarantee execution speed, tests inherit from `BaseUserTest` or `BaseManagerTest`. These automatically bypass standard UI login forms by injecting API-generated authorization tokens directly into the browser context cookies.

```text
TP_Polako_E2E/
│
├── api/                        # API clients for rapid authentication & setup
├── base/
│   ├── base_page.py            # Playwright wrappers and low-level interactions
│   └── base_test.py            # Fixture setups, page initializations, and cookie injection
│
├── pages/                      # Page Object Model (POM) layer
│   ├── auth/                   # Login, Registration, and Forgot Password structures
│   ├── events/                 # Event list, creation, editing, and preview pages
│   └── profile/                # User and Manager profile panels
│
└── tests/                      # Scalable Test Suites (UI & API validation)
    ├── test_login.py
    ├── test_registration.py
    └── test_user_profile.py
