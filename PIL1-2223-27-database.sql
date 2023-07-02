CREATE TABLE `users` (
  `id` int PRIMARY KEY,
  `lastname` varchar(255),
  `firstname` varchar(255),
  `email` varchar(255),
  `phone` varchar(255),
  `password` varchar(255),
  `role_id` int,
  `created_at` datetime
);

CREATE TABLE `levels` (
  `id` int PRIMARY KEY,
  `label` varchar(255)
);

CREATE TABLE `roles` (
  `id` int PRIMARY KEY,
  `label` varchar(255)
);

CREATE TABLE `subjects` (
  `id` int PRIMARY KEY,
  `label` varchar(255),
  `code` varchar(255),
  `total_time` int,
  `level_id` int
);

CREATE TABLE `classrooms` (
  `id` int PRIMARY KEY,
  `label` varchar(255)
);

CREATE TABLE `timetables` (
  `id` int PRIMARY KEY,
  `user_id` int,
  `subject_id` int,
  `classroom_id` int,
  `level_id` int,
  `start_time` datetime,
  `end_time` datetime,
  `week` int,
  `created_at` datetime
);

ALTER TABLE `users` ADD FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`);

ALTER TABLE `subjects` ADD FOREIGN KEY (`level_id`) REFERENCES `levels` (`id`);

CREATE TABLE `timetables_users` (
  `timetables_user_id` int,
  `users_id` int,
  PRIMARY KEY (`timetables_user_id`, `users_id`)
);

ALTER TABLE `timetables_users` ADD FOREIGN KEY (`timetables_user_id`) REFERENCES `timetables` (`user_id`);

ALTER TABLE `timetables_users` ADD FOREIGN KEY (`users_id`) REFERENCES `users` (`id`);


ALTER TABLE `timetables` ADD FOREIGN KEY (`subject_id`) REFERENCES `subjects` (`id`);

ALTER TABLE `timetables` ADD FOREIGN KEY (`level_id`) REFERENCES `levels` (`id`);

ALTER TABLE `timetables` ADD FOREIGN KEY (`classroom_id`) REFERENCES `classrooms` (`id`);
