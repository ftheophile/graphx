pipeline {
  agent any
  stages {
    stage("build") {
      steps{
        echo 'Building Graphx application ...'
      }
    }
    stage("test") {
      steps{
        echo 'Building Graphx application ...'
        sh 'python3 -m unittest discover -s tests/unit'
      }
    }
    stage("deploy") {
      steps{
        echo 'Deploying Graphx application ...'
      }
    }    
  }
}
