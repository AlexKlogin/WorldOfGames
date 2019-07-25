pipeline {
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        echo 'Cloning..'
        git 'https://github.com/AlexKlogin/WorldOfGames'
      }
    }
    stage('Building image') {
      steps{
      echo 'Building..'
        script {
          'docker-compose build'
        }
      }
    }
  }
}