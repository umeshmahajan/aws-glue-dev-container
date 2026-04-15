# aws-glue-dev-container
# AWS Glue 5 Local Development Environment (Dev Container)

This repository provides a **local development environment for AWS Glue 5 jobs** using Docker, VS Code Dev Containers, and CI/CD integration.

It enables developers to:

* Develop and test Glue jobs locally using Spark
* Maintain consistent environments across teams
* Integrate with CI/CD pipelines (Jenkins)
* Deploy jobs to AWS via CloudFormation

---

# 🧭 Overview

AWS Glue is a serverless ETL service built on Apache Spark. This project uses the official Glue Docker image to replicate the Glue runtime locally.

👉 Benefits:

* Faster development (no need to deploy to AWS for every change)
* Lower cost (local testing)
* Easier debugging

---

# 📁 Project Structure

```
glue5-dev/
│
├── .devcontainer/             # VS Code dev container configuration
│   └── devcontainer.json
│
├── .vscode/                  # Workspace settings for developers
│   ├── settings.json
│   └── extensions.json
│
├── docker/                   # Docker setup for Glue 5 environment
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── src/                      # Source code for Glue jobs
│   ├── jobs/                 # Glue ETL job scripts
│   │   └── sample_job.py
│   │
│   └── common/               # Shared utilities
│       └── utils.py
│
├── tests/                    # Unit tests for Glue jobs
│   └── test_sample.py
│
├── cicd/                     # CI/CD pipeline configuration
│   ├── Jenkinsfile
│   └── scripts/
│       ├── package.sh        # Packages Glue code
│       └── upload_s3.sh      # Uploads artifacts to S3
│
├── infra/                    # Infrastructure as Code (CloudFormation)
│   ├── glue-job.yaml
│   └── params/
│       ├── dev.json
│       ├── qa.json
│       └── prod.json
│
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
```

---

# 📦 File-Level Explanation

## 🔹 .devcontainer/devcontainer.json

Defines the development container used by VS Code.

**Purpose:**

* Runs Glue Docker container inside VS Code
* Mounts workspace into container
* Configures Python interpreter

---

## 🔹 .vscode/settings.json

Workspace-specific VS Code settings.

**Contains:**

* Python interpreter path
* Spark/Glue library paths
* Linting & formatting config

---

## 🔹 .vscode/extensions.json

Recommended VS Code extensions.

**Includes:**

* Python
* Jupyter
* AWS Toolkit (optional)

---

## 🔹 docker/Dockerfile

Custom Glue 5 container definition.

**Purpose:**

* Extends official Glue image
* Installs dev tools (pytest, pandas, etc.)
* Sets working directory

---

## 🔹 docker/docker-compose.yml

Defines how the container runs.

**Key features:**

* Mounts project directory into container
* Mounts AWS credentials
* Exposes Spark UI ports

---

## 🔹 src/jobs/

Contains Glue ETL scripts.

**Example:**

* `sample_job.py`: PySpark / Glue job logic

---

## 🔹 src/common/

Shared reusable utilities.

**Examples:**

* Data transformation helpers
* Logging utilities

---

## 🔹 tests/

Unit tests for Glue jobs.

**Purpose:**

* Validate transformations
* Enable CI testing

---

## 🔹 cicd/Jenkinsfile

Defines Jenkins pipeline.

**Stages:**

1. Checkout code
2. Package job
3. Upload to S3
4. Deploy via CloudFormation

---

## 🔹 cicd/scripts/package.sh

Packages job code.

**Includes:**

* Copy job scripts
* Install dependencies

---

## 🔹 cicd/scripts/upload_s3.sh

Uploads artifacts to S3.

**Used in:**

* CI/CD pipeline

---

## 🔹 infra/glue-job.yaml

CloudFormation template to create Glue job.

**Defines:**

* Glue job
* IAM role
* Job parameters

---

## 🔹 infra/params/

Environment-specific configs.

| File      | Purpose                 |
| --------- | ----------------------- |
| dev.json  | Development environment |
| qa.json   | QA environment          |
| prod.json | Production environment  |

---

## 🔹 requirements.txt

Python dependencies used in Glue jobs.

---

# 🚀 Getting Started

## 1. Clone repository

```
git clone <repo-url>
cd glue5-dev
```

---

## 2. Start Dev Environment

### Option A: Docker

```
cd docker
docker compose up -d --build
docker exec -it glue5_dev bash
```

### Option B: VS Code Dev Container (Recommended)

* Open project in VS Code
* Press `Ctrl + Shift + P`
* Select **"Reopen in Container"**

---

## ▶️ Run Glue Job

```
spark-submit src/jobs/sample_job.py
```

---

## 🧪 Run Tests

```
pytest
```

---

# ☁️ AWS Configuration

Ensure AWS credentials exist locally:

```
~/.aws/credentials
~/.aws/config
```

These are mounted into the container.

---

# 🔄 CI/CD Flow

1. Developer pushes code
2. Jenkins pipeline triggers
3. Artifacts uploaded to S3
4. CloudFormation deploys Glue job

---

# 🌍 Multi-Environment Setup

| Branch    | Environment |
| --------- | ----------- |
| feature/* | dev         |
| develop   | dev         |
| release/* | qa          |
| main      | prod        |

---

# ⚠️ Limitations (Local Dev)

Not fully supported locally:

* Glue Data Catalog
* Job bookmarks
* Lake Formation permissions

---

# 🏆 Summary

This repository provides:

* Local Glue 5 development environment
* Docker + VS Code integration
* CI/CD pipeline with Jenkins
* Infrastructure as Code with CloudFormation
* Multi-environment deployment strategy

---

# 📚 References

* AWS Glue Docker Development Guide
* AWS Glue 5.0 Documentation

---

# 👨‍💻 Author

Maintained by Umesh Mahajan
