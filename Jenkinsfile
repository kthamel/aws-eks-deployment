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
            parallel {
                stage('Application deployment - Nginx-A') {
                    steps {
                        sh 'helm lint ./helm-app-nginx-a'
                        sh 'helm install app-nginx-a --debug --dry-run ./helm-app-nginx-a'
                        sh 'helm template ./helm-app-nginx-a'
                        sh 'helm install app-nginx-a ./helm-app-nginx-a'
                    }
                }   
                stage('Application deployment - Nginx-B') {
                    steps {
                        sh 'helm lint ./helm-app-nginx-b'
                        sh 'helm install app-nginx-b --debug --dry-run ./helm-app-nginx-b'
                        sh 'helm template ./helm-app-nginx-b'
                        sh 'helm install app-nginx-b ./helm-app-nginx-b'
                    }
                }
            }
        }

        stage('Helm deployment list') {
            steps {
                sh 'helm list -a'
            }
        }    
    }
}
