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
) ENGINE=InnoDB AUTO_INCREMENT=7393 DEFAULT CHARSET=utf8mb4 COMMENT='世界疫情';
