# Topic Modeling Classification
This project explores topic modeling in natural language processing (NLP) using Python. Topic modeling is a method for finding a group of words (i.e. topics) from a collection of documents that best represents the information in the collection of text documents. The goal is to extract topics from a set of documents using the **TF-IDF** method for information extraction and three clustering algorithms: **K-means**, **DBSCAN**, and **Hierarchical Clustering**.

## Data
The input data consists of a set of text documents in a CSV file. 
The file contains 9 columns: `id`, `title`, `publication`, `author`, `date`, `year`, `month`, `url` and `content`. 
| Column      | Description |
| ----------- | ----------- |
|id | column contains a unique identifier for each document |
| title | column contains the raw text of each document |
| publication | column contains the puplication source name for each document |
| author | column contains the authors' names for each document |
| date | column contains the full-date of publication for each document |
| year | column contains the year of publication for each document |
| month | column contains the month of publication for each document |
| url | column contains the topic link for each document |
| content | column contains the raw text of each document |

## Data Cleaning
1. **Handel Missing values**
    1. _Handel columns with missing values_: by remove `url` column because it's empty(100% null values).
    2. _Handel rows with missing values_: by drop all rows contain null values.
2. **Handel columns data types**
    ```
    data_frame= data_frame.astype({"title": "string",
                                   "publication": "string",
                                   "author": "string",
                                   "date": "datetime64[ns]",
                                   "year": "int64",
                                   "month": "int64",
                                   "content": "string"})
    ```
3. **Dealing with unnecessary columns**
    1. Drop `id` column because it contain unnecessary unique values.
    2. Extract day from `date` column and rename column to day.

## Preprocessing for text data
The text data is preprocessed using the following steps:
1. Convert string column to lowercase.
2. Remove HTML Tags using regular expression.
3. Remove URLs using regular expression.
4. Remove unnecessary word like: publication name from title using regular expression.
5. Apply Tokenization using the nltk library: 
    1. Apply **sentence tokenization** to split text into sentences.
    2. Apply **word tokenization** to split sentences into individual words.
6. Apply Stop word removal: Common stop words (such as "a", "an", "the", etc.) are removed from the text using the nltk library.
7. Remove Punctuations using regular expression and string library.
8. Remove Special Characters using regular expression.
9. Remove invalid indexes in lists.
    1. Remove empty indexes.
    2. remove cells contain one character.
10. Remove most frequently 10 words.
11. Remove most rare 10 words.
12. Apply Stemming: The remaining words are stemmed using the Porter stemming algorithm from the nltk library.
13. Apply POS and Lemmatization: The remaining words are lematized using the wordnet lemmatizer  algorithm from the nltk library.

## Dealing with categorical data (Nominal Data).
1. Preprocess `Puplication` by apply one-hot encoding.
2. Preprocess `author` by splitting authors in a list and applying mapping on them.

## Feature Extraction
`TF-IDF vectorization`: The preprocessed text is converted into a matrix of TF-IDF feature vectors using the sklearn library.

## Clustering
The TF-IDF feature vectors are clustered using three different clustering algorithms:
| Algorithm   | Details |
| ----------- | ----------- |
| K-means | K-means is a centroid-based clustering algorithm that partitions the data into K clusters based on the Euclidean distance between the data points and the cluster centroids. |
| DBSCAN | DBSCAN is a density-based clustering algorithm that groups together data points that are close together in a high-density region, and separates out data points in low-density regions. |
| Hierarchical Clustering | Hierarchical Clustering is a clustering algorithm that groups together similar data points based on their distance from each other in a hierarchical structure. |


The resulting clusters are then analyzed to identify the most common topics in the data.

## Results
The results of the topic modeling analysis are presented in a set of visualizations, including:
- A scatter plot of the DBSCAN Clusters.
- A scatter plot of the Hierarchical Clustering Clusters.

## Usage
To run the project, 
- You will need to install the required Python libraries listed in the `requirements.txt` file.
- Run this code to install _stopwords_ and _wordnet_
    ```
    nltk.download(‘stopwords’)
    nltk.download(‘wordnet’)
    ```
- You will also need to provide a download CSV file from [here](https://files.fm/u/9yxgtuwh4).

## Visualization
- Word cloud for title column

![title](https://github.com/NourAyman10/NLP-Topic-Modeling-Classification/assets/83882344/17b62f16-d90f-4235-a52b-ef3ff5c87817)

- Word cloud for content column
  
![content](https://github.com/NourAyman10/NLP-Topic-Modeling-Classification/assets/83882344/5f405fc7-c878-4532-a391-32e1fc8dd916)

- DBSCAN Clustering

![DBSCAN](https://github.com/NourAyman10/NLP-Topic-Modeling-Classification/assets/83882344/695b4376-3552-45a2-bdb4-fe6b7fd280b3)

- Hierarchical Clustering
  
![HierarchicalClustering](https://github.com/NourAyman10/NLP-Topic-Modeling-Classification/assets/83882344/27439b99-fabf-4e77-8a03-c0e994ee1906)

## Credits
This project was created by:
- [**Abdelrhman Sayed**](https://github.com/Abdelrhman-Sayed70)
- [**Nour Ayman**](https://github.com/NourAyman10)
- [**Ruqaiyah Mohammed**](https://github.com/25Ruq)
- [**Heba Tarek**](https://github.com/hebatarekkamal) 
- [**Haneen Ibrahim**](https://github.com/HaneenIbrahim2)
- [**Mariam Ahmed**](https://github.com/MariamAhmeddd)
