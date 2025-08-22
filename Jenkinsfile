pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/hardikupadhyay-dg/calculator-app.git'

            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t calculator-app .'
            }
        }

        stage('Run Tests in Container') {
            steps {
                sh 'docker run --rm calculator-app'
            }
        }
    }
}
