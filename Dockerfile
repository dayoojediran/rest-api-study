FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN sudo apt install pip & sudo apt install  python3.8-venv & pip install --no-cache-dir --upgrade -r requirements.txt 
COPY . .
CMD ["/bin/bash", "docker-entrypoint.sh"]