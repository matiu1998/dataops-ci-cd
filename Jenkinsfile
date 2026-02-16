pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t comisiones-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run --rm -v "$PWD":/app comisiones-app'
            }
        }
    }

    post {
        success {
            echo 'Pipeline ejecutado correctamente'
        }
        failure {
            echo 'Pipeline falló'
        }
    }
}