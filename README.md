# machinelearning_python_rest_api

1) It is a python based REST API, deployed to Heroku platform. 
2) It uses **Machine Language(ML)** to predict the provisions needed to be loaded, based on the passenger count.
3) The Machine language(ML) model is trained with historical data. Once trained the model is saved as joblib(flight-provision.joblib) object.\
4) The model is trained with data in **Jupyter notebook "jupyter_notebook.ipynb"**, and is saved as "flight-provision.joblib".
5) The model is trained with the data in "**flight_provision.csv**" file.
6) It uses python "pandas", "sklearn" and "decision tree" python libraries.
7) The joblib model is being used in the REST API(**app.py**). It takes the passenger count as input and returns the provisions needed.
8) This is developed for Demo.
