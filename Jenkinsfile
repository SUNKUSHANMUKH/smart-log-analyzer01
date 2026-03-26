pipeline {
    agent any

    environment {
        IMAGE_NAME = 'smart-log-app'
        IMAGE_TAG  = "${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/YOUR_USERNAME/smart-log-analyzer'
            }
        }

        stage('Test') {
            steps {
                sh 'pip install pytest'
                sh 'pytest tests/ -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                sh "docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh "kubectl set image deployment/log-app log-app=${IMAGE_NAME}:${IMAGE_TAG}"
                sh "kubectl rollout status deployment/log-app"
            }
        }

        stage('Verify') {
            steps {
                sh 'kubectl get pods'
            }
        }
    }

    post {
        success { echo '✅ Deployment Successful!' }
        failure  { echo '❌ Build Failed — Check logs!' }
    }
}
