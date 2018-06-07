## NewsAnalysis

Trains, evaluates and analyses newspaper word embeddings.

## Install dependencies
To install the dependencies make sure you have [Python 2.7](https://www.python.org/download/releases/2.7/) and [pip](https://pip.pypa.io/en/stable/) installed. Clone or download the repository.

Upgrade pip:
```
pip install -U pip
```

Install the dependencies with:
```
pip install -r requirements.txt
```
Add models directory:
```
mkdir models
```

## Word Embeddings
- *newsAnalysis/createDatabase.py* accesses a SQL database to write the first n articles with information about title, text, the date of publication, article and newspaper id to a csv file.To connect to the database provide its name, host, port, user and password have to be provided.

- *newsAnalysis/Model.py* trains a word embedding, fasttext or word2vec, based on documents stored in a csv file.
Google generated analogies that show how well a model has learnt the relations in a specific field, e.g. *Tokyo:Japan::Oslo:Norway*, *sister:brother::niece:nephew*, etc. Besides semantic relations also word forms are tested, e.g. *sleeping:slept::dancing:danced*, *cool:coolest::weird:weirdest*, etc. With *evaluate()* the results of the trained word embedding model are displayed
Storing a model in a tsv file enable its visualization with the [tensorflow embedding proyector](
://projector.tensorflow.org/).


We recommend to create a shell or python script to specify the parameters and execute the different steps:

```
from createDatabase import createDatabase
from createModel import createModel
from evaluateModel import evaluateModel

DB='DatabaseName'
HOST='HostName'
PORT=PortNumber
USER='UserName'
PASSWORD='Password'

NR_DOCS=100000

name = 'dataName' + str(NR_DOCS)
data_path ='./data/' + name + '.csv'

if not os.path.exists(data_path):
    createDatabase(DB, HOST, PORT, USER, PASSWORD, data_path, NR_DOCS)

# use either fasttext or word2vec as modelType
model = Model(name=name, modelType='fasttext')

if model.exists():
    model.load()
else:
    model.create(data_path)
    model.save()

model.evaluate()
model.to_tsv()
```

## Acceptance Test
To ensure that your work also runs as you intended on other machines, please run an acceptance test.

To do this first copy the `docker-compose.yml.example` file and name it `docker-compose.yml`. Next fill in the environment 
variables with your values. 

Now you can build and run the acceptance test. 
```
docker-compose build
docker-compose up
```

This will create a docker container that will install all the requirements from requirements.txt and runs the 
newsAnalysis.run.py file. The generated data will be stored in the ./data dir that is created by this process.

