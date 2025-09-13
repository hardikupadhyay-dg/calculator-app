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
                bat 'docker build -t calculator-app .'
                echo 'minor test'
            }
        }

        stage('Run Tests in Container') {
            steps {
                bat 'docker run --rm calculator-app'
            }
        }
    }
}
