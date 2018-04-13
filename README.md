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

- *newsAnalysis/createModel.py* trains a word embedding based on documents stored in a database. To connect to the database the user has to provide its name, host, port, user and password. Together with the desired number of documents used for training the word embeddings, these properties are the input arguments of the function.

- *newsAnalysis/evaluateScript.py* computes the accuracy of a word embedding model. Google generated analogies that show how well a model has learnt the relations in a specific field, e.g. *Tokyo:Japan::Oslo:Norway*, *sister:brother::niece:nephew*, etc. Besides semantic relations also word forms are tested, e.g. *sleeping:slept::dancing:danced*, *cool:coolest::weird:weirdest*, etc.
To load the model the number of documents is required.

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

model = Model(name)
if model.exists():
    model.load()
else:
    model.create(data_path)
    model.save()

model.evaluate()
```

