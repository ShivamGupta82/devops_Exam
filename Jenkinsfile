pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Test') {
            steps {
                script {
                    // Run Python Selenium script
                    def output = sh(script: 'python3 selenium_script.py', returnStdout: true).trim()
                    println "Output of test_script.py: ${output}"
                    // Check the output to determine the test condition
                    if (output.contains('Passed')) {
                        currentBuild.result = 'SUCCESS'
                    } else {
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }
        stage("build") {
            steps {
                script {
                    // Build the Docker image with a tag
                    sh "docker build -t node-app:latest ."
                }
            }
        }
         stage("push"){
            steps{
                withCredentials([usernamePassword(credentialsId:"dockerHub",passwordVariable:"dockerHubPass",usernameVariable:"dockerHubUser")]){
                sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                sh "docker tag node-app:latest ${env.dockerHubUser}/node-app:latest"
                sh "docker push ${env.dockerHubUser}/node-app-test-new:latest"
                echo 'image push ho gaya'
                }
            }
        }
        stage("deploy"){
            steps{
                sh "docker-compose down && docker-compose up -d"
            }
        }
    }
}
