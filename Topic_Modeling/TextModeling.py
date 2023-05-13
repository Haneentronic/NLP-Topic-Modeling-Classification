import pandas as pd
from Topic_Modeling.Cleaning import Cleaning
from Topic_Modeling.Preprocessing import Preprocessing

""" Data Reading """
data_frame = pd.read_csv("../Dataset/articles.csv")

""" Data Cleaning """
cleaning = Cleaning(data_frame)

""" 1- Handel Missing values """
""" a- Handel columns with missing values """
# Remove url column because it's empty(100% null values)
cleaning.drop_column("url")

""" b- Handel rows with missing values """
# Drop rows contain null values
data_frame.dropna(inplace=True)

""" 2- Handel columns data types """
data_frame = data_frame.astype({"title": "string",
                                "publication": "string",
                                "author": "string",
                                "date": "datetime64",
                                "year": "int64",
                                "month": "int64",
                                "content": "string"})

# applying preprocessing
preprocessing = Preprocessing(data_frame)
preprocessing.drop_column("id")
