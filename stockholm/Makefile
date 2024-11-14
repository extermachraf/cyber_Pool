# Makefile for Stockholm Ransomware Simulation

# Variables
PYTHON = python3
SCRIPT = stockholm.py

# Default target
all: run

# Run the program
run:
	$(PYTHON) $(SCRIPT)

# Show help
help:
	$(PYTHON) $(SCRIPT) --help

# Show version
version:
	$(PYTHON) $(SCRIPT) --version

# Reverse encryption (requires KEY argument)
reverse:
	@echo "Usage: make reverse KEY=<your-key-here>"
	@echo "Example: make reverse KEY=your_generated_key"


reverse_run:
	$(PYTHON) $(SCRIPT) --reverse $(KEY)

# Silent run
silent:
	$(PYTHON) $(SCRIPT) --silent

.PHONY: all run help version reverse reverse_run silent