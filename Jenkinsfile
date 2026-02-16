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
    sh 'docker run --rm -v "$PWD/app":/out comisiones-app sh -lc "python /app/script_comisiones.py && cp /app/comisiones.xlsx /out/comisiones.xlsx"'
  }
}
  }

  post {
    success { echo 'Pipeline ejecutado correctamente' }
    failure { echo 'Pipeline falló' }
  }
}