# < UnderLoad >
## A News app that will not overload you with irrelevant information

## - Tailor - 
### Gives you hand-picked News Items based on your inputed interests (RED)

## - Headlines - 
### Gives you regular unfiltered News Headlines (BLUE)


## TODO
ENG:
- make gunicorn work with static files (img and css) (and secret!)
- refactor the messy lib


SPEED
- speeding up tailor even more, test scaling capacity with growing interests 
- -> or Filtering headlines?


PRODUCT
- Home Button

- Persistence of interests in Mongo DB .. and articles..?
-> Track age and articles, and requests/day?
  
- Quick user auth  (how do you deal with the API key..? Make them sign up?)
- -> Interests page render?


FUNCTIONAL
- UK News?
- tailor: Allow searching results in French


## User Guide
### Depdendencies
Using:
- NewsAPI
- Flask
- PyBuilder & PyBuilderDocker

### Build & Run
```pyb publish```

```docker run -v /Users/eliott.legendre/Desktop/test_mount/news_api.secret:/mnt/news_api.secret -p 0.0.0.0:8080:8080 underload:0.0.1 ```

### Author 
Eliott Legendre 
