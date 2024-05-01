# CONTIBUTING

## How to run the Dockerfile locally

```
sudo docker run -d -p 5000:5000 -w /app -v "$(pwd):/app" flask sh -c "flash run --host 0.0.0.0"

```