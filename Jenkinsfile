pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('build') {
            steps {
                     echo "test was a success"
                     sh "docker build -t node-app"
            }
        }
    }
}
