import re

class SafeScript:
    @staticmethod
    def sanitize_html(input_html):
        """Sanitize HTML content to prevent XSS attacks."""
        clean_html = re.sub(r'<(script|iframe|object|embed|form|details|s).*?>.*?</\1>', '', input_html, flags=re.DOTALL | re.IGNORECASE)
        return clean_html

    @staticmethod
    def escape_html(input_html):
        """Escape special characters in HTML content."""
        return input_html.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#39;')

    @staticmethod
    def sanitize_and_escape(input_html):
        """Sanitize and escape HTML content."""
        return SafeScript.escape_html(SafeScript.sanitize_html(input_html))

    @staticmethod
    def sanitize_sql(input_sql):
        """Sanitize SQL input to prevent SQL Injection attacks."""
        return re.sub(r'[-\'";]', '', input_sql)

    

    @staticmethod
    def prevent_xss_and_sqli(input_data):
        """Prevent both XSS and SQL Injection attacks."""
        sanitized_html = SafeScript.sanitize_html(input_data)
        escaped_html = SafeScript.escape_html(sanitized_html)
        sanitized_sql = SafeScript.sanitize_sql(input_data)
        validated_input = SafeScript.validate_input(input_data)
        
        return {
            "sanitized_html": sanitized_html,
            "escaped_html": escaped_html,
            "sanitized_sql": sanitized_sql,
            "validated_input": validated_input
        }


