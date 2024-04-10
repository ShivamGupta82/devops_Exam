pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage("Test") {
            steps {
                script {
                    // Run Python Selenium script
                    def output = sh(script: 'python3 selenium_script.py', returnStdout: true).trim()
                    println "Output of selenium_script.py: ${output}"
                    // Check the output to determine the test condition
                    if (output.contains('Passed')) {
                        currentBuild.result = 'SUCCESS'
                    } else {
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }
        stage("build and test"){
            steps{
                sh "docker build -t node-app."
            }
        }
          stage("deploy"){
            steps{
                sh "docker run -p 3000:3000 node-app"
            }
        }
    }
}
