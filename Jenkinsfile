pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("comisiones-app")
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    docker.image("comisiones-app").inside {
                        sh 'python script_comisiones.py'
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline ejecutado exitosamente'
        }
        failure {
            echo 'Pipeline falló'
        }
    }
}