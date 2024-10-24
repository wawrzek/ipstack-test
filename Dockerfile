FROM python:3.13-alpine

RUN mkdir -p /app
WORKDIR /app

RUN addgroup -g 199 -S appuser && \
    adduser -u 199 -G appuser -S appuser && \
    chown appuser:appuser /app
USER appuser

COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY location.py /app

ENTRYPOINT ["python", "location.py"]
CMD ["10.1.1.1"]
