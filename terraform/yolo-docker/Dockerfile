FROM bitnami/pytorch:latest
WORKDIR /code
COPY . .

# for yolov5 model
COPY .cache /.cache

#for opencv dependencies:
USER 0
RUN apt update
RUN apt install ffmpeg libsm6 libxext6  -y

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]