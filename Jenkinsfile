pipeline{
    
    agent any
    
    stages {
        stage('build'){
            steps {
                 echo "build application"
                 bat """
                    python -m venv env
                    cmd /c "env\Scripts\activate.bat"
                    pip install -r requirement.txt
                    cmd /c "env\Scripts\deactivate.bat"
                 """
            }
        }
        
        stage('test'){
            steps {
                 echo "test application"
                 bat """
                    python -m venv env
                    cmd /c "env\Scripts\activate.bat"
                    pip install -r requirement.txt
                    python manage.py runserver
                 """
            }
        }
        
    }
    
}
