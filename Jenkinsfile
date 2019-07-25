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
      bat 'docker-compose build'
      }
    }
    stage('Running container') {
      steps{
      echo 'running..'
      bat 'docker-compose up -d'
      }
    }

    stage('testing application') {
      steps{
      echo 'testing..'
      bat 'python tests/e2e.py'
      }
    }
  }
}