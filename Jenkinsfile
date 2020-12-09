pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3-alpine' 
                }
            }
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'pip install pytest'
                sh 'pip install "numpy==1.18.4"'
                sh 'pip install pytest-cov'
                sh 'pytest tests --cov-report=xml:coverate_results/coverage.xml --cov=lib'
            }
        }
    }
}