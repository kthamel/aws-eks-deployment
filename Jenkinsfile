pipeline {
    agent any

    stages {
        stage('List Clusters') {
            steps {
                sh 'aws eks list-clusters'
            }
        }

        stage('Select cluster') {
            steps {
                sh 'aws eks update-kubeconfig --region us-east-1 --name kthamel-eks-cluster'
            }
        }

        stage('List nodes') {
            steps {
                sh 'kubectl get nodes'
            }
        }

        stage('Application deployment') {
            steps {
                sh 'helm lint ./helm-app-python'
                sh 'helm install app-python --debug --dry-run ./helm-app-python'
                sh 'helm template ./helm-app-python'
                sh 'helm install app-python ./helm-app-python'
            }
        }

        stage('Helm deployment list') {
            steps {
                sh 'helm list -a'
            }
        }    
    }
}
