from flask import Flask, render_template
import sqlite3
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():

    # Connect database
    conn = sqlite3.connect("database.db")

    # Read sales table
    df = pd.read_sql_query("SELECT * FROM sales", conn)

    # Dashboard analytics
    total_sales = round(df['Sales'].sum(), 2)

    total_orders = len(df)

    top_category = df.groupby('Category')['Sales'].sum().idxmax()

    top_product = df.groupby('Product Name')['Sales'].sum().idxmax()

    conn.close()

    return render_template(
        "index.html",
        sales=total_sales,
        orders=total_orders,
        category=top_category,
        product=top_product
    )

if __name__ == '__main__':
    app.run(debug=True)