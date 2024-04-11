echo [$(date)]: "START"

echo [$(date)]: "Creating env"
pip install virtualenv
virtualenv venv

echo [$(date)]: "Activating env"
# Activate virtual environment based on operating system
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        source venv/bin/activate
    elif [[ "$OSTYPE" == "msys" ]]; then
        source venv/Scripts/activate
    else
        echo "Unsupported operating system. Please activate the virtual environment manually."
        exit 1
    fi

echo [$(date)]: "installing the requirements"
pip install -r requirements.txt

echo [$(date)]: "END"