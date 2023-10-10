pipeline {
  agent {
    kubeagent {
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