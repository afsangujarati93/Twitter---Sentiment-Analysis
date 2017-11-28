# -*- coding: utf-8 -*-
import Tweet_Train_Test as ttt
import Tweet_Create_Dataset as tcd
import Tweet_Main as tm

pos_tweets = [('I love this car', 'positive'),
              ('This view is amazing', 'positive'),
              ('I feel great this morning', 'positive'),
              ('I am so excited about the concert', 'positive'),
              ('He is my best friend', 'positive')]


neg_tweets = [('I do not like this car', 'negative'),
              ('This view is horrible', 'negative'),
              ('I feel tired this morning', 'negative'),
              ('I am not looking forward to the concert', 'negative'),
              ('He is my enemy', 'negative')]

tweet_test_dataset = [
                     'I am not happy', 
                     'Your song is annoying', 
                     'Larry is my friend', 
                     'I am happy',
                     'omg its already',
                     'you are disgusting',
                     'suck off',
                     'I don''t like you'
                     ]


#train_dataset = pos_tweets + neg_tweets   
#training_dataset = ttt.tweet_setup(train_dataset)
#file= open("training_dataset.txt", "w+")
#file.write(str(training_dataset))
#file.close()
##print("\ntraining:" + str(training_dataset))
#tweet_classifier = ttt.tweet_train(training_dataset)
#sentiment_array = ttt.tweet_test(tweet_classifier, tweet_test_dataset)
#print("\nsentiment_array: " + str(sentiment_array))

tm.tweet_main()
