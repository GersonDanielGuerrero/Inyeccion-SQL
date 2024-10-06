from django.shortcuts import render
from django.db import connection

def login_view(request):
    error_message = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Consulta SQL vulnerable
        query = f"SELECT * FROM user WHERE username = '{username}' AND password = '{password}'"
        #query = f"INSERT INTO user (username, password) VALUES ('{username}', '{password}')"
        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                result = cursor.fetchone()
            except Exception as e:
                error_message = str(e)

        if result:
            return render(request, "lista_productos.html")
        else:
            error_message = "Login failed!"

    return render(request, "login.html", {"error_message": error_message})

from django.db import connection
from django.shortcuts import render

def products_view(request):
    error_message = ""
    selected_type = request.GET.get("tipo", "")  # Obtener el tipo de la URL

    # Consulta SQL vulnerable
    query = f"SELECT * FROM product WHERE type = '{selected_type}'"
    with connection.cursor() as cursor:
        try:
            cursor.execute(query)
            products = cursor.fetchall()
        except Exception as e:
            return render(request, "lista_productos.html", {"error_message": str(e)})

    return render(request, "lista_productos.html", {"products": products, "selected_type": selected_type})


def user_info(request):
    user_id = request.GET.get("id")

    query = f"SELECT * FROM login_user WHERE id = {user_id}"
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()

    return render(request, "user_info.html", {"user": result})
