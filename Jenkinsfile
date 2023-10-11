pipeline {
  agent {label "kubeagent"}
  stages {
    stage('Build') {
      steps {
        sh "docker build -t keskonbouf_api:latest ./api"
      }
    }  
    stage('Test') {
      steps {

          echo 'pouet'
        
      }
    }
}
}