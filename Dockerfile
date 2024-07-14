FROM python:3.12
ADD main.py .
RUN apt-get update && apt-get install libzbar0 -y && apt-get install libgl1 -y 
COPY requirements.txt .
# RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]