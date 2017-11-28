# -*- coding: utf-8 -*-
import Tweet_Train_Test as ttt
import Tweet_Create_Dataset as tcd
from Log_Handler import Log_Handler as lh

logger = lh.log_initializer()
def tweet_main():
    try:
        #load the UI for user
        
        #ask user to enter a username for performing sentiment analysis on its tweets
        
        #take the user name and fetch tweets list for that user
        user_name = input("Enter the user name:\n")
        tweet_list = tcd.fetch_tweet(user_name)
        
        #create dataset
        train_head_count = 500
        test_head_count = 100
        raw_dataset_train, raw_dataset_test  = tcd.create_training_dataset(train_head_count, test_head_count)
        
        #setup the tweets for classifier
        training_dataset = ttt.tweet_setup(raw_dataset_train)
        testing_dataset = ttt.tweet_setup(raw_dataset_test)
        #train your classifier
        tweet_classifier = ttt.tweet_train(training_dataset)
        
        #validation to choose the right classifier. In our case we would be simply be using naive bayes classifier. So skipping this step
        ##---NA---##
        
        #test your classifier against the testing dataset for accuracy
        test_accuracy =  ttt.tweet_test_accuracy(tweet_classifier, testing_dataset)       
        print("\ntest_accuracy:" , str(test_accuracy))
        
        #pass the tweet list to your classifier for prediction
        sentiment_array, pos_tweets, neg_tweets = ttt.tweet_predict(tweet_classifier, tweet_list)
        print("\nsentiment_array: " + str(sentiment_array))
        print("\nPositive tweets count: " + str(len(pos_tweets)))
        print("\nNegative tweets count: " + str(len(neg_tweets)))
        
        #return the received response from prediction back to the UI classying among positives and negatives
        
    except Exception as Ex: 
        logger.error("Exception occurred in the tweet_main method| Exception:" + str(Ex))
 
     