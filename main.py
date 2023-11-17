from fastapi import FastAPI
from clickhouse_driver import connect


app = FastAPI()


conn = connect('clickhouse://default:click@localhost:9000/default')
cursor = conn.cursor()


def create_table():
    cursor.execute(
        '''
        CREATE TABLE lenta_ru_news(
            `url` String,
            `title` String,
            `text` String,
            `topic` String,
            `tags` String,
            `date` Date
        )
        ENGINE = MergeTree
        PRIMARY KEY url
        '''
    )


@app.post('/getWords')
def get_words():
    cursor.execute(
        '''
        SELECT arrayJoin(splitByNonAlpha(text)) AS word, count(*) AS ct
        FROM lenta_ru_news
        GROUP BY 1
        ORDER BY 2 DESC
        LIMIT 100;
        '''
    )
    rows = cursor.fetchall()
    return rows


if __name__ == "__main__":
    create_table()
