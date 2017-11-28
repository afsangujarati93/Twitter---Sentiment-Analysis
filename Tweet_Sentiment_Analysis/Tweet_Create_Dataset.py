# -*- coding: utf-8 -*-
import pandas as pd
from Log_Handler import Log_Handler as lh
import  tweepy
import json
from sklearn.model_selection import train_test_split

logger = lh.log_initializer()

def create_training_dataset(train_head_count, test_head_count):   
    try:        
      raw_dataset = pd.read_csv('DataSet/Sentiment Analysis Dataset.csv', header = 0, error_bad_lines=False)    
      raw_dataset['Sentiment'] = raw_dataset['Sentiment'].replace([1], 'positive')
      raw_dataset['Sentiment'] = raw_dataset['Sentiment'].replace([0], 'negative')
    
      raw_dataset = raw_dataset.drop('ItemID', 1)
      raw_dataset = raw_dataset.drop('SentimentSource', 1)
    
      columnsTitles = ['SentimentText', 'Sentiment']
      raw_dataset = raw_dataset.reindex(columns=columnsTitles)

      raw_dataset_train, raw_dataset_test = train_test_split(raw_dataset, test_size=0.2)
      
      raw_ds_final_train = create_pos_neg_dataset(raw_dataset_train, train_head_count)
      raw_ds_final_train = raw_ds_final_train.values 

      raw_ds_final_test = create_pos_neg_dataset(raw_dataset_train, test_head_count)
      raw_ds_final_test = raw_ds_final_test.values 
      
      return (raw_ds_final_train, raw_ds_final_test)
      
    except Exception as Ex: 
         logger.error("Exception occurred in the create_training_dataset method| Exception:" + str(Ex))
 
def create_pos_neg_dataset(raw_dataset, head_count):
    try:
        raw_dataset_pos = raw_dataset.loc[raw_dataset['Sentiment'] == 'positive']
        raw_dataset_pos = raw_dataset_pos.head(head_count)
#       print('\n Positive 100: ' + str(raw_dataset_pos))
      
        raw_dataset_neg = raw_dataset.loc[raw_dataset['Sentiment'] == 'negative']
        raw_dataset_neg = raw_dataset_neg.head(head_count)
#       print('\n Negative 100: ' + str(raw_dataset_neg)) 
        pos_neg_frames = [raw_dataset_pos, raw_dataset_neg]
        raw_dataset_pos_neg = pd.concat(pos_neg_frames)
        print("\n Positive tweets:" + str(len(raw_dataset_pos_neg[(raw_dataset_pos_neg['Sentiment'] == 'positive')])))
        print("\n Negative tweets:" + str(len(raw_dataset_pos_neg[(raw_dataset_pos_neg['Sentiment'] == 'negative')])))     
     
        return (raw_dataset_pos_neg)
    except Exception as Ex: 
         logger.error("Exception occurred in the create_training_dataset method| Exception:" + str(Ex))
     
    
def fetch_tweet(user_name):
    try:               
       #getting necessary keys and tokens from config file
       cofig_file = open("config.json").read()
       config_json = json.loads(cofig_file)
       consumer_key = config_json['twitter']['ConsumerKey']
       consumer_secret = config_json['twitter']['ConsumerSecret']
       access_token = config_json['twitter']['AccessToken']
       access_token_secret = config_json['twitter']['AccessTokenSecret']       
       api = IniTwitterApi(consumer_key, consumer_secret, access_token, access_token_secret)
       
       tweet_list = []
       file = open("tweets_" + user_name +".txt","a+", encoding="utf-8")
       for tweets in tweepy.Cursor(api.user_timeline, id = user_name, count=200).items():
            file.write(str(tweets.created_at) + "\t" + tweets.text + "\n\n")
            tweet_list.append(tweets.text)
       return tweet_list
    except Exception as Ex: 
         logger.error("Exception occurred in the fetch_tweet method| Exception:" + str(Ex))
 
def IniTwitterApi(consumer_key, consumer_secret, access_token, access_token_secret):
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)        
        api = tweepy.API(auth)
        return api
    except Exception as Ex:
        logger.error("Exception occurred in the IniTwitterApi method| Exception:" + str(Ex))

