# API Testing with Requests

## Overview
This repository contains automated tests for API validation using the Python `requests` library and `pytest`. The project is designed to test RESTful API endpoints for functionality, correctness, and response validation.

## Features
- Automated API testing using `requests`
- Test case execution with `pytest`
- Response validation (status codes, response body, headers)
- Easy configuration for different API environments

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- `pip` (Python package manager)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/shobhitha/api_testing_requests.git
   ```
2. Navigate to the project directory:
   ```sh
   cd api_testing_requests
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running Tests
Execute the tests using `pytest`:
```sh
pytest -v
```
For specific test modules:
```sh
pytest tests/test_api.py
```

## Configuration
- API endpoints and configurations can be stored in a separate config file (`config.json` or `config.py`).
- Update headers and authentication details as required.

## Project Structure
```
api_testing_requests/
│-- tests/
│   ├── test_api.py       # API test cases
│   ├── utils.py          # Helper functions
│-- config.py             # API configurations
│-- requirements.txt      # Dependencies
│-- README.md             # Project documentation
```

## Contributing
Feel free to open issues or submit pull requests to enhance the project.

## License
This project is licensed under the MIT License.

---
**Author:** Shobhitha Sarma Dittakavi
