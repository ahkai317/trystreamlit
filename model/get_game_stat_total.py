# -*- coding: utf-8 -*-
import setup

with setup.Conn_DB('stat_db').cursor() as cursor:

    sql = '''
		SELECT * FROM `sys_db`.`activity_list`
			COUNT(DISTINCT `player_id`) AS `player_count`,
			IFNULL(SUM(`bet_count`), 0) AS `bet_count`,
			IFNULL(SUM(`bet`), 0) AS `bet`,
			IFNULL(SUM(`valid_bet`), 0) AS `valid_bet`,
			IFNULL(SUM(`game_win`), 0) AS `game_win`,
			IFNULL(SUM(`jp_win`), 0) AS `jp_win`,
			IFNULL(SUM(`company_profit`), 0) AS `company_profit`,
			IFNULL(SUM(`valid_bet`)/SUM(`bet_count`), 0) AS `avg_valid_bet`
		FROM `stat_db`.`player_game_stat
	'''

    cursor.execute(sql)

    setup.Conn_DB('stat_db').commit()

    data = cursor.fetchall() # -> tuple

print(data)