## Risk buddy


## Testing

Run all test with the following command:

```bash
python -m pytest -vvv -x
``` 

### Structure

```arduino

risk_buddy/
├── data/
│   ├── raw/
│   ├── processed/
│   └── models/
├── docs/
├── src/
│   ├── controller/
│   │   ├── fraud_detection.py
│   │   └── risk_assessment.py
│   ├── model/
│   │   ├── preprocessing.py
│   │   ├── fraud_detection_model.py
│   │   └── risk_assessment_model.py
│   └── view/
│       ├── dashboard.py
│       └── results.py
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── config/
│   ├── config.yaml
│   └── logging.yaml
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore


```

### Directories 

* **data/**: This directory contains the raw and processed data, as well as the trained models. The raw/ directory contains the raw data files, the processed/ directory contains the preprocessed data files, and the models/ directory contains the trained machine learning models.

* **docs/**: This directory contains the documentation for the project. This can include information on how to set up and run the project, as well as any technical documentation for the code.

* **src/**: This directory contains the source code for the AI project. The controller/ directory contains the Flask app and the controllers for handling user input and updating the Model and View components. The model/ directory contains the code for preprocessing the data and building the machine learning models. The view/ directory contains the templates and HTML files for displaying the results to the user.

* **tests/**: This directory contains the testing code for the AI project. The unit/ directory contains the unit tests for each module, the integration/ directory contains the integration tests for testing the interactions between the different modules, and the e2e/ directory contains the end-to-end tests for testing the entire system.

* **config/**: This directory contains the configuration files for the project. The config.yaml file contains the configuration for the Flask app, and the logging.yaml file contains the configuration for the logging.

* **requirements.txt**: This file contains the dependencies required by the project. This can include libraries such as Flask, pandas, scikit-learn, and matplotlib.

* **README.md**: This file contains information about the project and its usage. This can include instructions on how to set up and run the project, as well as any other relevant information.

* **LICENSE**: This file contains the license for the project. This can include information on how the code can be used and distributed.

* **.gitignore**: This file lists the files and directories that should be ignored by Git. This can include files such as logs, configuration files, and temporary files.


## Datasets

[Fraud detection dataset ](https://www.kaggle.com/datasets/dermisfit/fraud-transactions-dataset?resource=download)

#### It has the following columns:

* **trans_date_trans_time**: The date and time of the transaction.

* **cc_num**: credit card number.

* **merchant**: Merchant who was getting paid.

* **category**: In what area does that merchant deal.

* **amt**: Amount of money in American Dollars.

* **first**: first name of the card holder.

* **last**: last name of the card holder.

* **gender**: Gender of the cardholder.

* **street**:Street of card holder residence

* **city**:city of card holder residence

* **state**:state of card holder residence

* **zip**:ZIP code of card holder residence

* **lat**:latitude of card holder

* **long**:longitude of card holder

* **city_pop**:Population of the city

* **job**:trade of the card holder

* **dob**:Date of birth of the card holder

* **trans_num**: Transaction ID

* **unix_time**: Unix time which is the time calculated since 1970 to today.

* **merch_lat**: latitude of the merchant

* **merch_long**:longitude of the merchant

* **is_fraud**: Whether the transaction is fraud(1) or not(0)



## Tech stack 

Tech used in this application

- [Flask](https://flask.palletsprojects.com/en/2.2.x/quickstart/)
- [d3.js](https://d3js.org/)
- [Pandas](https://pandas.pydata.org/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [matplotlib](https://matplotlib.org/)
- [Ui templates to try](https://www.codementor.io/@chirilovadrian360/flask-website-templates-open-source-seed-projects-1b6tya9jnl)
- [Spectre.css](https://picturepan2.github.io/spectre/getting-started.html)
- [Ruff](https://beta.ruff.rs/docs/) Need to add!