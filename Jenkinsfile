pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/kartikid001/git_jenkins_docker.git', branch: 'main'
            }
        }
        stage("Cleanup") {
            steps{
                bat "for /f "tokens=*" %%i in ('docker ps -aq') do docker rm -f %%i"
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
}
