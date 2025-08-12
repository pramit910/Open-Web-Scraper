# Open-Web-Scraper
A Web Scraping Application that can scrape anything


### Knowledge

##### Compile requirements from pyproject.toml to requirements.txt:

1. Method 1: using uv compiler
        
        `uv pip compile pyproject.toml -o requirements.txt`

2. Method 2: Using toml-to-requirements

        pip install toml-to-requirements

        toml-to-req --toml-file pyproject.toml -o requirements.txt

3. Method 3: Using poetry Built in export functionality

        poetry export -f requirements.txt --output requirements.txt --without-hashes