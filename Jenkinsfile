pipeline {
    agent any


       triggers {
                    pollSCM('H/5 * * * *')

                }

    stages {
        stage('Clonado de codigo fuente') {
            steps {
                git branch: 'main', credentialsId: 'gitCredentials', url: 'https://github.com/abibee12/Sprint10.git'
                echo 'se ha clonado el repositorio '
                echo 'probando nuevo cambio para sondear'
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

            // Ejecutamos los tests con cobertura
            bat 'coverage run -m pytest'

            // Verificamos la cobertura
            bat 'coverage report -m --fail-under=80'

            // Desactivamos el entorno virtual (Windows)
            bat 'venv\\Scripts\\deactivate.bat'

            echo 'Todos los tests se han ejecutado correctamente con al menos un 80% de cobertura.'
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
                    bat 'docker build -t abigailmtz8/appflask .'

                    echo "imagen creada exitosamente"

                    echo "segunda prueba ejecucion automatica tras nueva actualizacion"
                }
            }
        }

stage('Subida a Registry') {

    steps {
        script {
            // Autenticación con Docker Hub
            withCredentials([usernamePassword(credentialsId: 'dockerup', passwordVariable: 'dockerpass', usernameVariable: 'dockeruser')]) {

                bat "echo  docker login -u ${dockeruser}  -p ${dockerpass}  --password-stdin"
                // Sube la imagen al registry
                bat 'docker push abigailmtz8/appflask:latest'

                echo "Imagen subida exitosamente a Docker Hub"
            }
        }
    }
}





    }
}




