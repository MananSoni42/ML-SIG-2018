# Tweet cleaner
cleanTweets.py contains a class of tweets that will help in removing unnecessary information from raw twitter data (text)
to use the class, make sure it is in the same directory as your file and the following lineat the begining of your python file:
```from cleanTweets import Tweet```

An example of how to use it is shown in readFromData.py   
Usage: ```python3 readFromData.py jan9-2012.txt```

A Sample dataset jan9-2012.txt has been provided. It contains **21051** tweets along with emotion labels for each. 
Using this class it took **1424.28 s** to clean all the tweets in the sample dataset. It takes an average of **0.068 s** to clean a tweet using this class 
