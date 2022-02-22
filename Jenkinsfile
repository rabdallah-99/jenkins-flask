pipeline {
    agent any
    stages {
        stage('setup') {
            steps {
                sudo apt update
                sudo apt install python3 python3-venv python3-pip -y
                if (!fileExists('jenkins-flask')) {
                  sh '  git clone https://github.com/rabdallah-99/jenkins-flask'
                    }
                sh ' . ./setup.sh'

            } //steps close
        }
        stage('Test') {
            steps {
               sh ' python3 tests/test_app.py '
            }
        }
        stage('Database creation') {
            steps {
                if (fileExists('data.db')) {
                sh '    echo Database Exists'
                } else {
                sh 'python3 create.py'
                }

            }
        }
        stage('Run') {
            steps {
                sh ' python3 app.py &'
            }
        }  // Run
    } //stages
} // pipeline
