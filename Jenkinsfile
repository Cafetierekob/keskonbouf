pipeline {
  agent {label "kubeagent"}
  stages {
    stage('Build') {
      agent{docker {image "docker:latest"}}
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