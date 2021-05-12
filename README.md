# tfg_2021
All data and code related to the devlopement of The Emotions Behind the Stock Market
**By: Luis Guillermo Velasco**

Hopefully this can bue used as a guideline to for future projects in the field of NLP financial sentiment recognition.

## Scraping
* Contains Python code used to to scarpe tweets from Twitter and posts from Reddit (r/wallstreetbets)
#### Major libraries used
* twint (https://github.com/twintproject/twint)
* psaw (https://pypi.org/project/psaw/)

## Cleaning & Splitting
* Contains jupyter noteebooks used for data cleaning and splitting 
#### Major libraries used
* regex
* sci-kit learn (https://scikit-learn.org/stable/install.html)
* pandas (https://pandas.pydata.org/docs/)

## BERT_sentiment.ipynb
* Method used to fine-tune BERT model in order to classify bearish and bullish tweets
* Due to computational limitations, only the BERT-base model
#### Major libraries used
* tensorflow (https://www.tensorflow.org/resources/models-datasets)
* transformers (https://huggingface.co/transformers/)
* sci-kit learn (https://scikit-learn.org/stable/install.html)
* pandas (https://pandas.pydata.org/docs/)

### Results obtained in the iteration used to compute TFG results
<img width="304" alt="Screenshot 2021-05-12 at 1 48 12 PM" src="https://user-images.githubusercontent.com/42964815/117970713-42c26800-b329-11eb-997a-24f80bda9bb0.png">

## Data
#### man_training_data.csv
* Contains 800 labelled tweets/posts used for training the BERT model
* 400 bearish (negative)
* 400 bullish (positive)
#### man_test_data.csv
* Contains 100 labelled tweets/posts used for training the BERT model
* 50 bearish (negative)
* 50 bullish (positive)
#### man_validation_data.csv
* Contains 100 labelled tweets/posts used for training the BERT model
* 50 bearish (negative)
* 50 bullish (positive)
