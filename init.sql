CREATE TABLE `city` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `province_name` varchar(20) DEFAULT '' COMMENT '省名',
  `city_name` varchar(20) DEFAULT '' COMMENT '城市名',
  `date` varchar(8) DEFAULT '',
  `confirmed` bigint(11) DEFAULT '0' COMMENT '确诊数量',
  `cured` bigint(11) DEFAULT '0' COMMENT '治愈数量',
  `location_id` bigint(11) DEFAULT '0' COMMENT '邮编',
  `dead` bigint(11) DEFAULT '0' COMMENT '死亡数量',
  `suspected` bigint(11) DEFAULT '0' COMMENT '疑似病例',
  `created_at` bigint(11) DEFAULT NULL COMMENT '创建时间',
  `updated_at` bigint(11) DEFAULT NULL COMMENT '更新时间',
  `is_delete` tinyint(3) DEFAULT '0' COMMENT '是否删除',
  PRIMARY KEY (`id`),
  KEY `idx_created_at` (`created_at`),
  KEY `idx_updated_at` (`updated_at`),
  KEY `idx_is_delete` (`is_delete`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COMMENT='城市统计';

CREATE TABLE `history` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `date` varchar(8) DEFAULT '' COMMENT '日期',
  `confirmed` bigint(11) DEFAULT '0' COMMENT '确诊数量',
  `cured` bigint(11) DEFAULT '0' COMMENT '治愈数量',
  `dead` bigint(11) DEFAULT '0' COMMENT '死亡数量',
  `suspected` bigint(11) DEFAULT '0' COMMENT '疑似病例',
  `created_at` bigint(11) DEFAULT NULL COMMENT '创建时间',
  `updated_at` bigint(11) DEFAULT NULL COMMENT '更新时间',
  `is_delete` tinyint(3) DEFAULT '0' COMMENT '是否删除',
  PRIMARY KEY (`id`),
  KEY `idx_created_at` (`created_at`),
  KEY `idx_updated_at` (`updated_at`),
  KEY `idx_is_delete` (`is_delete`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COMMENT='历史记录表';

CREATE TABLE `province` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `country` varchar(20) DEFAULT '中国' COMMENT '国家',
  `province_name` varchar(20) DEFAULT '' COMMENT '省名',
  `short_name` varchar(20) DEFAULT '' COMMENT '缩略省名',
  `date` varchar(8) DEFAULT '',
  `confirmed` bigint(11) DEFAULT '0' COMMENT '确诊病例',
  `cured` bigint(11) DEFAULT '0' COMMENT '治愈数量',
  `dead` bigint(11) DEFAULT '0' COMMENT '死亡数量',
  `suspected` bigint(11) DEFAULT '0' COMMENT '疑似病例',
  `created_at` bigint(11) DEFAULT NULL COMMENT '创建时间',
  `updated_at` bigint(11) DEFAULT NULL COMMENT '更新时间',
  `is_delete` tinyint(3) DEFAULT '0' COMMENT '是否删除',
  PRIMARY KEY (`id`),
  KEY `idx_created_at` (`created_at`),
  KEY `idx_updated_at` (`updated_at`),
  KEY `idx_is_delete` (`is_delete`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COMMENT='省数据';


CREATE TABLE `world` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(50) DEFAULT '' COMMENT '国家名',
  `date` varchar(8) DEFAULT '' COMMENT '日期',
  `confirmed` bigint(11) DEFAULT '0' COMMENT '确诊数量',
  `dead` bigint(11) DEFAULT '0' COMMENT '死亡数量',
  `cured` bigint(11) DEFAULT '0' COMMENT '确诊数量',
  `suspected` bigint(11) DEFAULT '0' COMMENT '疑似病例',
  `add_dead` bigint(11) DEFAULT '0' COMMENT '死亡增加数量',
  `add_confirmed` bigint(11) DEFAULT '0' COMMENT '增加确诊数量',
  `add_cured` bigint(11) DEFAULT '0' COMMENT '增加治愈数量',
  `add_suspected` bigint(11) DEFAULT '0' COMMENT '增加疑似病例',
  `created_at` bigint(11) DEFAULT NULL COMMENT '创建时间',
  `updated_at` bigint(11) DEFAULT NULL COMMENT '更新时间',
  `is_delete` tinyint(3) DEFAULT '0' COMMENT '是否删除',
  PRIMARY KEY (`id`),
  KEY `idx_created_at` (`created_at`),
  KEY `idx_updated_at` (`updated_at`),
  KEY `idx_is_delete` (`is_delete`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COMMENT='世界疫情';


CREATE TABLE `user` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(50) DEFAULT '' COMMENT '用户名',
  `chinese_name` varchar(50) DEFAULT '' COMMENT '中文名',
  `email` varchar(50) DEFAULT 'example@sse.com.cn' COMMENT '邮箱',
  `phone` varchar(11) DEFAULT '' COMMENT '电话号码',
  `id_num` varchar(20) DEFAULT '' COMMENT '身份证号码',
  `password` varchar(50) DEFAULT NULL COMMENT '密码',
  `is_inner_staff` tinyint(3) DEFAULT '1' COMMENT '是否所内员工',
  `location` text COMMENT '户籍',
  `sh_location` text COMMENT '上海居住地址',
  `created_at` bigint(11) DEFAULT NULL COMMENT '创建时间',
  `updated_at` bigint(11) DEFAULT NULL COMMENT '更新时间',
  `is_delete` tinyint(3) DEFAULT '0' COMMENT '是否删除',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_name` (`name`),
  KEY `idx_created_at` (`created_at`),
  KEY `idx_updated_at` (`updated_at`),
  KEY `idx_is_delete` (`is_delete`),
  KEY `idx_chinese_name` (`chinese_name`),
  KEY `idx_is_inner_staff` (`is_inner_staff`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COMMENT='用户';

CREATE TABLE `daily_info` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(20) NOT NULL DEFAULT '' COMMENT '用户名',
  `date` varchar(8) NOT NULL DEFAULT '' COMMENT '统计日期',
  `in_sh` tinyint(3) NOT NULL DEFAULT '1' COMMENT '是否在沪',
  `health` tinyint(3) NOT NULL DEFAULT '1' COMMENT '健康状况',
  `symptom` varchar(512) DEFAULT '[]' COMMENT '症状',
  `contact_history` tinyint(3) NOT NULL DEFAULT '0' COMMENT '接触史',
  `access_public` tinyint(3) NOT NULL DEFAULT '0' COMMENT '是否进出过公共场所',
  `return_date` varchar(10) DEFAULT '' COMMENT '返沪日期',
  `note` text,
  `created_at` bigint(11) DEFAULT NULL COMMENT '创建时间',
  `updated_at` bigint(11) DEFAULT NULL COMMENT '更新时间',
  `is_delete` tinyint(3) DEFAULT '0' COMMENT '是否删除',
  PRIMARY KEY (`id`),
  KEY `idx_created_at` (`created_at`),
  KEY `idx_updated_at` (`updated_at`),
  KEY `idx_is_delete` (`is_delete`),
  KEY `idk_date` (`date`),
  KEY `idk_health` (`health`),
  KEY `idk_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COMMENT='每日情况统计'
