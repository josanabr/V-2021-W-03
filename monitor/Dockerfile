FROM python:3.7-alpine
WORKDIR /myscript
COPY requirements requirements.txt
RUN pip install -r requirements.txt
COPY monitor_eventos.py /myscript
CMD ["/myscript/monitor_eventos.py","/workdir"]
