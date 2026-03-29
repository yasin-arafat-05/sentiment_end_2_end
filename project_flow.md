
# ----- 1. SetUp the project structures: -----
- 1. create "venv" -> with uv 
- 2. add cookiecutter
- 3. run this on terminal: 
    ```bash
    cookiecutter -c v1 https://github.com/drivendata/cookiecutter-data-science
    ```
    - s3_bucket and aws_profile hit enter we will add those manually.
- 4. Rename src->models to only model
- 5. git push -> initial_commit

# ---- 2. SetUp Mlflow on Dagshub ----
- 1. Go to: https://dagshub.com/dashboard
- 2. Create > New Repo > Connect a repo > (Github) Connect > Select your repo > Connect
- 3. Copy experiment tracking url and code snippet. (Also try: Go To MLFlow UI)
- 4. pip install dagshub & mlflow
- 5. Run expriments(notebooks must track the expriment with mlflow)

`Must keep the Dagshub url,project_name in a constants.py file . Create src/config/__init__.py and constants.py file, expose constant. Then install the pip if using uv. then run pip install -r requirements.txt. if face any problem do "rm -rf build/ dist/ *.egg-info" and try to try it again. And restart the ipynb kernel.`



