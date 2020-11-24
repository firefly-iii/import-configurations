# Firefly III CSV importer configuration files
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-7-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

This repository contains standardized import configurations for the [Firefly III CSV importer](https://github.com/firefly-iii/csv-importer).

Various banks and financial institutions have already been added by contributing users. Thank you!

## Finding an import configuration for your bank.

Browse the files above, which are grouped by country and then by bank.

In the folder `other-software` you will find import configurations for other financial tools. In `firefly-iii`, you will find import configurations for Firefly III itself.

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://sakowi.cz"><img src="https://avatars0.githubusercontent.com/u/13169301?v=4" width="100px;" alt=""/><br /><sub><b>Szymon Sakowicz</b></sub></a><br /><a href="#content-sakowicz" title="Content">🖋</a></td>
    <td align="center"><a href="https://github.com/muracz"><img src="https://avatars1.githubusercontent.com/u/9215725?v=4" width="100px;" alt=""/><br /><sub><b>Marcin Uracz</b></sub></a><br /><a href="#content-muracz" title="Content">🖋</a></td>
    <td align="center"><a href="https://github.com/sebastianklein96"><img src="https://avatars2.githubusercontent.com/u/22731416?v=4" width="100px;" alt=""/><br /><sub><b>Sebastian Klein</b></sub></a><br /><a href="#content-sebastianklein96" title="Content">🖋</a></td>
    <td align="center"><a href="https://github.com/muracz"><img src="https://avatars1.githubusercontent.com/u/9215725?v=4" width="100px;" alt=""/><br /><sub><b>Marcin Uracz</b></sub></a><br /><a href="#content-muracz" title="Content">🖋</a></td>
    <td align="center"><a href="https://github.com/ilakast"><img src="https://avatars3.githubusercontent.com/u/1414477?v=4" width="100px;" alt=""/><br /><sub><b>ilakast</b></sub></a><br /><a href="https://github.com/firefly-iii/import-configurations/commits?author=ilakast" title="Documentation">📖</a> <a href="#content-ilakast" title="Content">🖋</a></td>
    <td align="center"><a href="https://github.com/baocin"><img src="https://avatars0.githubusercontent.com/u/5463986?v=4" width="100px;" alt=""/><br /><sub><b>Michael Pedersen</b></sub></a><br /><a href="#plugin-baocin" title="Plugin/utility libraries">🔌</a></td>
    <td align="center"><a href="https://federicociro.com"><img src="https://avatars2.githubusercontent.com/u/25438748?v=4" width="100px;" alt=""/><br /><sub><b>Federico</b></sub></a><br /><a href="https://github.com/firefly-iii/import-configurations/issues?q=author%3Afedericociro" title="Bug reports">🐛</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

## Adding an import configuration

First of all, thanks for adding your configuration! 🎉

These instructions will help you add a configuration file to the project which others can use. You can do this on GitHub itself, without having to use command line tools or weird commands.

1. Find the correct country code for the bank your configuration file relates to. Check out [this list of country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements).
2. Log into GitHub and fork the project using the icon at the top right of the screen.  More info can be found in [the GitHub help pages](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo).
3. From the forked repo select **Create New File**.
4. To create folders type `<country code>/<bank name>/default.json` e.g `gb/monzo/default.json`.
5. Paste your `.json` file contents into the file window.

⚠️ Before you continue, make sure that the JSON file contains no private data, like account names.

Then, finish the commit:

1. Type a commit title and message so the owner knows what benefits the change gives.
2. Select your account from the dropdown.
3. Select __Create a new branch for this commit and start a pull request__.
