pipeline {
    agent any

parameters {
        choice choices: ['main', 'master', 'developer'], name: 'BRANCH'
    }

       triggers {
                    pollSCM('H/5 * * * *')
                }

    stages {
        stage('Clonado de codigo fuente') {
            steps {
                git branch: 'main', credentialsId: 'gitCredentials', url: 'https://github.com/abibee12/Sprint10.git'
                echo 'se ha clonado el repositorio '
                echo 'nuevo cambio para sondear'
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
       //aqui tiene que ir un condicional
        when {
                expression { params.BRANCH == 'main' }
            }
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

 stages {
        stage('Conditional Stage') {
            when {
                expression { BRANCH_NAME == 'origin/' + params.BRANCH }
            }
            steps {
                script {
                    echo "Este stage se ejecutará solo si la rama es 'origin/${params.BRANCH}'."
                    echo "La rama actual es: ${BRANCH_NAME}"
                }
            }
        }
    }



    }
}
