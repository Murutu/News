# NewsNow

An application that will allow users to read news articles from various sources.

### Author
Peter Murutu


### Description
NewsNow is a web application that displays a list of various news sources like Lifehacker, NewYorkTimes, TechCrunch and many more. On choosing a news source, it will preview the top news articles of the day. Clicking a news article will redirect the user to read it fully from the news source. It achieves this by using the News API.

### User Stories
These are the behaviours/features that the application implements for use by a user.
As user can be able to:
  - Select the ones they prefer
  - See the top news articles from that news source
  - See the image, description and time the news article was created
  - Click on an article and read it fully from the news source
 
### Installation Requirements

```sh
$ Prerequisites
$ python3.6
$ pip
$ virtualenv
```


### Running the Application

- Creating the virtual environment:
```sh
$ python3.6 -m venv --without-pip virtual
$ source virtual/bin/env
$  curl https://bootstrap.pypa.io/get-pip.py | python 
```
  
### Installing Flask and other Modules

```sh
$ python3.6 -m pip install Flask
$ python3.6 -m pip install Flask-Bootstrap
$ python3.6 -m pip install arrow
$ python3.6 -m pip install requests
```

### Setting up the API Key
To be able to gather article info from the News API you will need an API Key.
Visit [Newsapi](https://newsapi.org/) v4+ to run.
- Insert the API Key you received from News Api where <Your-Api-Key> is.
- To run the application, in your terminal: $ python3.6 run.py .

### Technologies Used

```sh
$ Python3.6
$ Flask
```





### The link

https://news-peter.herokuapp.com/


### License

MIT ©2020 Peter Murutu
