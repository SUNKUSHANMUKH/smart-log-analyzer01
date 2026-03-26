pipeline {
    agent any

    environment {
        IMAGE_NAME = 'smart-log-app'
        // Use BUILD_NUMBER for unique tags, or keep 'v1' if you prefer static
        IMAGE_TAG  = "${BUILD_NUMBER}"
    }

    stages {
        // No explicit Checkout stage – Jenkins does that automatically.

        stage('Test') {
            steps {
                // Optional – skip if you don't have tests yet
                sh 'pip install pytest'
                sh 'pytest tests/ -v'   // Remove if tests/ folder doesn't exist
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Switch to Minikube's Docker daemon
                    sh 'eval $(minikube docker-env)'
                    sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                    sh "docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest"
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Update the deployment image and wait for rollout
                    sh "kubectl set image deployment/log-app log-app=${IMAGE_NAME}:${IMAGE_TAG}"
                    sh "kubectl rollout status deployment/log-app"
                }
            }
        }

        stage('Verify') {
            steps {
                sh 'kubectl get pods'
                // Optional: test the endpoint
                sh '''
                    kubectl port-forward service/log-app-service 8080:80 &
                    sleep 5
                    curl -f http://localhost:8080/analyze || exit 1
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Deployment Successful!'
        }
        failure {
            echo '❌ Build Failed — Check logs!'
        }
    }
}