FROM ubuntu
WORKDIR /
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    python3 \
    python3-pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install "pyramid==1.10.4" waitress
COPY . .
CMD ["python3", "app.py"]