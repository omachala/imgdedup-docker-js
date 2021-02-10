FROM python:3.8
RUN pip install imagededup
WORKDIR /
RUN pip install imagededup
COPY run.py .
CMD [ "python", "./run.py" ]
