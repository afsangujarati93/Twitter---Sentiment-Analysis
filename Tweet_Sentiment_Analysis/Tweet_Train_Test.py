# -*- coding: utf-8 -*-
#Below code is implemented following the steps mentioned on website:
#https://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/

import nltk
from Log_Handler import Log_Handler as lh

logger = lh.log_initializer()
distinct_word_list = []


def tweet_setup(train_dataset):
    try:        
        tweets_array = []    
        for (words, sentiment) in train_dataset:
            #splitting every tweet into list of words and ignoring those with length lesser than 3
            words_array = [e.lower() for e in words.split() if len(e) >= 3]
#            print("\nwords_array: " + str(words_array))
            tweets_array.append((words_array, sentiment))
        distinct_word_list = get_distinct_words_list(extend_tweets_words(tweets_array))
        training_dataset = nltk.classify.apply_features(label_tweet_array, tweets_array)
        return training_dataset
    except Exception as Ex:
        logger.error("Exception occurred in the tweet_setup method| Exception:" + str(Ex))
      
def extend_tweets_words(tweets):
    try:        
        word_list = []
        for (words, sentiment) in tweets:
          word_list.extend(words)
        return word_list
    except Exception as Ex:
        logger.error("Exception occurred in the extend_tweets_words method| Exception:" + str(Ex))
 

def get_distinct_words_list(word_list):
    try:        
        global distinct_word_list
        #getting the frequency of words in the word_list i.e. their occurance count and sorting
        word_list = nltk.FreqDist(word_list)
        #getting only the words and not the count of occurance through keys    
        distinct_word_list = word_list.keys()
        file= open("word_list.txt", "w+")
        file.write(str(distinct_word_list))
        file.close()
        return distinct_word_list
    except Exception as Ex:
        logger.error("Exception occurred in the get_distinct_words_list method| Exception:" + str(Ex))
 

#this method checks every tweet array in the distinct word list 
#and marks appropriate words
#as either true or false depending if they exists in the list 
#Also, this method is triggered by apply_features method in nltk library
def label_tweet_array(document): 
    try:        
        document_dict = set(document)
        labeled_array = {}        
        for word in distinct_word_list:
            labeled_array['contains(%s)' % word] = (word in document_dict)        
        return labeled_array
    except Exception as Ex:
        logger.error("Exception occurred in the get_distinct_words_list method| Exception:" + str(Ex))
 

def tweet_train(training_dataset):
    try:
        tweet_classifier = nltk.NaiveBayesClassifier.train(training_dataset)
        return tweet_classifier
    except Exception as Ex:
        logger.error("Exception occurred in the tweet_train method| Exception:" + str(Ex))

def tweet_test(tweet_classifier, test_dataset):
    try:
        tweet_sentiment_array = []
        pos_tweets = []
        neg_tweets = []
        for tweet in test_dataset:
            sentiment = tweet_classifier.classify(label_tweet_array(tweet.split()))
            tweet_sentiment_array.append((tweet, sentiment))
            if sentiment == 'positive':
                pos_tweets.append((tweet, sentiment))
            elif sentiment == 'negative':
                neg_tweets.append((tweet, sentiment))
        return (tweet_sentiment_array, pos_tweets, neg_tweets)
    except Exception as Ex:
        logger.error("Exception occurred in the tweet_train method| Exception:" + str(Ex))
   
    