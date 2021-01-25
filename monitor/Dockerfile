FROM ubuntu
RUN apt update && apt install -y --no-install-recommends python3 python3-pip
WORKDIR /myscript
COPY requirements requirements.txt
RUN pip3 install -r requirements.txt
COPY monitor_eventos.py /myscript
ENTRYPOINT ["python3","/myscript/monitor_eventos.py","/workdir"]
