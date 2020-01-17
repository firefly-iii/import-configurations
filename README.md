# Firefly III Import Configurations
This repository contains standardized import configurations for Firefly III. Various banks and financial institutions have already been added by contributing users. Thanks!

## Adding an import configuration

These instructions will help you add a configuration file to the project which others can use, by using the web pages directly on GitHub.com. They don't include instructions for updating files locally from a sync'd repo on your machine.

* Find the correct country code abbreviation for the bank your configuration file relates to.  See this list of [country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements).
* Log into GitHub and fork the project using the icon at the top right of the screen.  More info can be found in [the GitHub help pages](https://help.github.com/articles/fork-a-repo/).
* From the forked repo select **Create New File**.
* To create folders type `<country code>/<bank name>/default.json` e.g `gb/monzo/default.json`.
* Then paste your .json file contents into the file window.
* Type a commit title and message so the owner knows what benefits the change gives.
* Select your account from the dropdown.
* Select __Create a new branch for this commit and start a pull request__.

