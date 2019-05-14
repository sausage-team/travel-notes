CREATE TABLE `travel_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `content` longtext NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `status` int(11) NOT NULL,
  `author` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `travel_article_user_id_188d6f31_fk_travel_user_id` (`user_id`),
  CONSTRAINT `travel_article_user_id_188d6f31_fk_travel_user_id` FOREIGN KEY (`user_id`) REFERENCES `travel_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

CREATE TABLE `travel_articlecover` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cover` longtext NOT NULL,
  `article_id` int(11) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;

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