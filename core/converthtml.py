import os
import datetime as dt

HTML_PATH = os.path.normpath('../html/base.html')
base_html = """'<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Stock Report</title>
</head>
<body>
<h1>STOCK REPORT - {date}</h1>
    {tables}
</body>
</html>"""

def get_tables(stocks):
    tables = []
    count = 1
    for s in stocks:
        tables.append("""
        <h1><a href=https://ca.finance.yahoo.com/quote/{stockname}>{stockname}</a></h1>
        <img src="cid:image{count}">""".format(stockname=s,
                                                count=count)
        )
        count += 1
    return ''.join(tables)

def get_final_html(stocks):
    final_html = base_html.format(date=dt.datetime.today().date(),tables=get_tables(stocks))
    with open(HTML_PATH, 'w') as f:
        f.write(final_html)
                                