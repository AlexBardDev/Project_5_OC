/*
Here is the code for the MySQL database.
After the connection to the MySQL database, do the following queries
*/

CREATE DATABASE pur_beurre_db;

CREATE USER script@localhost IDENTIFIED BY "SUPERmotdepasse3000";

GRANT ALL ON pur_beurre_db.* TO script IDENTIFIED BY "SUPERmotdepasse3000";

/*
I use the ORM called 'peewee' to create the tables and the constraints.
I recommend to use 'peewee' because with this tool, the code is more
portable. You can easily change the database if the project becomes
too big. But, if you really want to use the MySQL queries, here there are:

CREATE TABLE `category` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB 


LOCK TABLES `category` WRITE;
INSERT INTO `category` VALUES (1,'boissons-sucrees'),(2,'produits-a-tartiner-sucres'),(3,'snacks-sales'),(4,'snacks-sucres'),(5,'viennoiseries'),(6,'plats-prepares-surgeles'),(7,'biscuits-et-gateaux'),(8,'cereales-pour-petit-dejeuner'),(9,'pates-alimentaires'),(10,'pizzas');
UNLOCK TABLES;

CREATE TABLE `foodsubstituted` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_name` varchar(50) NOT NULL,
  `substituted_product_name` varchar(50) NOT NULL,
  `description` text NOT NULL,
  `stores` varchar(50) NOT NULL,
  `link` varchar(200) NOT NULL,
  `id_category_id` int(11) NOT NULL,
  `is_saved` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `foodsubstituted_id_category_id` (`id_category_id`),
  CONSTRAINT `foodsubstituted_ibfk_1` FOREIGN KEY (`id_category_id`) REFERENCES `category` (`id`)
) ENGINE=InnoDB

LOCK TABLES `foodsubstituted` WRITE;
INSERT INTO `foodsubstituted` VALUES (1,'Coca Cola','Sprite (pack professionnel)','','','https://fr.openfoodfacts.org/produit/5000112559071',1,0),(2,'Ice Tea','Soya red fruit','','','https://fr.openfoodfacts.org/produit/5411188122098',1,0),(3,'Pomegranate Green Tea','Le jus bio légumes salé','','','https://fr.openfoodfacts.org/produit/3505040246069',1,0),(4,'Nutella','Confiture de cerises noires','','','https://fr.openfoodfacts.org/produit/3760101594835',2,0),(5,'Confiture Pêches','Confiture fraises extra','','','https://fr.openfoodfacts.org/produit/3301595000176',2,0),(6,'3D\'s Bugles goût paprika','Snack Soja saveur Barbecue','Snack Poppé à base de Soja et Pomme de Terre saveur Barbecue','Auchan','https://fr.openfoodfacts.org/produit/3245550078674',3,0),(7,'Apéro Cracks Fins & Fondants Mix Salé + Emmental','Goût Nacho Cheese','Tortilla chips de maïs goût nacho cheese','Auchan','https://fr.openfoodfacts.org/produit/3168930008170',3,0),(8,'Bretzels Ancel','Tuiles goût paprika','Tuiles à base de pomme de terre goût paprika','Cora','https://fr.openfoodfacts.org/produit/3257983217124',3,0),(9,'Lindor Noir 60%','Noir sans sucre','','','https://fr.openfoodfacts.org/produit/3760008560391',4,0),(10,'Petit écolier chocolat fin','Arlequin Tendre','','','https://fr.openfoodfacts.org/produit/3116740030881',4,0),(11,'Biscuit choco noir intense','Banania Arôme Intense','Préparation en poudre pour boisson cacaotée','Intermarché','https://fr.openfoodfacts.org/produit/3700278404414',4,0),(12,'10 pains au lait au levain','Brioche Tranchée Gourmande','','','https://fr.openfoodfacts.org/produit/3228857000142',5,0),(13,'Panettone Chocolat','Gâche tranchée','Brioche au beurre frais et à la crème fraîche','','https://fr.openfoodfacts.org/produit/3587220002252',5,0),(14,'Gâche Vendéenne Pur Beurre à la crème fraîche','8 Pains au lait Bio','Pain au lait issu de l\'agriculture biologique','Leclerc','https://fr.openfoodfacts.org/produit/3284230011884',5,0),(15,'Crousty Cheese','Poêlée maraîchère','','','https://fr.openfoodfacts.org/produit/3184032846342',6,0),(16,'Paniers. Gourmands Jambon Fromage','Ratatouille cuisinée','Ratatouille cuisinée','Picard','https://fr.openfoodfacts.org/produit/3270160114382',6,0),(17,'8 Paniers Poulet Champignons','Poêlée rustique la Rustique','Mélange de pommes de terre, champignons et légumes cuisiné surgelé','Carrefour, Franprix','https://fr.openfoodfacts.org/produit/3083681022650',6,0),(18,'Choco suprême','Tarte Framboise 6 Parts','','','https://fr.openfoodfacts.org/produit/3567747040449',7,0),(19,'Mikado Chocolat au lait','24 Macarons','','','https://fr.openfoodfacts.org/produit/3187670616339',7,0),(20,'Golden Oreo','Mon flan entremets parfum vanille','Préparation pour Mon flan entremets parfum vanille','Intermarché','https://fr.openfoodfacts.org/produit/3027030028665',7,0),(21,'Muesli Croustillant aux 2 Chocolats','Cereales Lion','','','https://fr.openfoodfacts.org/produit/7613033481314',8,0),(22,'Extra','Flocons d\'avoine Complets','Flocons d\'avoine complète','Carrefour','https://fr.openfoodfacts.org/produit/3421557910203',8,0),(23,'Ravioles du Dauphiné','Penne Rigate D\'alsace Aux Oeufs','','','https://fr.openfoodfacts.org/produit/3256221112139',9,0),(24,'Girasoli Gorgonzola Crémeux','Coudes rayés','','','https://fr.openfoodfacts.org/produit/3256221111958',9,0),(25,'Demi-Lune, Cèpes-Parmesan','Tortellini Emiliani Proschiutto e Formaggio','Pâtes de semoule de blé dur aux œufs, farcies avec viandes de porc, jambon et fromage','Franprix','https://fr.openfoodfacts.org/produit/8076808890015',9,0),(26,'Fiesta 3 Formaggi','Pizza La Géante Royale','Pizza à la mozarella, jambon cuit supérieur, édam. champignons de Paris et olives - Surgelée.','Carrefour','https://fr.openfoodfacts.org/produit/3560070822492',10,0),(27,'La Pizz Chorizo','Pizza aux cinq légumes','','','https://fr.openfoodfacts.org/produit/3564707119856',10,0),(28,'Pizza Sodebo Capri','Pizza Fruits de Mer','Pizza cuite sur pierre garnie de fruits de mer, surgelée.','Auchan','https://fr.openfoodfacts.org/produit/3596710441969',10,0);
UNLOCK TABLES;

*/
