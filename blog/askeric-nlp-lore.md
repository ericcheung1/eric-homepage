---
title: About askeric-nlp and rambles about my personal projects
date: 10 Nov, 2026
description: More about the askeric-nlp project and the iterative process on how it got to its current state.
number: 0
---

I wanted to talk about the lineage of this project [askeric-nlp](https://github.com/ericcheung1/askeric-nlp) and how it sort of got here. The current state, as of the posting date, is a FastAPI web app serving a single page that takes in Reddit post URLs and does sentiment analysis and keyword extraction on 15 comments/replies. Separately, it also takes in standalone texts and does sentiment analysis on that as well. 


There is also an API route that accepts JSON and does sentiment analysis on the inputs but this feature isn’t as well thought out and isn’t as cleanly integrated so I don’t advertise it as much. This project has helped me learn tremendously, I’ve tried to optimize it using things like the FastAPI event loop, offloading things to threads, and using less resource intensive models. 


I would say I’ve done an okay job on its technical design and hope to improve it more in the future. Currently, it's hosted on a Digital Ocean droplet sitting behind Caddy as the reverse proxy, all containerized and running off Docker Compose. But these details can change so I will not touch upon them too much here.


This project is definitely my most well thought out and most complete to date, but I didn’t just come with the premise of this project in one sitting, it has evolved alongside me and kind of changed every time I learned something new whether it was from a class, my other projects, or from work.


I’ve only ever worked on one or two big personal projects because I like to go back and retry old stuff with new ideas. I first started working on personal projects around the Fall 2024 semester, roughly September to December, where I was starting the 3rd year of my economics undergrad. I had little exposure to coding at that point except for using R in my econometrics classes and random scripts/notebooks/general messing about with Python. 


That semester I took a class on statistical learning where I learned a bunch of classic machine learning algorithms from a statistical point of view and learned about data science concepts like bias-variance trade off and that sort of stuff. I was also actively looking for co-op opportunities as either a business analyst or data analyst. So I thought I would try my hand at using a ML model on a resume project. 


I made this small web scraping [script](https://github.com/ericcheung1/Projects/blob/main/nba-salary-prediction/nba_stats_scraper.py) with beautiful soup for pulling NBA stats from [basketball-reference.com](https://www.basketball-reference.com/) and I used my machine learning knowledge from class to build some [models](https://github.com/ericcheung1/Projects/tree/main/nba-salary-prediction) in R to predict player salaries using box score stats. 


I eventually started to get some interviews for co-op and one was even for a data science position that I randomly applied to. Getting that interview made me believe I could actually work in a more technical and coding adjacent role even though thinking back I was clearly not ready for that job at the time. 


I ended up not getting that data science job and this was in the spring 2025 now, roughly March, I decided to do a bigger and grander project next. I came up with an [idea](https://github.com/ericcheung1/canucks-sentiment) that analyzed comments on the r/canucks subreddit because I was and still am a big Canucks fan. Sidenote if you’re a Canucks fan, I did this after the season where we made the playoffs (╥﹏╥). 


The premise in the beginning was fairly simple: use the Python and a Reddit API library to scrape post-game threads for the 2024-25 season and then find a way to analyze sentiment for each comment. I researched some models that did sentiment analysis and ended up picking NLTK’s Vader model and Distilbert. These two models allowed me to compare a simpler rules-based model versus a transformer-based model. And working with Distilbert gave me exposure to the huggingface ecosystem. 


I decided to store the post data in MongoDB which was installed locally on my Windows PC. I did this because I had used SQLite to store the NBA salary data that I had scraped and now I wanted to learn about NoSQL. Looking back on it now I could have easily stored both the salary data and Reddit post data in CSVs or JSON but at least it was good to get exposed to those things. 


After finishing the analysis, I realized that the results weren’t very interesting to look at from a terminal or inside Jupyter notebooks. I wanted something that could be shown off like a website or a dashboard, so I decided on using Flask to build it. At this point I had no idea how a website worked, how things differed between a static page and a whole web application, or how others can get access to the website that I have on localhost. I didn’t even know that having data on MongoDB locally on my computer doesn’t actually make it available to the site in production. 


I ended up using MongoDB Atlas to host my data and I used Render to host the website. Doing those two things taught me a lot even if I didn’t fully understand everything at the time. I remember feeling very behind and wanted to do everything to sort of catch up in a way. It led to the canucks-sentiment project to be overcomplicated when it could have been more simple.


Fast-forward to January of 2026, I was able to get a data science co-op. I didn’t even know what I was getting myself into but one of the first things I learned was Docker. I learned to package up models I found or made into flask applications and into Docker containers. Having ML models in a flask application allowed other people or things to access the model which was a really good hands-on look at the distributed nature of things at larger companies. I also learned a little about AWS and that whole ecosystem and more specifically Sagemaker.


I wanted to apply this knowledge, more specifically packaging ML models in flask and cloud deployment. So I made an [NLP Inference API](https://github.com/ericcheung1/WPaaS) which I deployed on a Digital Ocean droplet. Doing this allowed me to understand how to configure a server manually and get my application code deployed there automatically though CI/CD pipelines. I also got to understand how networking and DNS work on a basic level which is why my projects are hosted on silly little domain names. 

After working on the NLP inference API I got into a phase where I wanted to make apps. Which led me to work on an [initial version](https://github.com/ericcheung1/askeric-nlp/blob/main/docs/README.md) of askeric-nlp which acted as a separate service that called my NLP inference API. It allowed me to practice a mini sort of distributed system. But it got cumbersome to have two things to maintain. I decided that I wanted one repo and one service which is how I ended up on the current setup.  
