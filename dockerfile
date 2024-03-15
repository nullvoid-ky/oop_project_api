FROM python:3.11

WORKDIR /code 

COPY . .

ENV JWT_SECRET=cmplNxCuy9S9EK2DVE6nvV8BNSRNccEq

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]