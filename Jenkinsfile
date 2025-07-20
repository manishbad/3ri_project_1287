pipeline {
    agent any

    environment {
        IMAGE_NAME = "helloworld"
        CONTAINER_NAME = "hwcontainer"
        CONTAINER_PORT = "5000"
        HOST_PORT = "8082"
        RANDOM_TAG = "v${new Random().nextInt(9999)}"
    }

    stages {
        
        stage('Checkout Github Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/manishbad/3ri_project_1287.git'
            }
        }
        stage('Cleanup Existing Container') {
            steps {
                script {
                    echo "Stopping and removing container if it exists..."
                    sh """
                    if [ \$(docker ps -aq -f name=\$CONTAINER_NAME) ]; then
                        docker stop \$CONTAINER_NAME || true
                        docker rm \$CONTAINER_NAME || true
                    fi
                    """
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker Image with tag: \$RANDOM_TAG"
                    sh """
                    docker build -t \$IMAGE_NAME:\$RANDOM_TAG .
                    """
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    echo "Running container \$CONTAINER_NAME with image tag \$RANDOM_TAG"
                    sh """
                    docker run -d --name \$CONTAINER_NAME -p \$HOST_PORT:\$CONTAINER_PORT \$IMAGE_NAME:\$RANDOM_TAG
                    """
                }
            }
        }

        stage('Show Running Container') {
            steps {
                sh 'docker ps -f name=$CONTAINER_NAME'
            }
        }
    }
}
