# Firefly III Import Configurations
This repository contains standardized import configurations for Firefly III. Various banks and financial institutions have already been added by contributing users. Thanks!

<!-- MarkdownTOC -->

- Import configurations
	- Firefly III
	- The Netherlands
	- Switserland
	- UK
	- US
- Adding an import configuration

<!-- /MarkdownTOC -->



## Import configurations
### Firefly III
* [v4.1.4](https://raw.githubusercontent.com/firefly-iii/import-configurations/master/firefly-iii/4.1.4.json)
* [v4.6.11](https://raw.githubusercontent.com/firefly-iii/import-configurations/master/firefly-iii/4.6.11.json)

### The Netherlands
* [Rabobank (new CSV)](https://github.com/firefly-iii/import-configurations/blob/master/nl/rabobank/rabobank-new-csv-format.json)
* [ABN AMRO](https://github.com/firefly-iii/import-configurations/blob/master/nl/abnamro/default.json)
* [ING](https://raw.githubusercontent.com/firefly-iii/import-configurations/master/nl/ing/default.json)
* [bunq](https://github.com/firefly-iii/import-configurations/blob/master/nl/bunq/default.json)
* [SNS](https://github.com/firefly-iii/import-configurations/blob/master/nl/sns/default.json)

### Switserland
* [Credit Suisse](https://github.com/firefly-iii/import-configurations/blob/master/ch/creditsuisse/default.json)
* [Swisscard](https://github.com/firefly-iii/import-configurations/blob/master/ch/swisscard/default.json)

### UK
* [Revolut](https://github.com/firefly-iii/import-configurations/blob/master/uk/revolut/default.json)

### US
* [Wells Fargo](https://github.com/firefly-iii/import-configurations/blob/master/us/wellsfargo/default.json)

## Adding an import configuration

These instructions will help you add a configuration file to the project which others can use, by using the web pages directly on GitHub.com.  They don't include instructions for updating files locally from a sync'd repo on your machine.

* Find the correct country code abbreviation for the bank your configuration file relates to.  See [country codes]: https://www.worldatlas.com/aatlas/ctycodes.htm A2 column
* Log into GitHub and fork the project using the icon at the top right of the screen.  More info can be found here: https://help.github.com/articles/fork-a-repo/
* From the forked repo select "__Create new File__"
* To create folders type "country code"/"bank name"/"default.json" e.g gb/monzo/default.json
* Then paste your .json file contents into the file window
* Type a commit title and message so the owner knows what benefits the change gives. i.e. new bank import config
* Select your account from the dropdown
* Select __Create a new branch for this commit and start a pull request__
