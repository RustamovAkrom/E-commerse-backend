pipeline {
    agent any

    stages {
        stage('Checkout'){
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'python manage.py test' 
            }
        }
    }
}