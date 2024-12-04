# Multi-Tenant RAG

Multi-Tenant RAG (Retrieval-Augmented Generation) is a Python-based project designed to implement RAG workflows for multi-tenant architectures. It combines vector-based search, efficient data retrieval, and intelligent query handling tailored for multi-tenancy.

## Documentation

The project is organized into several key areas. Refer to the links below for detailed information:

- [Overview](docs/Overview.md)
- [Installation](docs/Installation.md)
- [Usage](docs/Usage.md)
- [Configuration](docs/Configuration.md)
- [File Structure](docs/FileStructure.md)
- [Contributing](docs/Contributing.md)
- [License](docs/License.md)

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
# Install Dependencies

To install the required dependencies for Multi-Tenant RAG, follow these steps:

---

## Steps

1. **Install Dependencies Using Poetry**:
   - If Poetry is already installed:
     ```bash
     poetry install
     ```

2. **Run Initialization Script** (Windows):
   - Use the batch script to initialize:
     ```bash
     ./install.bat
     ```

---

## Notes

- Ensure that Python and Poetry are properly installed and added to your system's PATH.
- If you encounter errors, verify your Python version (3.8 or above) and retry the installation.

  # Verify Milvus Setup

Milvus is a critical component for the vector-based retrieval system in Multi-Tenant RAG. Ensure it is installed and running.

---

## Steps

1. **Start the Milvus Server**:
   ```bash
   milvus-server start

