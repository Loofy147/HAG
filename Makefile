.PHONY: test validate clean

# Automated Testing
test:
	python3 -m unittest discover tests/

# Final Validation
validate:
	python3 scripts/manifold_stability_test.py

# Cleanup
clean:
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name "*.pyc" -delete
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf data/legal data/finance data/events data/cern

# Setup Environment
setup:
	pip install -r requirements.txt
	pip install .

# Full Build & Validate
build: clean setup test validate
