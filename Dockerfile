FROM python:2
RUN pip install -r requirements.txt
CMD python app.py
