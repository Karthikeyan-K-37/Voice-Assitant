# Multi-Tenant RAG

Multi-Tenant RAG (Retrieval-Augmented Generation) is a Python-based project designed to implement RAG workflows for multi-tenant architectures. It combines vector-based search, efficient data retrieval, and intelligent query handling tailored for multi-tenancy.

## Documentation

The project is organized into several key areas. Refer to the links below for detailed information:

- [Overview](docs/Overview.md)
- [Installation](docs/Installation.md)
- [Set Up Environment Variables](docs/SetUpEnvironment.md)
- [Install Dependencies](docs/InstallDependencies.md)
- [Verify Milvus](docs/VerifyMilvus.md)
- [Usage](docs/Usage.md)
- [Configuration](docs/Configuration.md)
- [File Structure](docs/FileStructure.md)
- [Contributing](docs/Contributing.md)
- [License](docs/License.md)

# Overview

Multi-Tenant RAG is a system designed to provide efficient and scalable solutions for retrieval-augmented generation in multi-tenant environments. It supports:

- **Multi-Tenant Architecture**: Isolates data and logic for each tenant.
- **Vector-Based Search**: Uses `Milvus` for storing and retrieving embeddings.
- **Document Splitting**: Automatically segments documents for better retrieval.
- **Extensible Design**: Easily integrates new features or external APIs.

---

## Key Features

1. **Tenant Isolation**: Ensures secure and separate data handling for each tenant.
2. **Search Optimization**: Implements efficient search for large datasets.
3. **Scalable Storage**: Utilizes Milvus for handling large-scale vector data.
4. **Customizable Configurations**: `.env` file for environment-specific settings.



---
# Installation

Follow these steps to set up and install Multi-Tenant RAG.

---

## Prerequisites

1. **Python**: Version 3.8 or above
2. **Poetry**: Dependency management tool
3. **Milvus**: Vector database (ensure it is installed and running)
4. **SQLite**: Pre-installed with Python, used for lightweight database management.

---

## Steps

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd muti-tenant-rag
---
# Set Up Environment Variables

Follow these steps to configure the environment for Multi-Tenant RAG:

---
## Steps

1. **Copy the Example Environment File**:
   ```bash
   cp .env.example .env

# Install Dependencies

To install the required dependencies for Multi-Tenant RAG, follow these steps:

---

## Steps

1. **Install Dependencies Using Poetry**:
   ```bash
   poetry install

# Verify Milvus Setup

Milvus is a critical component for the vector-based retrieval system in Multi-Tenant RAG. Ensure it is installed and running.

---

## Steps

1. **Start the Milvus Server**:
   ```bash
   milvus-server start

# Usage

Follow these steps to run the Multi-Tenant RAG application.

---

## Run the Application

1. **Using the Batch Script** (Windows):
   ```bash
   ./run.bat

# Contributing

We welcome contributions to Multi-Tenant RAG! Follow the guidelines below to get started.

---

## Steps to Contribute

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch-name

