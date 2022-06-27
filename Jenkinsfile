pipeline {
  agent any

  parameters{
    string(name: 'administrator', defaultValue: 'Jenkins-Admin', description: 'Name of administrator')
  }
  stages {
    stage("build") {
      steps{
        echo "Hello ${params.administrator}, Building GraphX application ..."
        sh 'python3 --version'
      }
    }
    stage("test") {
      steps{
        echo 'Testing GraphX application ...'
        sh 'python3 -m unittest discover -s tests/unit'
      }
    }
    stage("deploy") {
      parallel {
        stage("dev001") {
          steps{
            echo 'Deploying GraphX application to dev001 landscape...'
          }
        }
        stage("staging"){
          steps{
            echo 'Deploying GraphX application to staging landscape...'
            sh 'curl --location --request GET "https://postman-echo.com/get?deploy=staging&status=marked"'
          }
        }
      } 
    }    
  }
  post {
    always {
        echo "This pipeline is design to build and deploy GraphX Application"
    }
    failure {
        echo "Notifying ${params.administrator} that the pipeline failed"
        mail bcc: '', body: "<b>GraphX pipeline has failed according to ${env.JOB_NAME} <br> Build Number: ${env.BUILD_NUMBER} <br> URL: ${env.BUILD_URL}", cc: '', charset: 'UTF-8', from: '', mimeType: 'text/html', replyTo: '', to: "jenkins-admin@local.me", subject: 'GraphX Pipeline failed!';
    }
  }
}
