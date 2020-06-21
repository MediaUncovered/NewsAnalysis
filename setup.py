from setuptools import setup

setup(
    name="newsanalysis",
    version="0.1.0",

    url="https://github.com/MediaUncovered/NewsAnalysis",
    description="use word embeddings to uncover bias in newspapers",
    long_description=open("README.md").read(),

    packages=["newsAnalysis"],
    include_package_data=True,

    install_requires=[
        "sqlalchemy==1.1.11",
        "sqlalchemy-utils==0.32.14",
        "gensim>=3.7",
        "nltk==3.4.5",
        "unicodecsv==0.14.1",
        "psycopg2==2.7.1",
        "numpy>=1.15",
        "matplotlib==2.2",
        "nose==1.3.7",
        "responsibly==0.1.1",
    ],
)
