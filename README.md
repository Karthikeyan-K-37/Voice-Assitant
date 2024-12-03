# SayAI RAG (Retrieval-Augmented Generation)

## Overview

SayAI RAG is a Python-based project designed to implement Retrieval-Augmented Generation (RAG) workflows for efficient data retrieval and processing. It leverages vector-based search capabilities, utilities for text splitting, and a streamlined pipeline for query handling.

## Features

- **Vector Store Integration**: Utilizes `Milvus` for storing and retrieving vector embeddings.
- **Text Splitting**: Tools to segment documents into smaller chunks for improved retrievability.
- **Search Capabilities**: Implements efficient search algorithms for retrieving relevant data.
- **Agent Logic**: Handles query workflows and combines retrieval with generation.
- **Configurable Environment**: Provides customizable configurations via `.env` and `.env.example` files.

---

## File Structure

```plaintext
sayvai_rag/
├── __pycache__/          # Compiled Python files
├── __init__.py           # Initialization file for the package
├── agent.py              # Core logic for handling RAG workflows
├── config.py             # Configuration management for the application
├── milvus_vector_store.py # Vector database integration with Milvus
├── search.py             # Search functionality for data retrieval
├── text_splitter.py      # Tools for splitting and processing text
├── utils.py              # Utility functions
Scripts/
├── activate.bat          # Script to activate the environment
.env                       # Environment variables for configuration
.env.example               # Example environment file
.gitignore                 # Specifies files to ignore in version control
sayvai.db                  # SQLite database for storing local data
sayvai.db.lock             # Lock file for database management
app.py                     # Entry point for running the application
install.bat                # Batch script for project setup
poetry.lock                # Dependency lock file (Poetry)
pyproject.toml             # Dependency and project configuration
README.md                  # Project documentation (this file)
run.bat                    # Batch script to run the application
