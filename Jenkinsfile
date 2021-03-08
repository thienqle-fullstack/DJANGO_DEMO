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
                    xcopy * G:\\Webhost\\hello_django /s /i
                    no
                """
            }
        }
        
    }
    
}
