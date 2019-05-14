CREATE TABLE `travel_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `id_card` varchar(18) NOT NULL,
  `uid` varchar(40) NOT NULL,
  `role` int(11) NOT NULL,
  `icon` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;