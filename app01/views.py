from django.shortcuts import render,HttpResponse
import pymysql
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def get_data(request):
    # 连接到MySQL数据库
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        database='pha',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    # 创建游标对象
    cursor = conn.cursor()
    # 执行查询语句，获取数据
    query = "SELECT * FROM pathway"
    cursor.execute(query)
    data = cursor.fetchall()
    # 关闭游标和数据库连接
    cursor.close()
    conn.close()
    # 将数据格式化为Django所需的格式
    pathway_data = list(data)
    # 将数据传递给前端
    return render(request, 'pha synthesis.html', {'data': pathway_data})


