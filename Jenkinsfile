pipeline {
    agent any
    environment {
        CREATE_SCHEMA = "true"
        DATABASE_URI = credentials("DATABASE_URI")
        SECRET_KEY = credentials("SECRET_KEY")
    }
    stages {
        stage('setup') {
            steps {
                sh ' bash ./setup.sh'
            } //steps close
       }
        stage('Test') {
            steps {
               sh ' bash test.sh  '
            }
        }
        stage('Database creation') {
            steps {
                script{
                    if (env.CREATE_SCHEMA == "true") {
                        sh ' bash database.sh'
                    }
                }

            }
        }
        stage('Run') {
            steps {
                sh ' bash run.sh'
            }
        }  // Run
    } //stages
} // pipeline
