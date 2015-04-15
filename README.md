# news-post

This post shows you how to combine the power of [Kimono](http://kimonolabs.com) and [Monkeylearn](http://monkeylearn.com) to scrape news sites and analyze articles in order to gain insights on the different news outlets as well as what's happening around us.

## What's included

This repository includes:
* `stritch.py` - a script that takes the raw data downloaded from Kimono and outputs a JSON with nicer data to work with.
* `*_raw.json` - the raw data from Kimono to give `stitch.py`, and what was used to write the post. The processed data is also included, so processing the raw data is not needed.
* `notebook/`
  * `*.json` - the data to analyze.
  * `News.ipyn` - an IPython notebook that will classify, process and graph the data.

## How to run the notebook

1. Clone this repository.
1. Navigate to the root directory of the repository.
2. Install the dependencies with `pip install -r requirements.txt`.
3. Navigate to the `notebook` directory.
4. Do `ipython notebook`.