# YouTube Video Downloader

This project is a Python script that allows you to download videos from YouTube.

## Getting Started

* Clone this repository to your computer.
* Install the pytube package by running the following command in your terminal:

```
pip install pytube
```

* Run the script by typing the following command in your terminal:

```
python youtube_video_downloader.py
```

## Usage

* The script will prompt you to enter the URL of the video you want to download. Once you have entered the URL, the script will download the video and save it to a file called `video.mp4`.

## Options

The script has a few options that you can use to customize the download process. These options can be passed to the script as command-line arguments.

* `-q`: Set the quality of the video to download. The default quality is `1080p`.
* `-o`: Set the output file name. The default output file name is `video.mp4`.

## Example

* To download a video in 720p and save it to a file called `my_video.mp4`, you would use the following command:


* python youtube_downloader.py -q 720p -o my_video.mp4


## Author

* This project was created by ```Akshay Parihar```

## License

* This project is licensed under the MIT License.
