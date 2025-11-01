pipeline {
    agent any

    environment {
        python = 'C:\\Users\\kardm\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t gdj1 ."
            }
        }

        stage('Create Container') {
            steps {
                bat "docker run -d -p 8502:8501 gdj1"
            }
        }
    }

    post {
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
