pipeline {
    agent {label "kubeagent"}

    stages {
        stage('Clean') {
            steps {
                echo 'Pouet 1'
            }
        }
        stage('Build Docker Image') {
            steps {
                docker image build ./api -t keskonbouf_api:latest 
            }
        }
        stage('Deploy') {
            steps {
                echo 'Pouet 3'
            }
        }
    }
}