# Projet Ingenuity 

## Introduction: Ingenuity dans le cadre de la mission Mars 2020. 

Mars 2020 est une mission spatiale qui consiste à déployer l'astromobile (rover) Perseverance sur le sol martien pour étudier sa surface et collecter des échnatillons du sol. Elle constitue la première d'une série de trois missions dont l'objectif final est de ramener ces échantillons sur Terre pour leur analyse. 

Ingenuity est un petit hélicoptère développé par l'agence spatiale Américaine, la NASA. Il est mis en oeuvre à titre expérimental sur le sol de la planète Mars au cours de la mission Mars 2020.
L'hélicoptère est embarqué à bord du rover Perseverance. 

Le 19 avril 2021, pour la première fois dans l'histoire de l'ère spatiale, un engin effectue un vol motorisé dans l'atmosphère ténue d'une autre planète. L'objectif d'Ingenuity est la reconnaissance optique du terrain, l'hélicoptère réalise de nombreuses photos aériennes utiliées par les pilotes de l'astromobile Perseverance pour identifier les obstacles et les sites prometteurs (prelèvement d'échantillons rocheux sur le sol martien). En effet, L'atmosphère très ténue (suelemnt 1% de la pression atmosphérique présente sur Terre) n'offre qu'une portance très faible et la mise au point d'un aérobot est par conséquent plus difficile. 

Ingenuity est un hélicoptère de 1,8 kg disposant de 2 rotors contrarotatifs coaxiaux. Il tire son énergie de 6 batteries lithium-ion rechargées par des cellules solaires. Son système de navigation lui permet de suivre sans intervention humaine un trajet pré-programmé. Sa seule charge utile est une caméra. 

La mission s'est récemment arrêtée (18 janvier 2024) en raison de la casse d'un pale lors du 72e vol. 

Ingenuity a ouvert de nouvelles perspectives pour l'exploration de Mars. La NASA et l'ESA, dans leur mission de retour d'échantillons martien, incluent maintenant 2 hélicopères similaires qui seront chargés de collecter les tubes contenant les échantillons martien déposés par l'astromobile Perseverance en cas de panne de celui-ci. 

La mission Mars Sample Return sera la première utilisation opérationnelle d'Ingenuity. Développée par la NASA en collaboration avec l'Agence spatiale européenne, elle a pour objectif de ramener sur Terre les échantillons de sol martien prélevés par l'astromobile Perseverance. Pour remplir cet objectif la mission prévoit d'envoyer un atterrisseur, Sample Retrieval Lander (SRL), emportant un bras téléopéré permettant de récupérer les tubes contenant les échantillons de sol. Si ces derniers se trouvent hors de portée de l'atterrisseur à la suite d'une panne de Perseverance, SRL dispose de deux hélicoptères Sample Recovery Helicopter, directement dérivés de l'hélicoptère Ingenuity, équipés d'une pince pour récupérer les tubes là où ils ont été déposés.

## Première approche de l'anatomie de l'hélicoptère Martien

Le site de la NASA donnant de nombreuses informations sur Ingenuity: (https://mars.nasa.gov/technology/helicopter/#)

<img width="1014" alt="Capture d’écran 2024-02-26 à 14 47 01" src="https://github.com/joel-colaso/2324_Projet1AB_-ingenuity-/assets/161329228/ec56dfa6-b859-430e-8665-364e45866630">

<img width="1210" alt="Capture d’écran 2024-02-26 à 14 47 34" src="https://github.com/joel-colaso/2324_Projet1AB_-ingenuity-/assets/161329228/0fe71f29-cba0-405e-a0ff-b863bfc618c3">

## Exploration du fonctionnement de l'hélicoptère

### Propulsion: 

L'hélicoptère se déplace dans les airs grâce à deux rotors contrarotatifs coaxiaux bipales. La vitesse de rotation est comprise entre 2400 et 2900 tours par minute, soit dix fois celle d'un rotor principal d'hélicoptère sur terre, pour pouvoir être efficace dans l'air peu dense de Mars. C'est une condition que nous ne pourrons pas remplir. 

La compréhension du mode de fontionnement des hélices d'un hélicoptère nous permet de soulever de premières difficultés: il faut des hélices de petites tailles qui sont coaxiales et contrarotatives, des pièces qu'il nous ai impossible de construire nous même (impression 3D). Une solution que nous avons pouvons mettre en place est l'utilisation d'hélices prélevées sur un hélicoptère télécommandé. On démontera l'appareil pour ne garder que les hélices sur l'axe et les moteurs, tout l'éléctronique sera reconstruit selon notre cahier des charges. 

Type d'aéronef: l'utilisation de rotors contrarotatifs coaxiaux permet de gagner en encombrement par rapport au recours à un rotor anticouple. 

### Énergie: 

L'énergie est le principal facteur limitant concernant les capacités de l'hélicoptère. L'énergie nécessaire pour la propulsion, le fonctionnement des capteurs (altimètre, caméra), les résistances chauffantes (chargées de maintenir les différents systèmes à une température compatible avec les contraintes de fonctionnement durant la nuit martienne), l'avionique, les processeurs et le système de télécommunication est fournie par six accumulateurs lithium-ion, d'une capacité de 36 Watts-h rechargés par des cellules photovoltaïques (surface active de 544 cm^2).

### Capteurs: 

- une caméra de navigation
- 2 centrales à inertie 3 axes (accélération et vitesse de rotation)
- inclinomètre 2 axes
- altimètre

### Télécommunication: 

Compte tenu du délais de communication Mars-Terre (une dizaine de minutes dans des conditions favorables), l'hélicoptère vol de manière autonome en appliquant des instructions transmises au préalable. En vol, l'hélicoptère ne reçoit pas mais émet pour communiquer les données collectées. 

### Avionique et processeurs:

L'avionique est répartie sur 5 circuits imprimés, dont 4 forment les côtés du fuselage cubique et le cinquième sa partie intèrieure. L'ordinateur embarqué utilise un microporcesseur Snapdragon cadencé à 2,26 Ghz et doté d'une mémoire vive de 2 Go et d'une mémoire flash de 32 Go. L'ordinateur prend en charge la fonction de navigation et pilote les rotors via deux microcontroleurs redondants. Le logiciel qui tourne sur le microporcesseur est assisité par un circuit intégré de type FPGA, qui prend en charge certaines fonctionnalités comme le contrôle d'altitiude, la gestion des entrées-sorties sur la centrale à inertie, de l'altimètre et de l'inclinomètre, et la gestion des télécommunications. Le FPGA est une version militarisée du ProASIC3L de MicroSemi. Le système d'exploitation est GNU/Linux. 



### Sources: 

https://mars.nasa.gov/technology/helicopter/#Tech-Specs

https://fr.wikipedia.org/wiki/Ingenuity_(hélicoptère)
