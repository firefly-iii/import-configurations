# Firefly III Data Importer configuration files
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-40-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

This repository contains standardized import configurations for the [Firefly III Data Importer](https://github.com/firefly-iii/data-importer).

Various banks and financial institutions have already been added by contributing users. Thank you!

## Finding an import configuration for your bank.

Browse the files above, which are grouped by country and then by bank.

In the folder `other-software` you will find import configurations for other financial tools. In `firefly-iii`, you will find import configurations for Firefly III itself.

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

### Support the development of Firefly III

If you like Firefly III and if it helps you save lots of money, why not send me a dime for every dollar saved! :tada:

OK that was a joke. If you feel Firefly III made your life better, consider contributing as a sponsor. Please check out my [Patreon](https://www.patreon.com/jc5) and [GitHub Sponsors](https://github.com/sponsors/JC5) page for more information. Thank you for considering donating to Firefly III!

## Contact

You can contact me at [james@firefly-iii.org](mailto:james@firefly-iii.org), you may open an issue or contact me through the support channels:

- [GitHub Discussions for questions and support](https://github.com/firefly-iii/firefly-iii/discussions/)
- [Gitter.im for a good chat and a quick answer](https://gitter.im/firefly-iii/firefly-iii)
- [GitHub Issues for bugs and issues](https://github.com/firefly-iii/firefly-iii/issues)
- [Follow me around for news and updates on Twitter](https://twitter.com/Firefly_iii)

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://sakowi.cz"><img src="https://avatars0.githubusercontent.com/u/13169301?v=4?s=100" width="100px;" alt="Szymon Sakowicz"/><br /><sub><b>Szymon Sakowicz</b></sub></a><br /><a href="#content-sakowicz" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/muracz"><img src="https://avatars1.githubusercontent.com/u/9215725?v=4?s=100" width="100px;" alt="Marcin Uracz"/><br /><sub><b>Marcin Uracz</b></sub></a><br /><a href="#content-muracz" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/sebastianklein96"><img src="https://avatars2.githubusercontent.com/u/22731416?v=4?s=100" width="100px;" alt="Sebastian Klein"/><br /><sub><b>Sebastian Klein</b></sub></a><br /><a href="#content-sebastianklein96" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/muracz"><img src="https://avatars1.githubusercontent.com/u/9215725?v=4?s=100" width="100px;" alt="Marcin Uracz"/><br /><sub><b>Marcin Uracz</b></sub></a><br /><a href="#content-muracz" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ilakast"><img src="https://avatars3.githubusercontent.com/u/1414477?v=4?s=100" width="100px;" alt="ilakast"/><br /><sub><b>ilakast</b></sub></a><br /><a href="https://github.com/firefly-iii/import-configurations/commits?author=ilakast" title="Documentation">📖</a> <a href="#content-ilakast" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/baocin"><img src="https://avatars0.githubusercontent.com/u/5463986?v=4?s=100" width="100px;" alt="Michael Pedersen"/><br /><sub><b>Michael Pedersen</b></sub></a><br /><a href="#plugin-baocin" title="Plugin/utility libraries">🔌</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://federicociro.com"><img src="https://avatars2.githubusercontent.com/u/25438748?v=4?s=100" width="100px;" alt="Federico"/><br /><sub><b>Federico</b></sub></a><br /><a href="https://github.com/firefly-iii/import-configurations/issues?q=author%3Afedericociro" title="Bug reports">🐛</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/3isenHeiM"><img src="https://avatars0.githubusercontent.com/u/26417172?v=4?s=100" width="100px;" alt="3isenHeiM"/><br /><sub><b>3isenHeiM</b></sub></a><br /><a href="#content-3isenHeiM" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/SamBouwer"><img src="https://avatars3.githubusercontent.com/u/6918900?v=4?s=100" width="100px;" alt="SamBouwer"/><br /><sub><b>SamBouwer</b></sub></a><br /><a href="#content-SamBouwer" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Akuma737"><img src="https://avatars2.githubusercontent.com/u/1916021?v=4?s=100" width="100px;" alt="Akuma737"/><br /><sub><b>Akuma737</b></sub></a><br /><a href="#content-Akuma737" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://paul.biester.pro"><img src="https://avatars0.githubusercontent.com/u/2650326?v=4?s=100" width="100px;" alt="Paul Biester"/><br /><sub><b>Paul Biester</b></sub></a><br /><a href="#content-isonet" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.linkedin.com/in/thiagogpa/"><img src="https://avatars.githubusercontent.com/u/39960304?v=4?s=100" width="100px;" alt="Thiago Andrade"/><br /><sub><b>Thiago Andrade</b></sub></a><br /><a href="#content-thiagogpa" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://rolisz.ro"><img src="https://avatars.githubusercontent.com/u/426313?v=4?s=100" width="100px;" alt="Roland Szabo"/><br /><sub><b>Roland Szabo</b></sub></a><br /><a href="#content-rolisz" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://kenric.in/"><img src="https://avatars.githubusercontent.com/u/5753813?v=4?s=100" width="100px;" alt="Kenric D'Souza"/><br /><sub><b>Kenric D'Souza</b></sub></a><br /><a href="#content-AzureByte" title="Content">🖋</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://baletskyi.me"><img src="https://avatars.githubusercontent.com/u/11590484?v=4?s=100" width="100px;" alt="Alex Baletskyi"/><br /><sub><b>Alex Baletskyi</b></sub></a><br /><a href="#content-baletskyi" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/EliRibble"><img src="https://avatars.githubusercontent.com/u/2319207?v=4?s=100" width="100px;" alt="Eli Ribble"/><br /><sub><b>Eli Ribble</b></sub></a><br /><a href="#content-EliRibble" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/MadWalnut"><img src="https://avatars.githubusercontent.com/u/33835479?v=4?s=100" width="100px;" alt="MadWalnut"/><br /><sub><b>MadWalnut</b></sub></a><br /><a href="#content-MadWalnut" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/weissi1994"><img src="https://avatars.githubusercontent.com/u/846897?v=4?s=100" width="100px;" alt="Daniel Weissengruber"/><br /><sub><b>Daniel Weissengruber</b></sub></a><br /><a href="#content-weissi1994" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/niallperks"><img src="https://avatars.githubusercontent.com/u/35839988?v=4?s=100" width="100px;" alt="niallperks"/><br /><sub><b>niallperks</b></sub></a><br /><a href="#content-niallperks" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://leonjza.github.io/"><img src="https://avatars.githubusercontent.com/u/1148127?v=4?s=100" width="100px;" alt="Leon Jacobs"/><br /><sub><b>Leon Jacobs</b></sub></a><br /><a href="#content-leonjza" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Dave4234"><img src="https://avatars.githubusercontent.com/u/86469014?v=4?s=100" width="100px;" alt="Dave4234"/><br /><sub><b>Dave4234</b></sub></a><br /><a href="#content-Dave4234" title="Content">🖋</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/marcquark"><img src="https://avatars.githubusercontent.com/u/23556080?v=4?s=100" width="100px;" alt="Marc Leuser"/><br /><sub><b>Marc Leuser</b></sub></a><br /><a href="#content-marcquark" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/arbezerra"><img src="https://avatars.githubusercontent.com/u/5190728?v=4?s=100" width="100px;" alt="André Ricardo"/><br /><sub><b>André Ricardo</b></sub></a><br /><a href="#content-arbezerra" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/le-jou"><img src="https://avatars.githubusercontent.com/u/28442160?v=4?s=100" width="100px;" alt="Lennard Jouvenal"/><br /><sub><b>Lennard Jouvenal</b></sub></a><br /><a href="#content-le-jou" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/leizhang"><img src="https://avatars.githubusercontent.com/u/140418?v=4?s=100" width="100px;" alt="Lei Zhang"/><br /><sub><b>Lei Zhang</b></sub></a><br /><a href="#content-leizhang" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/zannis"><img src="https://avatars.githubusercontent.com/u/1011451?v=4?s=100" width="100px;" alt="Zannis Kalampoukis"/><br /><sub><b>Zannis Kalampoukis</b></sub></a><br /><a href="#content-zannis" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/mblankenstein"><img src="https://avatars.githubusercontent.com/u/802221?v=4?s=100" width="100px;" alt="Michel Blankenstein"/><br /><sub><b>Michel Blankenstein</b></sub></a><br /><a href="#content-mblankenstein" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/terencejackson8000"><img src="https://avatars.githubusercontent.com/u/14046007?v=4?s=100" width="100px;" alt="terencejackson8000"/><br /><sub><b>terencejackson8000</b></sub></a><br /><a href="#content-terencejackson8000" title="Content">🖋</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="http://yassfuentes.es"><img src="https://avatars.githubusercontent.com/u/60194650?v=4?s=100" width="100px;" alt="Yass Fuentes"/><br /><sub><b>Yass Fuentes</b></sub></a><br /><a href="#content-backmind" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/fergalc"><img src="https://avatars.githubusercontent.com/u/3813285?v=4?s=100" width="100px;" alt="fergalc"/><br /><sub><b>fergalc</b></sub></a><br /><a href="#content-fergalc" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://z3ntu.xyz"><img src="https://avatars.githubusercontent.com/u/3768500?v=4?s=100" width="100px;" alt="Luca Weiss"/><br /><sub><b>Luca Weiss</b></sub></a><br /><a href="#content-z3ntu" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/C9Glax"><img src="https://avatars.githubusercontent.com/u/13404778?v=4?s=100" width="100px;" alt="Glax"/><br /><sub><b>Glax</b></sub></a><br /><a href="#content-C9Glax" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://saxobroko.com"><img src="https://avatars.githubusercontent.com/u/18757374?v=4?s=100" width="100px;" alt="Saxo_Broko"/><br /><sub><b>Saxo_Broko</b></sub></a><br /><a href="#content-saxobroko" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Svedrin"><img src="https://avatars.githubusercontent.com/u/946488?v=4?s=100" width="100px;" alt="Michael Ziegler"/><br /><sub><b>Michael Ziegler</b></sub></a><br /><a href="#content-Svedrin" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Korri"><img src="https://avatars.githubusercontent.com/u/130747?v=4?s=100" width="100px;" alt="Hugo Vacher"/><br /><sub><b>Hugo Vacher</b></sub></a><br /><a href="#content-korri" title="Content">🖋</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/aasiddiq"><img src="https://avatars.githubusercontent.com/u/9424117?v=4?s=100" width="100px;" alt="Aadil Siddiqui"/><br /><sub><b>Aadil Siddiqui</b></sub></a><br /><a href="#content-aasiddiq" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tabias"><img src="https://avatars.githubusercontent.com/u/6348309?v=4?s=100" width="100px;" alt="tabias"/><br /><sub><b>tabias</b></sub></a><br /><a href="#content-tabias" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://daviddaily.dev"><img src="https://avatars.githubusercontent.com/u/18452976?v=4?s=100" width="100px;" alt="Daily the Noob"/><br /><sub><b>Daily the Noob</b></sub></a><br /><a href="#content-DailytheNoob" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/OscarTienda"><img src="https://avatars.githubusercontent.com/u/89542749?v=4?s=100" width="100px;" alt="Óscar Tienda Beteta"/><br /><sub><b>Óscar Tienda Beteta</b></sub></a><br /><a href="#content-OscarTienda" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Danjaraka"><img src="https://avatars.githubusercontent.com/u/38589122?v=4?s=100" width="100px;" alt="Daniel"/><br /><sub><b>Daniel</b></sub></a><br /><a href="#data-Danjaraka" title="Data">🔣</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
