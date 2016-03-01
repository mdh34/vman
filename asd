BEGIN TRANSACTION;
CREATE TABLE vman_config (box_id text, name text, provider text, state int, directory text, project_dir text);
INSERT INTO `vman_config` VALUES ('3698b9a','default','virtualbox','poweroff','/home/glink/Projects/php','/home/glink/Projects/php/www');
COMMIT;
