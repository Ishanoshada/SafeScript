# SafeScript v1.0.2

![Python Version](https://img.shields.io/badge/python-3.9-blue.svg)

SafeScript is a Python module designed to enhance the security of web applications by providing various functions to prevent common security vulnerabilities such as XSS and SQL Injection attacks.

## Features

- **sanitize_html**: Sanitize HTML content to prevent XSS attacks.
- **escape_html**: Escape special characters in HTML content.
- **sanitize_sql**: Sanitize SQL input to prevent SQL Injection attacks.
- **prevent_xss_and_sqli**: Prevent both XSS and SQL Injection attacks.

## Installation

You can install SafeScript using pip:

```bash
pip install safescript
```

## Usage

```python
from safescript import SafeScript

# Example Usage
input_data = "<script>alert('XSS Attack')</script>"
output = SafeScript.prevent_xss_and_sqli(input_data)
print(output)
```

## Functions

- **sanitize_html(input_html)**
   - Sanitize HTML content to prevent XSS attacks.

- **escape_html(input_html)**
   - Escape special characters in HTML content.

- **sanitize_sql(input_sql)**
   - Sanitize SQL input to prevent SQL Injection attacks.

- **prevent_xss_and_sqli(input_data)**
   - Prevent both XSS and SQL Injection attacks.

## Version History

- v1.0.2 (Current Version)
    - [List of changes in v1.0.2]

- v1.0.1
   - Initial release with basic security functions.

**Repository Views** ![Views](https://profile-counter.glitch.me/safescript/count.svg)

 
## Contributors

- [Ishan Oshada](https://github.com/ishanoshada)

