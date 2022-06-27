pipeline {
  agent { docker { image 'python:3.10.1-alpine'}}

  parameters{
    string(name: 'administrator', defaultValue: 'Jenkins-Admin', description: 'Name of administrator')
  }
  stages {
    stage("build") {
      steps{
        echo "Hello ${params.administrator}, Building GraphX application ..."
        sh 'python --version'
      }
    }
    stage("test") {
      steps{
        echo 'Testing GraphX application ...'
        sh 'python3 -m unittest discover -s tests/unit'
      }
    }
    stage("deploy") {
      parallel dev001:{
        node('dev001'){
          echo 'Deploying GraphX application to dev001 landscape...'
        }
      },
      staging:{
        node('staging'){
            echo 'Deploying GraphX application to staging landscape...'
        }
      }
    }    
  }
  post {
    always {
        echo "This pipeline is design to build and deploy GraphX Application "
    }
    failure {
        echo "Notifying ${params.administrator} that the pipeline failed"
        mail to: jenkins-admin@local.me, subject: 'GraphX Pipeline failed!'
    }
  }
}
