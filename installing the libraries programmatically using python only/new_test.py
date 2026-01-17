import pip 
lib=["scikit-learn","tensorflow","Fastapi[all]","pydantic"]

for i in lib:
    try:
        pip.main(['install',i , '--quiet'])
        print(f"Master your wish to install the libraries has been fullfilled programmatically as your lazy bitch assa  idiot to do it yourself")
    except Exception as e:
        print(f" An error occurred while installing {i}: {e} master . I quess your have move your mighty but lazy ass to do it yourself old way")