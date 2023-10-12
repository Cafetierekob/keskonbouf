pipeline {
  agent {
    kubernetes {
      yaml '''
        apiVersion: v1
        kind: Pod
        spec:
          containers:
          - name: kube
            image: bitnami/kubectl:latest
            command:
            - cat
            tty: true
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
    stage('Build-Docker-Images') {
      parallel{
        stage('build api'){
          steps {
            container('docker') {
              sh 'docker build -t cafetiere/keskonbouf_front:latest ./streamlit_front'
            }
          }
        }
        stage('build front'){
          steps{
            container('docker'){
              sh 'docker build -t cafetiere/keskonbouf_api:latest ./api'
            }
          }
        }

      }
    }
    stage('login dockerhub'){
      steps{
        container('docker'){
          sh 'docker login -u $DOCKERHUBCRED_USR -p $DOCKERHUBCRED_PSW'
        }
      }
    }
    stage('Push images'){
      parallel{
        stage('Push front'){
          steps{
            container('docker'){
              sh 'docker image push cafetiere/keskonbouf_front:latest' 
           }
          }        
        }
        stage('Push api'){
          steps{
            container('docker'){
              sh 'docker image push cafetiere/keskonbouf_api:latest' 
            }
          }
        }
      }
    }
    stage('Deplyment front'){
      steps{
        container('kube'){
          withKubeConfig([namespace :'default']){
            sh 'kubectl rollout restart -n default deployment keskonbouf-front'
          }
        }
      }
    }
  }
}

