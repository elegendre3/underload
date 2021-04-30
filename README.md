# UnderLoad -- News app fpr when your overloaded

## - Headlines - 
### Gives you regular unfiltered News Headlines



## - Tailor - 
### Gives you hand-picked News Items based on your inputed interests




## TODO
ENG:
- try to fix the hacky build. Maybe build.sh for now (CP static dir)
- make gunicorn work with static files (img and css)

- SPEED
-- speeding up tailor search and-or cache
-- need to do smthg.. more interests will mean more searches, not viable
-- Filtering headlines? Replacing tailor..? ...
-- multiproc queries..? use all available cores

- Persistence of interests in Mongo DB .. and articles..?
-> Track age and articles, and requests/day?

- Mongo DB (docker-compose)
-- store users, keys and interests
-- Quick user auth + NewAPI sign up link to get and store API Key
- -> Interests page render?


FUNC
- UK News?
- tailor: Allow searching results in French



### Author 
Eliott Legendre 
