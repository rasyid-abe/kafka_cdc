pipeline{
    // environment {
    //     credentialId = 'aliregistry'
    //     url = "https://registry-intl.ap-southeast-5.aliyuncs.com"
    //     scannerHome = tool 'Sonarqube'
    //     servicename = 'kafka-connect-staging'
    // }
    agent any
    stages {
        stage('Publish Approval') {
            when { 
                tag "v*"
            }
            steps {
                script{
                //   input message: "Deploy these changes?", submitter "admin"
                def userName = input message: 'Deploy these changes?', submitter: "grandis,admin", submitterParameter: "grandis,admin"
                echo "Accepted by ${userName}"
                if (!(['grandis','admin'].contains(userName))) {
                    error('This user is not approved to deploy to PROD.')
                }
                }
            }
        }
        stage('Deploy Kafka Connect Prod') {
            when { 
                tag "v*"
            }
            steps {
                script {
                    sshagent (credentials: ['kafka-connect-prod-gcp']) {
                    sh 'ssh -t -o StrictHostKeyChecking=no -l majoo 10.128.0.52 "cd ~/svc-data-cdc/infrastructure/kafka; git fetch --all; git checkout tags/${TAG_NAME}; cd ~/svc-data-cdc; . ./export-env.sh; python3 cicd.py --env prod;"'
                    }
                  }
                }
                post {
                success {
                    slackSend (color: '#008000', message: "SUCCESS: Deploy Kafka Connect Prod ${env.JOB_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
                }
                failure {
                    slackSend (color: '#FF0000', message: "FAILED: Deploy Kafka Connect Prod ${env.JOB_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
                }
             }
        }    
        stage('Deploy Kafka Connect Staging') {
            when { 
                branch "main"
            }
            steps {
                script {
                    sshagent (credentials: ['staging-kafka-cdc']) {
                    //sh 'ssh -tt -o StrictHostKeyChecking=no -l adam 10.130.233.190 -p 2801 "cd ~/kafka/infrastructure/kafka/svc-data-cdc/infrastructure/kafka; git pull origin main; docker-compose -f ~/kafka/infrastructure/kafka/svc-data-cdc/infrastructure/kafka/kafka-connect.yaml up -d; cd ~/kafka/infrastructure/kafka/svc-data-cdc; . ./export-env.sh; python3 cicd.py --env staging;"'
                    
                    sh 'ssh -t -o StrictHostKeyChecking=no -l majoo 10.132.0.35 "cd ~/svc-data-cdc/infrastructure/kafka; git pull origin main; docker compose -f ~/svc-data-cdc/infrastructure/kafka/kafka-connect-stg.yaml up -d; cd ~/svc-data-cdc; . ./export-env.sh; python3 cicd.py --env staging;"'
                    }
                }
            }
            post {
                success {
                    slackSend (color: '#008000', message: "SUCCESS: Deploy Kafka Connect Beta ${env.JOB_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
                }
                failure {
                    slackSend (color: '#FF0000', message: "FAILED: Deploy Kafka Connect Beta ${env.JOB_NAME} #${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>)")
                }
            }
        }
    }
}