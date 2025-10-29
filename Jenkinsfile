pipeline {
    agent any

    environment {
        IMAGE = 'smartlog'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/aishnalla1/SmartLog.git'
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

        stage('Clean Up') {
            steps {
                bat 'docker stop smartlog_test && docker rm smartlog_test'
            }
        }
    }
}
