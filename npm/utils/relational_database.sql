SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

DROP SCHEMA IF EXISTS `npm_dependencies` ;
CREATE SCHEMA IF NOT EXISTS `npm_dependencies` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `npm_dependencies` ;

-- -----------------------------------------------------
-- Table `npm_dependencies`.`Packages`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `npm_dependencies`.`Packages` ;

CREATE TABLE IF NOT EXISTS `npm_dependencies`.`Packages` (
  `package` CHAR(40) NOT NULL,
  `version` CHAR(30) NOT NULL,
  `package_index` INT(11) NOT NULL,
  `license` CHAR(60),
  CONSTRAINT `pk_packages` PRIMARY KEY (`package`,`version`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `npm_dependencies`.`Dependencies`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `npm_dependencies`.`Dependencies` ;

CREATE TABLE IF NOT EXISTS `npm_dependencies`.`Dependencies` (
  `package_package` CHAR(40) NOT NULL,
  `package_version` CHAR(30) NOT NULL,
  `package_depends_to_package` CHAR(40) NOT NULL,
  `package_dependency_version` CHAR(30) NOT NULL,
  CONSTRAINT `pk_dependencies` PRIMARY KEY (`package_package`,`package_version`,`package_depends_to_package`),
  CONSTRAINT `fk_dependencies_packages_package_version`
    FOREIGN KEY (`package_package`, `package_version`)
    REFERENCES `npm_dependencies`.`Packages` (`package`, `version`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_dependencies_packages_package_idx` ON `npm_dependencies`.`Dependencies` (`package_package` ASC);
CREATE INDEX `fk_dependencies_packages_version_idx` ON `npm_dependencies`.`Dependencies` (`package_version` ASC);