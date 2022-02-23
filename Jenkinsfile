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
    post{
        always{
            junit 'junit_report.xml'
        cobertura autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: 'coverage.xml', conditionalCoverageTargets: '70, 0, 0', failUnhealthy: false, failUnstable: false, lineCoverageTargets: '80, 0, 0', maxNumberOfBuilds: 0, methodCoverageTargets: '80, 0, 0', onlyStable: false, sourceEncoding: 'ASCII', zoomCoverageChart: false
        }

    }



} // pipeline
