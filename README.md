# Security Testing Implementation

This project implements a comprehensive security testing framework with CI/CD integration, including Static Application Security Testing (SAST), Dynamic Application Security Testing (DAST), and code quality analysis using SonarQube.

## Features

- **Static Analysis (SAST)**
  - SonarQube integration for code quality and security analysis
  - Pylint for Python code quality checks
  - Coverage reporting with pytest

- **Dynamic Analysis (DAST)**
  - OWASP ZAP integration for automated security testing
  - Comprehensive security scan reports
  - Integration with CI/CD pipeline

- **CI/CD Pipeline**
  - Automated testing on every push and pull request
  - Security scanning in the deployment pipeline
  - Quality gates enforcement

## Prerequisites

- Python 3.9 or higher
- Docker (for running OWASP ZAP)
- SonarQube server (local or cloud instance)
- ngrok (for exposing local SonarQube server)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/security-app-testing.git
   cd security-app-testing
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up SonarQube:
   - Install and start SonarQube server locally
   - Create a new project in SonarQube
   - Generate an authentication token
   - Configure ngrok to expose your local SonarQube server:
     ```bash
     ngrok http 9000
     ```

4. Configure GitHub Secrets:
   - `SONAR_TOKEN`: Your SonarQube authentication token
   - `SONAR_HOST_URL`: Your ngrok URL (e.g., https://xxxx-xxx-xxx-xxx-xxx.ngrok.io)

## Project Structure

```
security-app-testing/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # CI/CD pipeline configuration
├── app/
│   └── ...                    # Application source code
├── tests/
│   └── ...                    # Test files
├── zap-reports/              # OWASP ZAP scan reports
├── requirements.txt          # Python dependencies
└── README.md                # This file
```

## Running Tests

### Local Testing

1. Run unit tests with coverage:
   ```bash
   python -m pytest --cov=app --cov-report=xml:coverage.xml --junitxml=test-results.xml
   ```

2. Run pylint:
   ```bash
   pylint app tests > pylint-report.txt
   ```

### Security Scanning

1. Start the application:
   ```bash
   python run.py
   ```

2. Run OWASP ZAP scan:
   ```bash
   docker run --rm \
     -v "$(pwd)/zap-reports:/zap/wrk/:rw" \
     -t ghcr.io/zaproxy/zaproxy:stable \
     zap-baseline.py \
     -t http://localhost:5000 \
     -J report.json \
     -w report.md \
     -r report.html
   ```

## CI/CD Pipeline

The project includes a GitHub Actions workflow that runs:
1. Unit tests and code coverage
2. Static code analysis with SonarQube
3. Dynamic security testing with OWASP ZAP
4. Deployment (if on main branch)

## Security Reports

- SonarQube reports are available in your SonarQube instance
- OWASP ZAP reports are generated in the `zap-reports` directory
- Test coverage reports are generated as XML files

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OWASP ZAP for dynamic security testing
- SonarQube for static code analysis
- GitHub Actions for CI/CD pipeline
