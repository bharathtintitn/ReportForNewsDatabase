# This module runs on python 2.7
'''This module will generate report for news database in psql. '''
import datetime
import psycopg2

class ReportingTool(object):
    '''Connect new db and fetch report.'''
    def __init__(self, db_name):
        self.db_name = db_name

    def get_db_connection(self):
        '''get db connection.'''
        conn = psycopg2.connect("dbname="+self.db_name)
        return conn

    def execute_query(self, query):
        '''execute given query and return result.'''
        conn = self.get_db_connection()
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        conn.close()
        return rows

def create_report(file_name, message):
    '''This method create a file and adds message.'''

    with open(file_name + '.txt', 'w') as file_pointer:
        for line in message:
            file_pointer.write(line + '\n')

def three_popular_articles(db_connection):
    '''Fetch top 3 popular articles from db.'''
    query = '''select num, title, author
            from (select count(*) num, path 
                  from log
                  group by path 
                  order by num Desc 
                  limit 10) l, articles a
            where l.path = '/article/' || a.slug
            limit 3;'''

    message = []
    result = db_connection.execute_query(query)
    for row in result:
        #print "row: ", row[1], "count:", row[0]
        text = '"' + row[1] + '"' + '-- ' + str(row[0]) + ' views'
        print text
        message.append(text)
    create_report('3_popular_articles', message)
    #self.close_db_connection(conn)

def popular_author(db_connection):
    '''
    Method to fetch most popular authors
    and return top one.
    '''
    query = '''select sum(num) total, au.name
               from (select count(*) num, path
                     from log
                     group by path
                     order by num Desc
                     limit 10) l, articles a, authors au
               where l.path = '/article/' || a.slug
               and a.author = au.id
               group by au.name
               order by total Desc;'''

    message = []
    result = db_connection.execute_query(query)
    for row in result:
        text = row[1] + '-- ' + str(row[0]) + ' views'
        message.append(text)
        print text
    create_report('popular_author', message)

def day_with_highest_request_error(db_connection):
    '''
    Method returns day with most http failures.
    '''
    query = '''
        select t.count request, l.count failed, l.date, (t.count/100) percentage from
        (select count(*) count , date from
        (select status, path, cast(time as date) date from log) a
        group by date) t,
        (select count(*) count, date 
        from (select status, path, cast(time as date) date 
        from log where status = '404 NOT FOUND') b
        group by date) l
        where l.date = t.date
        and l.count > (t.count/100);
        '''
    result = db_connection.execute_query(query)
    message = []
    for row in result:
        date = datetime.datetime.strptime(str(row[2]), '%Y-%m-%d')
        date = date.strftime('%b %d, %Y')
        percentage = (int(row[1])/float(row[0]))*100
        text = date + ' -- ' +  str(round(percentage, 2)) + '% errors'
        message.append(text)
        print text
    create_report('day_on_which_more_request_errors', message)


if __name__ == "__main__":

    report = ReportingTool('news')
    three_popular_articles(report)
    popular_author(report)
    day_with_highest_request_error(report)
