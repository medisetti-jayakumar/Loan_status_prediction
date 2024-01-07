import os
from pathlib import Path

package_name = "loan_prediction_app"

list_of_files = [
    "Dataset/credit_train.csv",
    "Flask App/static/style.css",
    "templates/app.py",
    "templates/chargedoff.html",
    "templates/fullypaid.html",
    "templates/loanstatus.html",
    "Training/Loan status preparation.ipynb",
    "app.py",
    "Procfile",
    "requirements.txt"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # create an empty file

