# Instagram User Data Fetcher

 This project uses the instaloader library to download metadata, profile picture, posts, and stories from an Instagram profile.

## Installation and Requirements
* Language: `python3` 
* To use this project, first install the instaloader library with the following command: 

`pip install instaloader`

## How to run this File
* Enter your Instagram username and password to the following variables:

`USER` = "your_username"

`PASSWORD` = "your_password"

* Finally, Run the following command to download the metadata, profile picture, posts, and stories from your Instagram profile:

`python instagram_user_data_fetcher.py`

## Author

* This project was created by `Akshay Parihar`

## Output

* The output of this project will be a directory called `output` . This directory will contain the following files:

* `metadata.json`: This file contains the metadata for the Instagram profile, including the username, full name, number of followers, number of followings, number of posts, etc.
* `profile_pic.jpg`: This file contains the profile picture for the Instagram profile.
* `posts`: This directory contains all of the posts from the Instagram profile. Each post is a separate file in JPG format.
* `stories`: This directory contains all of the stories from the Instagram profile. Each story is a separate file in MP4 format.


## License
* This project is licensed under the MIT License. See the LICENSE file for more information.


I hope this is helpful!
