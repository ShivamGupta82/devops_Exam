pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage("build and test"){
            steps{
                sh "docker build -t node-app"
            }
        }
          stage("deploy"){
            steps{
                sh "docker run -p 3000:3000 node-app"
            }
        }
    }
}
