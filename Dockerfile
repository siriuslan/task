FROM python:3.8
COPY . /task_image
WORKDIR /task_image
RUN pip install -r requirements.txt
CMD ["python", "main.py"]


