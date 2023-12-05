pipeline {
    agent any

    stages {
        stage('Clonado de codigo fuente') {
            steps {
                git branch: 'main', credentialsId: 'gitCredentials', url: 'https://github.com/abibee12/Sprint10.git'
                echo 'se ha clonado el repositorio '
            }
        }

        stage('Ejecucion de los test') {
            steps {
                script {
                    // Configuramos el entorno virtual
                    bat 'python -m venv venv'

                    // Activamos el entorno virtual (Windows)
                    bat 'venv\\Scripts\\activate.bat'

                    // Instalamos las dependencias
                    bat 'pip install -r requirements.txt'

                    // Ejecutamos los tests
                    bat 'pytest'

                    // Desactivamos el entorno virtual (Windows)
                    bat 'venv\\Scripts\\deactivate.bat'

                    echo 'todos los test se han ejecutado correctamente'
                }
            }
        }

        stage('Linting con flake8') {
            steps {
                script {
                    // Activamos el entorno virtual (Windows)
                    bat 'venv\\Scripts\\activate.bat'

                    // Ejecutamos flake8 para linting
                    bat 'flake8'

                    // Desactivamos el entorno virtual (Windows)
                    bat 'venv\\Scripts\\deactivate.bat'

                    echo "Current branch: \${BRANCH_NAME}"

                    echo 'linting realizado'
                }
            }
        }

        stage('Creacion de Imagen Docker') {
            steps {
                script {
                    // Construye la imagen Docker
                    bat 'docker build -t appflask .'

                    echo "imagen creada exitosamente"

                    echo "segunda prueba ejecucion automatica tras nueva actualizacion"
                }
            }
        }

   stage('Subida a Registry') {
    when {
        expression {
            // Obtén la rama actual de Git de manera más robusta
            def gitBranch = bat(script: 'git rev-parse --abbrev-ref HEAD', returnStdout: true).trim()
            echo "Git Branch: ${gitBranch}"

            return gitBranch in ['develop', 'master', 'main']
        }
    }
    steps {
        script {
            // Autenticación con Docker Hub (sustituye con tu configuración específica)
            bat 'docker login -u abigailmtz8 -p Abigailmtz_'

            // Sube la imagen al registry (sustituye <tu-repositorio-dockerhub>)
            bat 'docker push abigailmtz8/appflask:latest'

            echo "Imagen subida exitosamente a Docker Hub"
        }
    }
}

    }
}
