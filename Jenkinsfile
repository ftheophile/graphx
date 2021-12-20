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
        echo 'Testing Graphx application ...'
        python -m unittest discover -s tests/unit
      }
    }
    stage("deploy") {
      steps{
        echo 'Deploying Graphx application ...'
      }
    }    
  }
}
