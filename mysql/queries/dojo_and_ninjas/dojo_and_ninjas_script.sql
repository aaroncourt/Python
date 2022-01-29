-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Dojos_And_Ninjas
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `Dojos_And_Ninjas` ;

-- -----------------------------------------------------
-- Schema Dojos_And_Ninjas
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Dojos_And_Ninjas` DEFAULT CHARACTER SET utf8 ;
USE `Dojos_And_Ninjas` ;

-- -----------------------------------------------------
-- Table `Dojos_And_Ninjas`.`Dojos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dojos_And_Ninjas`.`Dojos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Dojos_And_Ninjas`.`Ninjas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Dojos_And_Ninjas`.`Ninjas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `age` INT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `Dojo_id` INT NOT NULL,
  PRIMARY KEY (`id`, `Dojo_id`),
  INDEX `fk_Ninjas_Dojos_idx` (`Dojo_id` ASC) VISIBLE,
  CONSTRAINT `fk_Ninjas_Dojos`
    FOREIGN KEY (`Dojo_id`)
    REFERENCES `Dojos_And_Ninjas`.`Dojos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
