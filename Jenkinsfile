pipeline{
    
    agent {
        dockerfile true
    }
    
    stages {
        stage('deploy'){
            steps {
                sh 'docker build .'
                sh 'docker-compose up'
            }
        }
        
    }
    
}
