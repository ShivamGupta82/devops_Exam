pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage("build and test") {
            steps {
                script {
                    // Build the Docker image with a tag
                    sh "docker build -t node-app:latest ."
                }
            }
        }
        stage("deploy") {
            steps {
                script {
                    // Run the Docker container from the built image
                    sh "docker run -p 3000:3000 node-app:latest"
                }
            }
        }
    }
}
