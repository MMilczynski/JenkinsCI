pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh 'pytest tests --cov-report=xml:coverate_results\coverage.xml --cov=lib'
            }
        }
    }
}