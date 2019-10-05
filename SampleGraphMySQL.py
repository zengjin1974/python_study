import pymysql
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

class SampleMysql:
    def show(self):
        sql = "SELECT * FROM beer_temperature"

        eng = pymysql.connect(host='localhost',
                              user='amazon',
                              password='Admin2019',
                              db='amazon',
                              charset='utf8')

        df = pd.read_sql(sql, eng)

        print(df)

        plt.subplot(1, 1, 1)

        x = np.array(df["temperature"].tolist())
        y = np.array(df["beer_sale"].tolist())

        colors = y * 10
        area = y * 100

        plt.scatter(x, y, c=colors, marker="o", s=area)

        plt.title("Jan-Aug Temperature vs Bear Sale", loc="center")

        for a, b in zip(x, y):
            plt.text(a, b, b, ha='center', va="center", fontsize=10, color="white")

        plt.xlabel('Temperature')
        plt.ylabel('Bear Sale')

        plt.grid(False)

        plt.show()


sm = SampleMysql()
sm.show()

