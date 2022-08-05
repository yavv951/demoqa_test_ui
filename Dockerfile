FROM python

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV ENV=dev

CMD python -v -m pytest

