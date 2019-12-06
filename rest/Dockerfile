FROM python:3.8.0
RUN mkdir -p /vol/app
WORKDIR /vol/app
ADD requirements.txt .
RUN pip install -r requirements.txt
RUN echo "import nltk\nnltk.download('stopwords')" | python
RUN echo "import nltk\nnltk.download('wordnet')" | python
RUN echo "import nltk\nnltk.download('punkt')" | python
RUN rm requirements.txt
EXPOSE 8000
