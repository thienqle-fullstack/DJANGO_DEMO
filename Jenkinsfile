pipeline{
    
    agent any
    
    stages {
        stage('build'){
            steps {
                 echo "build application"
                 bat """
                    python -m venv env
                    cmd /c "env\\Scripts\\activate.bat"
                    pip install -r requirement.txt
                    python manage.py collectstatic --noinput
                    cmd /c "env\\Scripts\\deactivate.bat"
                 """
            }
        }
        
        stage('test'){
            steps {
                 echo "test application"
                 bat """
                    cmd /c "env\\Scripts\\activate.bat"
                    python manage.py test
                    cmd /c "env\\Scripts\\deactivate.bat"
                 """
            }
        }
        
        stage('deploy'){
         
            steps {
                echo "deploy application"
                bat """
                    whoami
                    copy * G:\\Webhost\\hello_django
                    copy hello_project G:\\Webhost\\hello_django\\hello_project
                    copy static  G:\\Webhost\\hello_django\\static
                    cmd /c "python -m venv G:\\Webhost\\hello_django\\env"
                    cmd /c "G:\\Webhost\\hello_django\\env\\Scripts\\activate.bat"
                    cmd /c "python G:\\Webhost\\hello_django\\manage.py collectstatic --noinput"
                """
            }
        }
        
    }
    
}
