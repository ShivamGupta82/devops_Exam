pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('test') {
            steps {
                script {
                    // Run Python Selenium script
                    def output = sh(script: 'python3 selenium_script.py', returnStdout: true).trim()
                    println "${output}"
                    // Check the output to determine the test condition
                    if (output.contains('Passed')) {
                        currentBuild.result = 'SUCCESS'
                    } else {
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }
        stage('build') {
            when {
                expression {
                    return currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                     echo "test was a success"
                     sh "docker build -t node-app"
            }
        }
    }
}
