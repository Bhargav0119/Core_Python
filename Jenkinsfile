pipeline {
    agent any

    environment {
        PYTHON_EXE = 'C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
    }

    stages {
        stage('Verify Python') {
            steps {
                bat '"%PYTHON_EXE%" --version'
            }
        }

        stage('Discover Python Files') {
            steps {
                bat 'dir /s /b *.py'
            }
        }

        stage('Run Python Exercise') {
            steps {
                bat '"%PYTHON_EXE%" "Week_One\\Day_Three\\Accessing_lists.py"'
            }
        }
    }

    post {
        success {
            echo 'Core Python pipeline completed successfully'
        }

        failure {
            echo 'Core Python pipeline failed—check the console output'
        }
    }
}