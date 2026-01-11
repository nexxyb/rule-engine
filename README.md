# Django Pluggable Rule Engine

This project demonstrates a small Django application implementing a **pluggable rule engine** that evaluates business rules against orders via a REST API.

The focus is on clean architecture, extensibility, and correctness.

---

## Features

- Django + Django REST Framework
- Order model with seeded data
- Pluggable rule engine using auto-registration
- Easily extensible rule design (no modification of existing code required)
- REST API endpoint for rule evaluation
- Unit and API test coverage

---


## Rule Engine Design

- Each rule is a class inheriting from `BaseRule`
- Rules implement a `check()` method returning `True` or `False`
- Rules are auto-registered using a decorator into a global registry
- New rules can be added without modifying existing code

---

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <repo-name>
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux / Mac
   # venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install django djangorestframework
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Seed example orders**
   ```bash
   python manage.py seed_orders
   ```

6. **Run the server**
   ```bash
   python manage.py runserver
   ```

---

## API Usage

### Endpoint

`POST /rules/check/`

### Request Body

```json
{
  "order_id": 1,
  "rules": ["min_total_100", "min_items_2"]
}
```

### Response

```json
{
  "passed": true,
  "details": {
    "min_total_100": true,
    "min_items_2": false
  }
}
```

---

## Running Tests

```bash
python manage.py test
```

