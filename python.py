print("Hello from Python on Jenkins!")
pipeline {
    agent any

    stages {
        stage('Run Python Script') {
            steps {
                sh 'python3 hello.py'
            }
        }
    }
}
