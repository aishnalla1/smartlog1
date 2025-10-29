pipeline {
    agent any

    environment {
        IMAGE = 'smartlog'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/aishnalla1/smartlog1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE% .'
            }
        }

        stage('Run Container (Test)') {
            steps {
                bat 'docker rm -f smartlog_test || echo skip'
                bat 'docker run -d --name smartlog_test -p 5000:5000 %IMAGE%'
                bat 'timeout /t 5'
                bat 'curl http://localhost:5000/'
            }
        }

        stage('API Test') {
            steps {
                // Root endpoint test
                bat 'curl -f http://localhost:5000/ || exit 1'

                // Analyze endpoint test with POST data
                bat 'curl -X POST http://localhost:5000/analyze -H "Content-Type: application/json" -d "{\\"logs\\":\\"ERROR: test failure\\"}"'
            }
        }

        stage('Clean Up') {
            steps {
                bat 'docker stop smartlog_test && docker rm smartlog_test'
            }
        }
    }
}
