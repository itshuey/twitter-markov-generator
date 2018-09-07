# twitter-markov-generator

This python project is composed of three units:
- markovGenerator reads .txt files and uses a Markov Chain algorithm to generate text in that style
- twitterScraper takes an input handle and stores the past 300 tweets in a .txt file
- main provides [interactive UI](mainUItwitter.png) that guides you through generating your own text

Unfortunately, twitterScraper is not a true web scraper, and relies on Twitter API and Tweepy. I obtained access tokens by applying through twitter's website, but as they expire, you will not be able to use the majority of this project without contacting me. Feel free to reach out to me [here](mailto:hssa2016@mymail.pomona.edu) or [obtain your own tokens](https://developer.twitter.com/content/developer-twitter/en.html).

Because of this, I have included a catalog of .txt files including Donald Trump and Barack Obama's recent tweets, as well as some of Shakespeare's sonnets. I will try to update this repository with new .txt files! I recommend running the main.py file, but I have included example function calls for the other files as well.

Enjoy!

.

.

.

p.s. Here are some mock Trump tweets!

```
In [30]: generateText(d,50)
```

```
Out[30]: 'The Boston Globe, which is making the President, when she says is a foreign power. We can,
         and that depends on in their currency, the ninth month since I know it’s “not presidential”
         to Troy loves the Pacific Ocean. Thank you. If I campaign colluded with his political '
```

```
In [31]: generateText(d,50)
```

```
Out[31]: 'Phony Dossier, FISA Court Judge. Fixing our workers! She is about Comey’s firing, afraid
         the U.S., our warfighters in the Democrat Thugs spent over nothing for Governor for the 
         rigged investigation he was a big and fast! Great Country....BUT WE ARE WINNING! Other
         Countries should be dropped? RT @realDonaldTrump: Troy '
```

```
In [32]: generateText(d,50)
```

```
Out[32]: "Congratulations to take out and for twenty years as 'pro-black' at Russia probe will be a spy
         - African American and countries use Page as an Alabama Coal Mine” https://t.co/IwLEO9ff9X 
         Lou Dobbs: “This is a job, tears in another way to Gregg Jarrett. https://t.co/TmICRUV9uo
         ...I say anything so Fake News "
```
