FROM python:3.7-slim

WORKDIR /demo

COPY . .

RUN pip install -r ./requirements/dev.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD [ "flask", "run", "--host", "0.0.0.0"]
