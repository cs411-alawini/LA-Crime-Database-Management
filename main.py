from app import db
from sqlalchemy import text
from app import app

# if __name__ == '__main__':
#     conn = db.connect()
#     query_results = conn.execute(text("SELECT Location.areaName, COUNT(Location.areaName) AS CRIMECOUNT FROM (Report JOIN Location ON Location.area = Report.area) GROUP BY Location.areaName ORDER BY CRIMECOUNT LIMIT 15;")).fetchall()
#     conn.close()
#     print(query_results)

if __name__ == "__main__":
    app.run(debug=True)