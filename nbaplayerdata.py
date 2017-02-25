#! -*-coding:utf-8-*-
#!/usr/bin/env python3

# http://nba.sports.163.com/team/21/stat/
import urllib.request

def get_player_data():
    print("球员名字,所属球队,场次,时间,投篮投中数,投篮出手数,投篮命中率,三分球投中数,三分球出手数,三分球命中率,罚篮投中数,罚篮出手数,罚篮命中率,篮板进攻,篮板防守,篮板总计,助攻,失误,抢断,盖帽,犯规,得分")
    l = list(range(1,30))
    l.append(5312)
    for team_id in l:
        # urllib.request.urlopen()
        # if urllib.parse.getcode() == 404:
            # print(team_id)
        url = "http://nba.sports.163.com/team/"+ str(team_id) +"/stat/"
        # url = "http://nba.sports.163.com/team/1/stat/"
        # fname = "player_data.csv"
        # urllib.request.urlretrieve(url,fname)
        if urllib.request.urlopen(url).getcode() == 404:
            print("no team")
        else:
            try:
                html = urllib.request.urlopen(url).read()
            finally:
                html = html.decode('UTF-8')
                table = html[html.find('tb-title'):html.find('</table>')]
                # print(table)
                team_name = table[table.find('tb-title">'):table.find('球员数据')][10:]
                # 从每队的球员数据页获得球队名称
                # print(team_name)
                # print("球员名字,所属球队,场次,时间,投篮投中数,投篮出手数,投篮命中率,三分球投中数,三分球出手数,三分球命中率,罚篮投中数,罚篮出手数,罚篮命中率,篮板进攻,篮板防守,篮板总计,助攻,失误,抢断,盖帽,犯规,得分")
                players_qote = table[table.find('<a href'):table.find('</table>')]
                # print(players_qote)
                """
                print(player_qote.count('/tbody'))
                """
                players_str = players_qote.split('</tbody>')
                # print(player_str)
                for i in range(0,players_qote.count('/tbody')):
                    # player = players_str[i].strip().replace('</td><td>',',')
                    # s = player_str[1].split('</td>>')
                    s = players_str[i].split('</td>')
                    # s代表单个球员
                    # print(s)
                    # data_list=[]
                    player_data_str=""
                    # data_list.insert(1, team_name)
                    player_data_str= team_name+ player_data_str
                    for j in range(0,len(s)-1):
                        if j == 0:
                            player_name = s[0][s[0].find('/">'):s[0].find('</')][3:]
                            # print(player_name)
                            # data_list.insert(0, player_name)
                            player_data_str = player_name + ',' + player_data_str
                        else:
                            data = s[j][s[j].find('<td>'):][4:]
                            # data_list.append(data)
                            player_data_str = player_data_str + ','+ str(data)
                    # print(str(data_list))
                    print(player_data_str)


if __name__=='__main__':
    get_player_data()
