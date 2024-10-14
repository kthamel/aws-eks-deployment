FROM python
WORKDIR /tmp

COPY requirements.txt ./
COPY app.py /tmp/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9001
CMD ["python3", "app.py"]
