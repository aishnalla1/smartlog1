pipeline {
    agent any

    environment {
        IMAGE_NAME = "smartlog"
        CONTAINER_NAME = "smartlog_test"
        PORT = "5002"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/aishnalla1/smartlog1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Run Container (Test)') {
            steps {
                bat """
                    docker rm -f ${CONTAINER_NAME} || echo skip
                    docker run -d --name ${CONTAINER_NAME} -p ${PORT}:5000 ${IMAGE_NAME}
                """
            }
        }

        stage('API Test') {
            steps {
                bat """
                    curl -f http://localhost:${PORT} || exit 1
                """
            }
        }

        stage('Clean Up') {
            steps {
                bat "docker rm -f ${CONTAINER_NAME} || echo skip"
            }
        }
    }

    post {
        always {
            bat "docker rm -f ${CONTAINER_NAME} || echo skip"
        }
        success {
            echo '✅ CI/CD pipeline executed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check logs above.'
        }
    }
}
