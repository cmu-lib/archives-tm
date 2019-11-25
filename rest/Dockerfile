FROM python:3.7.5
RUN mkdir -p /vol/app
WORKDIR /vol/app
ADD requirements.txt .
RUN pip install -r requirements.txt
RUN echo "import nltk\nnltk.download('stopwords')\nnltk.download('wordnet')" | python
RUN rm requirements.txt
EXPOSE 8000
