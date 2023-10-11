pipeline {
  agent {label "kubeagent"}
  stages {
    stage('Build') {
      steps {
        git "api/"
      }
      steps{
        def api = docker.build("keskonbouf_api:latest")
      }
    }  
    stage('Test') {
      steps {

          echo 'pouet'
        
      }
    }
}
}