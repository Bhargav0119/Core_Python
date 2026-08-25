pipeline {
    agent any

    environment {
        PYTHON_EXE = 'C:\\Users\\Dell\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
    }

    triggers {
        pollSCM('H/5 * * * *')
    }

    stages {
        stage('Verify Python') {
            steps {
                bat '"%PYTHON_EXE%" --version'
            }
        }

        stage('Syntax Check') {
            steps {
                bat '"%PYTHON_EXE%" -m compileall -q Week_One'
            }
        }

        stage('Discover Python Files') {
            steps {
                bat 'dir /s /b *.py'
            }
        }

        stage('Create Test Environment') {
            steps {
                bat 'if exist .venv rmdir /s /q .venv'
                bat '"%PYTHON_EXE%" -m venv .venv'
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements-dev.txt'
            }
        }

        stage('Run Automated Tests') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest -v'
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