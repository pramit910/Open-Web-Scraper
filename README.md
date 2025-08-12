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


##### Best Code Practices for Code Maintainability & Scalability

1. Modular Code Design
2. Use Configuration Files where needed (yaml & jsons as needed with hyperparameters as needed)
3. Automate testing with pytest or similar frameworks
4. Version control with Git
5. Document thoroughly


##### Sample Repository Structure for GenAI projects

├── .github/                   # GitHub-specific files (e.g., actions, workflows)
├── notebooks/                 # Jupyter notebooks for experiments and analysis
├── docs/                      # Project documentation
├── project/
│   ├── agents/                # Agent logic and orchestration
│   ├── prompt/                # Prompt engineering logic
│   ├── llms/                  # Large language model integration
│   ├── embeddings/            # Embedding generation and handling
│   ├── vectordatabase/        # Vector database operations
│   ├── tools/                 # Custom tools for tasks (e.g., web scraping, calculators)
│   ├── memory/                # Memory management for agent context
│   ├── callbacks/             # Custom callbacks for training, generation, etc.
│   ├── utils/                 # Utility functions
│   ├── telemetry/             # Monitoring and logging
│   ├── config/                # Configuration files for models, data, and tools
│   ├── data_loaders/          # Data loading and preprocessing scripts
│   ├── retrievers/            # Retrieval logic for search or information fetching
│   ├── reranker/              # Reranking algorithms for retrieved results
│   ├── main.py                # Main entry point for running the project
├── logs/                      # Training and experiment logs
├── tests/                     # Unit tests and integration tests
├── Dockerfile                 # Dockerfile for containerization
├── .gitignore                 # Git ignore file for excluding files from version control
├── LICENSE                    # License file
├── README.md                  # Project overview and instructions
├── Makefile                   # Makefile for project automation
├── pyproject.toml             # Project metadata and dependencies (for Poetry or modern Python projects)


