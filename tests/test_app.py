# tests/test_app.py

import pytest
from app.main import app  # Assuming your main FastAPI file is app/main.py

def test_app_import():
    """
    A simple test to ensure the FastAPI application object can be imported.
    This acts as a basic sanity check.
    """
    assert app is not None
```*(**Note:** You may need to adjust the `from app.main import app` line if your main application file is located elsewhere.)*

#### **Step 3: Update the `validate-stack.yml` Workflow**

We need to make one small change to our CI workflow to ensure it can find the `app` code when running tests.

Edit `.github/workflows/validate-stack.yml` and modify the "Run tests" step:

```yaml
# In .github/workflows/validate-stack.yml

      # ... (previous steps) ...

      - name: Run tests and generate coverage report
        # We add a PYTHONPATH environment variable so the test runner can find the 'app' module.
        run: |
          docker compose run --rm \
            -e PYTHONPATH=/app \
            webapp pytest --cov=app --cov-report=xml tests/
