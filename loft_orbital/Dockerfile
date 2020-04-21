FROM python:3.7.3-slim
MAINTAINER Sergey Kuznetsov
RUN apt-get update && apt-get install -y python
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
ADD loft_orbital.py /loft_orbital/loft_orbital.py
ADD test_loft_orbital.py /loft_orbital/test_loft_orbital.py
CMD ["/loft_orbital/loft_orbital.py"]
ENTRYPOINT ["python"]