pipeline {
    agent any

    stages {
        stage('List Clusters') {
            steps {
                sh 'aws eks list-clusters'
            }
        }

        stage('Check files') {
            steps {
                sh 'ls -l'
            }
        }
    }
}
