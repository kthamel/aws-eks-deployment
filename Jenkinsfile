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
                sh 'helm lint ./application-nginx'
                sh 'helm install app-nginx --debug --dry-run ./application-nginx'
                sh 'helm template ./application-nginx'
                sh 'helm install app-nginx ./application-nginx'
            }
        }

        stage('Helm deployment list') {
            steps {
                sh 'helm list -a'
            }
        }    
    }
}
