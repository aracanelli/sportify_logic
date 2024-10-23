import psycopg2 # type: ignore
from dotenv import load_dotenv # type: ignore
import os

# Load environment variables
load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
def get_group_id(name):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    cursor.execute("select group_id from groups where name = '" + name + "'")

    group_id = cursor.fetchone()

    cursor.close()
    conn.close()
    return group_id[0]

def fetch_players(group_id):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT p.player_id, p.nick_name, p.level, pg.sub,
        case when exists(select 1 from history 
                            where player1_id=p.player_id 
                            or player2_id=p.player_id
                            or player3_id=p.player_id
                            or player4_id=p.player_id
                            and group_id = """ + str(group_id) +
                            """) then true else false end as has_played
        FROM player_groups pg, players p 
        WHERE p.player_id = pg.player_id and group_id = 
    """ + str(group_id))
    games = cursor.fetchall()

    cursor.close()
    conn.close()

    return games

def fetch_history(group_id):
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT player1_id, player2_id, player3_id, player4_id, score1, score2
        FROM history where group_id = 
    """ + str(group_id) + " order by match_id asc")

    history = cursor.fetchall()

    cursor.close()
    conn.close()

    return history