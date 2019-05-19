/*
Navicat MySQL Data Transfer

Source Server         : root
Source Server Version : 50722
Source Host           : localhost
Source Database       : test_project

Target Server Type    : MYSQL
Target Server Version : 50722
File Encoding         : 65001

Date: 2019-05-14 20:19:54
*/
delete from userinfo WHERE username LIKE 'Tes%';
delete from userinfo WHERE nickname LIKE '测试账号';
