pipeline {
  agent {
    kubernetes {
      yaml '''
        apiVersion: v1
        kind: Pod
        spec:
          containers:
          - name: docker
            image: docker:latest
            command:
            - cat
            tty: true
            volumeMounts:
             - mountPath: /var/run/docker.sock
               name: docker-sock
          volumes:
          - name: docker-sock
            hostPath:
              path: /var/run/docker.sock    
        '''
    }
  }
  environment {
    DOCKERHUBCRED = credentials('dockerhub')
  }
  stages {
    stage('Build-Docker-Image') {
      steps {
        container('docker') {
          sh 'docker build -t keskonbouf_front:latest ./streamlit_front'
        }
      }
    }
    stage('login dockerhub'){
      steps{
        container('docker'){
          sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
        }
      }
    }
    stage('Push image'){
      steps{
        container('docker'){
         sh 'docker push keskonbouf_front:latest' 
        }
      }
    }
  } 
}