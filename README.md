# Firefly III Import Configurations
This repository contains standardized import configurations for Firefly III. Various banks and financial institutions have already been added by contributing users. Thanks!

<!-- MarkdownTOC autolink="true" -->

- [Import configurations](#import-configurations)
	- [Firefly III](#firefly-iii)
	- [Great Britain](#great-britain)
	- [The Netherlands](#the-netherlands)
	- [Switserland](#switserland)
	- [US](#us)
	- [Austria](#austria)
- [Adding an import configuration](#adding-an-import-configuration)

<!-- /MarkdownTOC -->



## Import configurations
### Firefly III
* [v4.1.4](https://raw.githubusercontent.com/firefly-iii/import-configurations/master/firefly-iii/4.1.4.json)
* [v4.6.11](https://raw.githubusercontent.com/firefly-iii/import-configurations/master/firefly-iii/4.6.11.json)

### Great Britain
* [Revolut](https://github.com/firefly-iii/import-configurations/blob/master/gb/revolut/default.json)
* [Monzo](https://github.com/firefly-iii/import-configurations/blob/master/gb/monzo/default.json)

### The Netherlands
* [Rabobank (new CSV)](https://github.com/firefly-iii/import-configurations/blob/master/nl/rabobank/rabobank-new-csv-format.json)
* [ABN AMRO](https://github.com/firefly-iii/import-configurations/blob/master/nl/abnamro/default.json)
* [ING](https://raw.githubusercontent.com/firefly-iii/import-configurations/master/nl/ing/default.json)
* [bunq](https://github.com/firefly-iii/import-configurations/blob/master/nl/bunq/default.json)
* [SNS](https://github.com/firefly-iii/import-configurations/blob/master/nl/sns/default.json)

### Switserland
* [Credit Suisse](https://github.com/firefly-iii/import-configurations/blob/master/ch/creditsuisse/default.json)
* [Swisscard](https://github.com/firefly-iii/import-configurations/blob/master/ch/swisscard/default.json)

### US
* [Wells Fargo](https://github.com/firefly-iii/import-configurations/blob/master/us/wellsfargo/default.json)

### Austria
* [Easybank](https://github.com/firefly-iii/import-configurations/blob/master/at/easybank/default.json)

## Adding an import configuration

These instructions will help you add a configuration file to the project which others can use, by using the web pages directly on GitHub.com.  They don't include instructions for updating files locally from a sync'd repo on your machine.

* Find the correct country code abbreviation for the bank your configuration file relates to.  See this list of [country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements).
* Log into GitHub and fork the project using the icon at the top right of the screen.  More info can be found in [the GitHub help pages](https://help.github.com/articles/fork-a-repo/).
* From the forked repo select **Create New File**.
* To create folders type `<country code>/<bank name>/default.json` e.g `gb/monzo/default.json`.
* Then paste your .json file contents into the file window.
* Type a commit title and message so the owner knows what benefits the change gives.
* Select your account from the dropdown.
* Select __Create a new branch for this commit and start a pull request__.
