FROM python:3.10
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN sudo apt install pip & sudo apt install python3.8-venv & pip install -r requirements.txt 
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]