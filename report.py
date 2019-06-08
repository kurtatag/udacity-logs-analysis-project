#!/usr/bin/env python3

import psycopg2

PROBLEM_01 = 'What are the most popular three articles of all time?'
PROBLEM_02 = 'Who are the most popular article authors of all time?'
PROBLEM_03 = 'On which days did more than 1% of requests lead to errors?'


def pretty_print(problem_description):
    """
    Makes original function output prettier.

    Adds some styling to the original function output.
    Also prints out the problem description before the original
    function prints out the solution.
    """
    def decor_func(original_func):
        def wrapper_func(*args, **kwargs):
            print('\nProblem:')
            print(problem_description)
            print('\nSolution:')
            original_func(*args, **kwargs)
            print('\n\n' + ('=' * 72) + '\n')
        return wrapper_func
    return decor_func


@pretty_print(PROBLEM_01)
def problem_01(conn):
    cur = conn.cursor()

    query = """
        SELECT
            articles.title as article,
            count(1) as views
        FROM
            articles
            LEFT JOIN log
                ON '/article/' || articles.slug = log.path
        GROUP BY articles.title
        ORDER BY views DESC
        LIMIT 3;
    """

    cur.execute(query)

    results = cur.fetchall()

    for row in results:
        print('"{}" -- {:,} views'.format(row[0], row[1]))

    cur.close()


@pretty_print(PROBLEM_02)
def problem_02(conn):
    cur = conn.cursor()

    query = """
        SELECT
            authors.name AS author,
            count(1) AS views
        FROM
            authors
            LEFT JOIN articles
                ON authors.id = articles.author
            LEFT JOIN log
                ON '/article/' || articles.slug = log.path
        GROUP BY authors.name
        ORDER BY views DESC;
    """

    cur.execute(query)

    results = cur.fetchall()

    for row in results:
        print('{} -- {:,} views'.format(row[0], row[1]))

    cur.close()


@pretty_print(PROBLEM_03)
def problem_03(conn):
    cur = conn.cursor()

    query = """
        WITH all_hits AS (
            SELECT
                to_char(time, 'MONTH DD, YYYY') as day,
                count(*) as requests
            FROM log
            GROUP BY day
        ), errors AS (
            SELECT
                to_char(time, 'MONTH DD, YYYY') as day,
                count(*) as requests
            FROM log
            WHERE status LIKE '%404%'
            GROUP BY day
        )
        SELECT
            all_hits.day,
            errors.requests::decimal / all_hits.requests * 100
        FROM
            all_hits
            LEFT JOIN errors
                ON all_hits.day = errors.day
        WHERE errors.requests::decimal / all_hits.requests * 100 > 1
        ORDER BY all_hits.day;
    """

    cur.execute(query)

    results = cur.fetchall()

    for row in results:
        print('{} -- {:.2f}% errors'.format(' '.join(row[0].split()), row[1]))

    cur.close()


if __name__ == "__main__":

    with psycopg2.connect('dbname=news') as conn:
        problem_01(conn)
        problem_02(conn)
        problem_03(conn)
