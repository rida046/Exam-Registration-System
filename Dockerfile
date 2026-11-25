FROM python:3.14

WORKDIR /exam

COPY exam_registration.py .

CMD ["python", "exam_registration.py"]