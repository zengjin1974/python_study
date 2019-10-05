DROP TABLE `beer_temperature`;

CREATE TABLE `beer_temperature` (
  `seq` int(11) NOT NULL,
  `temperature` decimal(4,2) DEFAULT NULL,
  `beer_sale` decimal(4,2) DEFAULT NULL,
  PRIMARY KEY (`seq`)
) ;

INSERT INTO `beer_temperature` (`seq`,`temperature`,`beer_sale`) VALUES (1,5.50,2.38);
INSERT INTO `beer_temperature` (`seq`,`temperature`,`beer_sale`) VALUES (2,6.60,3.85);
INSERT INTO `beer_temperature` (`seq`,`temperature`,`beer_sale`) VALUES (3,8.10,4.41);
