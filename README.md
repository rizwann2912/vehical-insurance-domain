# MLOps Vehicle Insurance Data Pipeline 🚗📊

Built a comprehensive MLOps project focusing on vehicle insurance data with end-to-end automation and cloud deployment. This project demonstrates modern ML engineering practices with real-world data management and production-ready deployment.

## Project Overview 🛠️

Created a complete machine learning pipeline that processes vehicle insurance data with automated CI/CD deployment on AWS. The architecture includes data ingestion, validation, transformation, model training, evaluation, and deployment components.

## Getting Started 🚀

### Project Structure Setup
Executed `template.py` to generate the project structure with organized folders and configuration files.

### Package Configuration
Configured local package imports through `setup.py` and `pyproject.toml` files. Reference `crashcourse.txt` for detailed explanations.

### Environment Setup
```bash
conda create -n vehicle python=3.10 -y
conda activate vehicle
pip install -r requirements.txt
```

Verified installation with `pip list` to ensure all dependencies are properly configured.

## Database Integration 🍃

### MongoDB Atlas Configuration
Set up MongoDB Atlas cluster with M0 tier for development:
- Created project and configured authentication
- Set network access to allow connections from any IP (0.0.0.0/0)
- Retrieved Python connection string

### Data Upload Process
Created `notebook` directory with `mongoDB_demo.ipynb` for data ingestion. Successfully pushed dataset to MongoDB and verified through Atlas dashboard under Database > Browse Collections.

## Pipeline Development 💻

### Logging and Exception Handling
Implemented comprehensive logging and exception handling modules. Tested functionality with `demo.py` to ensure robust error management.

### Exploratory Data Analysis
Conducted thorough EDA and feature engineering analysis to understand data patterns and optimize preprocessing steps.

### Core Components
Developed modular pipeline components:

**Data Ingestion**: Built MongoDB connection functions in `configuration.mongo_db_connections.py` and data ingestion logic in `components.data_ingestion.py`

**Data Validation**: Implemented schema validation using `config.schema.yaml` and validation functions in `utils.main_utils.py`

**Data Transformation**: Created transformation pipeline in `components.data_transformation.py` with custom estimator in `entity/estimator.py`

**Model Training**: Developed training components in `components.model_trainer.py` with integrated estimator logic

Environment configuration:
```bash
# Linux/Mac
export MONGODB_URL="mongodb+srv://username:password...."
# Windows PowerShell
$env:MONGODB_URL = "mongodb+srv://username:password...."
```

## Cloud Infrastructure ☁️

### AWS Configuration
Set up AWS infrastructure with IAM user and AdministratorAccess permissions:

```bash
export AWS_ACCESS_KEY_ID="YOUR_AWS_ACCESS_KEY_ID"
export AWS_SECRET_ACCESS_KEY="YOUR_AWS_SECRET_ACCESS_KEY"
```

### S3 Integration
Created `my-model-mlopsproj` bucket in us-east-1 region for model storage. Implemented S3 operations in `src.aws_storage` and `entity/s3_estimator.py` for model versioning and deployment.

### Model Evaluation and Deployment
Built model evaluation components with S3 integration for model artifacts. Created prediction pipeline with API endpoints through `app.py` with web interface support.

## Production Deployment 🚀

### Containerization
Configured Docker deployment with `Dockerfile` and `.dockerignore` for containerized application deployment.

### CI/CD Pipeline
Implemented GitHub Actions workflow with AWS integration. Required GitHub secrets:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_DEFAULT_REGION`
- `ECR_REPO`

### EC2 Deployment
Deployed on AWS EC2 with:
- Docker installation and configuration
- Self-hosted GitHub runner setup
- Port 5080 configuration for web access
- Application accessible at `http://public-ip:5080`

## Technical Architecture 🌊

```
Data Ingestion → Data Validation → Data Transformation → Model Training → Model Evaluation → Model Deployment
```

Fully automated pipeline with GitHub Actions, Docker containerization, and AWS cloud infrastructure.

## Key Technologies 📚

**Data & ML**: MongoDB Atlas, Pandas, Scikit-learn
**Cloud**: AWS (S3, EC2, ECR), Docker
**CI/CD**: GitHub Actions, automated testing and deployment
**Web**: Flask API with HTML templates
**Monitoring**: Comprehensive logging and exception handling

## Project Highlights ✨

- **Scalable Architecture**: Modular components for easy maintenance and updates
- **Cloud-Native**: Full AWS integration with automated deployment
- **Production Ready**: Comprehensive error handling and monitoring
- **Modern MLOps**: Industry-standard CI/CD practices with containerization

## Resources 📖

- `crashcourse.txt`: Detailed setup and configuration guide
- AWS documentation for cloud service integration
- GitHub Actions for CI/CD automation best practices

## Getting the App Running 🎯

1. Clone the repository and set up the environment
2. Configure MongoDB and AWS credentials
3. Run the pipeline components or trigger through GitHub Actions
4. Access the deployed application through the EC2 public IP

The project demonstrates end-to-end MLOps practices with production-ready deployment and monitoring capabilities.