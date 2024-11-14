# Stockholm Ransomware Simulation

This script simulates a ransomware attack by encrypting files in a specified directory and providing functionality to decrypt them with a given key.

## Modules

- `os`: Provides a way of using operating system dependent functionality.
- `sys`: Provides access to some variables used or maintained by the interpreter.
- `argparse`: Provides a command-line argument parsing functionality.
- `cryptography.fernet`: Implements symmetric encryption using the Fernet algorithm.

## Functions

- `generate_key()`: Generates a new Fernet encryption key.
- `load_key(key)`: Loads a Fernet encryption key.
- `encrypt_file(file_path, fernet)`: Encrypts a file using the provided Fernet key.
- `decrypt_file(file_path, fernet)`: Decrypts a file using the provided Fernet key.
- `parse_args()`: Parses command-line arguments.
- `main()`: Main function to handle encryption and decryption based on command-line arguments.

## Usage

### To encrypt files:
```sh
python stockholm.py
```

### To decrypt files:
```sh
python stockholm.py --reverse <encryption_key>
```

### Additional options:
- `-v, --version`: Show version information.
- `-s, --silent`: Run without output.

## Makefile

### Variables
- `PYTHON = python3`
- `SCRIPT = stockholm.py`

### Default target
```makefile
all: run
```

### Run the program
```makefile
run:
    $(PYTHON) $(SCRIPT)
```

### Show help
```makefile
help:
    $(PYTHON) $(SCRIPT) --help
```

### Show version
```makefile
version:
    $(PYTHON) $(SCRIPT) --version
```

### Reverse encryption (requires KEY argument)
```makefile
reverse:
    @echo "Usage: make reverse KEY=<your-key-here>"
    @echo "Example: make reverse KEY=your_generated_key"
```

### Reverse run
```makefile
reverse_run:
    $(PYTHON) $(SCRIPT) --reverse $(KEY)
```

### Silent run
```makefile
silent:
    $(PYTHON) $(SCRIPT) --silent
```

### Phony targets
```makefile
.PHONY: all run help version reverse reverse_run silent
```