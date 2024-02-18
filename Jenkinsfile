pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                script {
                    sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh '''
                    source venv/bin/activate
                    pytest -m "profile" --alluredir=test_results
                    '''
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'test_results/**', fingerprint: true
        }
    }
}
