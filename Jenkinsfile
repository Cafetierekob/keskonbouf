pipeline {
  agent {label "kubeagent"}
  stages {
    stage('Build') {
      steps {
        container('docker') {
          docker image build ./api -t keskonbouf_api:latest
        }
      }
    }  
    stage('Test') {
      steps {

          echo 'pouet'
        
      }
    }
}
}