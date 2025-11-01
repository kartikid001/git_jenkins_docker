pipeline {
    agent any
    environment{
        python = 'C:\\Users\\kardm\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }
    // triggers{
    //     cron("*/1 * * * *")
    // }
    stages{
        stage('Checkout Code'){
            steps{
                checkout scm
            }
        }
        stage('Build Docker Image'){
            steps{
                bat "docker build -t GDJ1"
            }
        }
        stage('CREATE CONTAINER'){
            steps{
                bat "docker run 8502:8502 GDJ1"
            }
        }
    }
    post{
        success {
            echo "SUCCESSFUL ETL..."
        }
        failure {
            echo "ETL FAILED !!"
        }
        always {
            echo "ETL PROCESS .."
        }
    }
}