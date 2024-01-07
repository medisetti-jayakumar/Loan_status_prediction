# Loan_status_prediction

![Alt text](<Flask App/image_folder/Screenshot 2024-01-07 003933.png>)

This app predicts the loan status of the client as charged-off or fully-in-paid by feeding the required inputs likr credit score, annual income, job experience etc.....

![Alt text](<Flask App/image_folder/Screenshot 2024-01-07 001922.png>)

-------------------------------------------------------------------

## create the folder structure as required:
-Run the template.py file to create the folder structure

    python template.py
## create the environment and activate the environment
    conda create -n env python==3.8 -y
    conda activate env

## install the requirements.txt
    pip install -r requirements.txt

## Import the dataset
[click-here-for-dataset](https://raw.githubusercontent.com/medisetti-jayakumar/Loan_status_prediction/main/Dataset/credit_train.csv)

Machine Learning is indispensable for the beginner in Data Science, this dataset allows you to work on supervised learning, more preciously a classification problem. This is the reason why I would like to introduce you to an analysis of this one.

We have data of some predicted loans from history. So when there is name of some ‘Data’ there is a lot interesting for ‘Data Scientists’. I have explored dataset and found a lot interesting facts about loan prediction.

## preprocess, cleaning, Analysis and model buiding
[click here for jupyter](https://github.com/medisetti-jayakumar/Loan_status_prediction/blob/main/Training/Loan%20Status%20Prediction.ipynb)

### Save the model by using joblib
    import joblib
    joblib.load(model_name,"loan_model.pkl")
## write a HTML code for Input and Result pages

- [loan_status.html](https://github.com/medisetti-jayakumar/Loan_status_prediction/blob/main/templates/loanstatus.html)

- [Charged_off.html](https://github.com/medisetti-jayakumar/Loan_status_prediction/blob/main/templates/chargedoff.html)

- [fully_paid.html](https://github.com/medisetti-jayakumar/Loan_status_prediction/blob/main/templates/fullypaid.html)

## Create application using flask

[application_code](https://github.com/medisetti-jayakumar/Loan_status_prediction/blob/main/app.py)

    - creation of app for the input features
    - load the machine learning model as

       | joblib.load("loan_model.pkl") |

    - assign the html code to return the final result page
## Result

Input page:
![Alt text](<Flask App/image_folder/Screenshot 2024-01-07 003933.png>)

    After feeding all the inputs,
    the result is < 1 i.e Charged-off
    The result is >= 1 i.e Fully-paid 
If the result as Charged off:
![Alt text](<Flask App/image_folder/Screenshot 2024-01-06 235837.png>)

with background image![Alt text](<Flask App/image_folder/Screenshot 2024-01-07 000627.png>)

If the result is fully-paid, then it looks like:
![Alt text](<Flask App/image_folder/Screenshot 2024-01-07 001922.png>)