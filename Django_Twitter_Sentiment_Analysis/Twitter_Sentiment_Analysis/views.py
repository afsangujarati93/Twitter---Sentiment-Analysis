from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from Twitter_Sentiment_Analysis.Log_Handler import Log_Handler as lh
from django import forms
from Twitter_Sentiment_Analysis.Tweet_Main import Tweet_Main as tm

class NameForm(forms.Form):
    user_name = forms.CharField(label = '', max_length=100, widget=forms.TextInput(
        attrs={
            'class':'form-control input-lg',
            'style': 'margin-top: 20px',
            'placeholder':'Username'
        }))

logger = lh.log_initializer()
def index(request):
    try:
        #load the UI for user
        #ask user to enter a username for performing sentiment analysis on its tweets
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = NameForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                user_name = form.cleaned_data['user_name']
                sentiment_array, pos_tweets, neg_tweets = tm.Tweet_Router(user_name)
                
                str_pos_tweets = '\n\n'.join(pos_tweets)
                str_neg_tweets = '\n\n'.join(neg_tweets)

                pos_tweets_count = len(pos_tweets)
                neg_tweets_count = len(neg_tweets)
                total_tweets = (pos_tweets_count + neg_tweets_count)
                print('\npos tweets count:' + str(pos_tweets_count))
                print('\nneg tweets count:' + str(neg_tweets_count))

                pos_tweet_percent = round((pos_tweets_count/total_tweets)*100, 2)
                neg_tweet_percent = round((neg_tweets_count/total_tweets)*100, 2)
                print('\npos tweets percent:' + str(pos_tweet_percent))
                print('\nneg tweets percent:' + str(neg_tweet_percent))
                # pos_tweet_1 = str(pos_tweets)
                # print ('\npos_tweets' + str_pos_tweets)
                 #return the received response from prediction back to the UI classying among positives and negatives
                return render(request, 'analysis_ouput.html', {
                    'username' : user_name,
                    'postweets': str_pos_tweets,                    
                    'negtweets': str_neg_tweets,
                    'postweetscount': str(pos_tweets_count),
                    'negtweetscount': str(neg_tweets_count),
                    'postweetpercent':str(pos_tweet_percent),
                    'negtweetpercent':str(neg_tweet_percent),
                    })
                # return HttpResponse()
                # return HttpResponseRedirect('/thanks/')
            # if a GET (or any other method) we'll create a blank form
        else:
            form = NameForm()
        return render(request, 'index.html', {'form': form})

    except Exception as Ex: 
        logger.error("Exception occurred in the index method| Exception:" + str(Ex))
        return render(request, 'index.html')
        # return HttpResponse("Exception occurred in the index method| Exception:" + str(Ex))

