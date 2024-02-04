# Configuration d'Importation RBC pour Firefly III Data Importer

Ce fichier de configuration JSON est conçu pour être utilisé avec l'outil d'importation de données Firefly III, permettant l'importation automatique des transactions financières depuis les relevés de compte de la Royal Bank of Canada (RBC) vers Firefly III.

## Structure du Fichier de Configuration

- **Version et Source :** Ce fichier est basé sur la version 3 du format de fichier de configuration et est conçu pour fonctionner avec la version `ff3-importer-1.4.1` de l'importateur de données Firefly III.
- **Format de Date :** La date des transactions est attendue au format `n/j/Y` (mois/jour/année).
- **Délimiteur :** Les colonnes dans le fichier CSV sont séparées par des virgules.
- **Entêtes et Règles :** Le fichier d'importation contient des en-têtes, et les règles d'importation sont activées.

## Format du Fichier CSV

Votre fichier CSV provenant de RBC doit contenir les colonnes suivantes :

1. _Type de compte (ce champ est ignoré dans cette configuration)_
2. Numéro du compte
3. Date de l'opération
4. Numéro du chèque
5. Description 1
6. Description 2
7. CAD (montant de la transaction en dollars canadiens)
8. _USD (ce champ est ignoré dans cette configuration)_

## Détection des Doublons

La méthode de détection des doublons `classique` est utilisée pour éviter l'importation de transactions en double.

## Conversion de Devise

La conversion de devise est activée, permettant la conversion automatique des montants des transactions en devise principale de votre compte Firefly III si nécessaire.