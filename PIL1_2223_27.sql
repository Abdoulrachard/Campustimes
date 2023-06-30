CREATE DATABASE PIL1222327;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) NOT NULL,
  `prenom` varchar(100) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `images_path` varchar(100) NOT NULL,
  `role_id` int,
  `created_at` datetime,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`role_id`)
  REFERENCES roles(`id`),
  UNIQUE KEY `email` (`email`)
) DEFAULT CHARSET=utf8mb4;

CREATE TABLE `role` (
  `id` int NOT NULL AUTO_INCREMENT,
  `label` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
)DEFAULT CHARSET=utf8mb4;

CREATE TABLE `classrooms`(
  `id` int NOT NULL AUTO_INCREMENT,
  `label` varchar(100) DEFAULT NULL,
  `capacity` int NOT NULL,
  `status` boolean,
  `description` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
)DEFAULT CHARSET=utf8mb4;

CREATE TABLE `subjects`(
  `id` int NOT NULL AUTO_INCREMENT,
  `label` varchar(100) DEFAULT NULL,
  `code` varchar(100),
  `total_time` int,
  `level_id` int,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`level_id`)
  REFERENCES levels(`id`)
)DEFAULT CHARSET=utf8mb4;

CREATE TABLE `levels` (
  `id` int NOT NULL AUTO_INCREMENT,
  `label` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
)DEFAULT CHARSET=utf8mb4;

CREATE TABLE `timetables` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int,
  `subject_id` int,
  `classroom_id` int,
  `level_id` int,
  `start_time` datetime,
  `end_time` datetime,
  `week` int,
  `created_at` datetime,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`)
  REFERENCES users(`id`),
  FOREIGN KEY (`subject_id`)
  REFERENCES subjects(`id`),
  FOREIGN KEY (`classroom_id`)
  REFERENCES classrooms(`id`),
  FOREIGN KEY (`level_id`)
  REFERENCES levels(`id`)
) DEFAULT CHARSET=utf8mb4;