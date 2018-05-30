'''
cleanTweets.py - Class to remove unnecesary information from a tweet
Author - Manan Soni (BITS ACM) (github: MananSoni42)
'''

from nltk.tokenize import sent_tokenize,word_tokenize,TweetTokenizer
from pattern3.en import suggest
import hunspell
import re
import copy

class Tweet:
    def __init__(self,sen):
        if not isinstance(sen,str):
            raise TypeError('Expected: ' + str(type('a')) + ' received: ' + str(type(sen)))
        t = TweetTokenizer(strip_handles=False,reduce_len=True)
        self.sen = t.tokenize(sen)

        self.tok = t.tokenize(sen)
        self.original = sen

    def __repr__(self):
        return self.original

    def defaultClean(self):
        '''
        Parameters: None
        Description: perform each of the class functions on the tweet
        Returns: tokenized tweet
        '''
        self.remNewLine(origTweet=False)
        self.remEmojis(origTweet=False)
        self.remEmoticons(origTweet=False)
        self.remHash(origTweet=False)
        self.replName(origTweet=False)
        self.sepChar(origTweet=False)
        self.spellCorrect(origTweet=False)

        return self.sen
    def remNewLine(self,origTweet=True):
        '''
        Parameters: None
        Description: remove all instances of New line (\n) from the Tweet
        Returns: tokenized tweet
        '''

        if origTweet:
            line = copy.copy(self.tok)
        else:
            line = self.sen

        for word in line:
            line[line.index(word)].replace('\n','')

        self.sen = line
        return line

    def remEmojis(self,origTweet=True):
        '''
        Parameters: None
        Description: Remove all characters that have Unicode code > 128 (mostly emojis)
        Returns: tokenized tweet
        '''

        if origTweet:
            line = copy.copy(self.tok)
        else:
            line = self.sen

        for word in line:
            line[line.index(word)] = ''.join([c for c in word if ord(c)<128])
        self.sen = line
        return line

    def getTweet(self,orig = False,origTweet=True):
        '''
        Parameters: orig = True/False
        Description:returns original(unmodified) tweet if orig=True otherwise returns modified tokenized tweet
        Returns: tokenized tweet
        '''
        if orig is True:
            return self.original
        else:
            return self.sen

    def remEmoticons(self,origTweet=True):
        '''
        Parameters: None
        Description: Remove emoticons like :)
        Returns: tokenized tweet
        '''

        if origTweet:
            line = copy.copy(self.tok)
        else:
            line = self.sen

        #define relevant emoticons
        emh = [':-)',':)',':-]',':]',':-3',':3',':->',':>','8-)','8)',':-}',':}',':o)',':c)',':^)','=]','=)',':-D',':D','8-D','8D','x-D','xD','X-D','XD','=D','=3','B^D',':-))',':\'-)',':\')']
        ems = [':-(',':(',':-c',':c',':-<',':<',':-[',':[',':-||','>:[','>:{',':@','>:(',':\'-(',':\'(']
        emr1 = ['D-\':','D:<','D:','D8','D;','D=','DX',':-o',':o',':-O',':O',':-0','8-0','>:O',':-*',':*',':x',':x']
        emr2 = [';-)',';)','*-)','*)',';-]',';]',';^}',':-,',';D',':-P',':P','X-P','XP','xp','x-p','xp',':-p',':p',':-b',':b','d:','=p','>:P']
        emr3 = [':-/',':/',':-.','>:\\','>:/',':\\','=/','=\\',':L','=L',':S',':-|',':|',':$',':-X',':X',':-#',':#',':-&',':&']
        emr4 = [';\'(','O:-)','O:)','O:-3','O:3','0:-3','0:3','0:-)','0:)','0;^)','>:-)','>:)','}:-)','}:)','3:-)','3:)','>;)','|;-)','|-O',':-J','<:-|','\',:-|','%-)','%)']
        em = emh + ems + emr1 + emr2 + emr3 + emr4
    	#remove emoticons
        for c in line[:]:
            if c in em:
                del line[line.index(c)]
        self.sen = line
        return line

    def remHash(self,origTweet=True):
        '''
        Parameters: None
        Description: Replace #word with word
        Returns: tokenized tweet
        '''

        if origTweet:
            line = copy.copy(self.tok)
        else:
            line = self.sen

        line = [c.strip('#') for c in line]
        self.sen = line
        return line

    def sepChar(self,origTweet=True):
        '''
        Parameters: None
        Description: Replace myNewWord with my New Word (camelCase)
        Returns: tokenized tweet
        '''

        if origTweet:
            line = copy.copy(self.tok)
        else:
            line = self.sen

        for word in line:
            if re.search(r'[a-z]+[A-Z][a-z]+',word)!=None:
                temp = re.findall(r'[a-zA-Z][^A-Z]*',word)
                ind = line.index(word)
                if ind is len(line)-1:
                    line = line[:ind] + temp
                elif ind is 0:
                    line = temp + line[ind+1:]
                else:
                    line = line[:ind] + temp + line[ind+1:]
        self.sen = line
        return line

    def spellCorrect(self,origTweet=True):
        '''
        Parameters: None
        Description: Correct spelling mistakes using the hunspell engine
        if origTweet:
        Returns: tokenized tweet
        '''

        if origTweet:
            line = copy.copy(self.tok)
        else:
            line = self.sen

        hspell = hunspell.HunSpell('/usr/share/hunspell/en_US.dic', '/usr/share/hunspell/en_US.aff')

        #pass it through a spell checker - hunspell
        for i in range(len(line)):
            flag = False
            for c in [',','.','!','\'','"',';',':','?','&','/','\\','*','~','(',')','[',']','{','}','$','%','^','-','_','+','=','|','<','>']:
                if c in line[i]:
                    flag = True
                    break
            if (not hspell.spell(line[i])) and line[i] != "**NAME**" and flag == False:
                line[i] = hspell.suggest(line[i])[0]
        self.sen = line
        return line

    #replace @name with **name**
    def replName(self,name = '**NAME**',origTweet=True):
        '''
        Parameters: Word to replace @ mentions
        Description: Replace @Name with Arguement 1 (default is **NAME**)
        Returns: tokenized tweet
        '''

        if origTweet:
            line = copy.copy(self.tok)
        else:
            line = self.sen

        line = [word for word in line if word!='']

        try:
            for i in range(len(line)):
                if line[i][0]=='@':
                    line[i] = name
        except Exception as e:
            print('tweet:',line)
            print('Exception:',e)
        self.sen = line
        return line


if __name__ == '__main__':
    w = Tweet('@Manan ,I\'m lesving BITS today !! :] #freadom myNameIsManan')
    print('original:',w)
    print('cleaned:',w.defaultClean())
