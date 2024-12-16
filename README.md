# DOSSIER-MEDICAL-AVEC-BLOCKCHAIN
Système de Gestion des Dossiers Médicaux sur la Blockchain
### Description du Projet
Ce projet est une application décentralisée (DApp) permettant la gestion sécurisée des dossiers médicaux sur une blockchain Ethereum. Il garantit la transparence, la sécurité et la confidentialité des informations grâce à l'utilisation des smart contracts et du stockage décentralisé via IPFS. Les patients peuvent stocker, gérer et contrôler l'accès à leurs dossiers médicaux, tandis que les médecins accèdent uniquement aux dossiers autorisés.

### Fonctionnalités Principales
Authentification des Utilisateurs

Enregistrement et connexion pour les patients et les médecins.
Gestion des rôles (Patient/Docteur) via les smart contracts.
Stockage Sécurisé des Dossiers Médicaux

Chiffrement des dossiers médicaux avec l'algorithme AES.
Téléversement des fichiers chiffrés sur IPFS.
Enregistrement des hachages IPFS sur la blockchain.
Contrôle des Permissions

Les patients peuvent accorder ou révoquer l'accès à leurs dossiers médicaux pour les médecins.
Gestion des autorisations via smart contracts.
Audit et Traçabilité

Enregistrement des actions (ajout de fichiers, permissions) dans un contrat d'audit.
Affichage des logs d'audit pour assurer la traçabilité des opérations.
Interface Utilisateur Conviviale

Application graphique développée avec Tkinter pour faciliter l'interaction des utilisateurs.
Différents onglets pour l'authentification, la gestion des patients, l'accès aux informations et les logs d'audit.
Architecture du Système

### L'architecture repose sur les éléments suivants :

Ethereum Blockchain : Enregistrement des hachages des fichiers et gestion des transactions.
Smart Contracts : Contrats Solidity pour gérer les permissions, les utilisateurs et les logs d'audit.
IPFS : Stockage décentralisé pour les fichiers médicaux chiffrés.
Python (Tkinter & Web3.py) : Interface graphique et interaction avec la blockchain.
AES Encryption : Sécurisation des fichiers médicaux avant téléversement sur IPFS.
Ganache : Simulation locale de la blockchain Ethereum pour le développement et les tests.
Pinata : Service pour gérer les fichiers sur IPFS.
