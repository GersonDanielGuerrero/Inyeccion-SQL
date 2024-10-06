from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    class Meta:
        db_table = 'user'

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=100, default='electrodomesticos')

    sql= """
INSERT INTO product (name, description, price, type) VALUES
('Coca Cola', 'Bebida gaseosa', 1.50, 'bebidas'),
('Pepsi', 'Bebida gaseosa', 1.40, 'bebidas'),
('Chocolatina', 'Bebida de chocolate', 0.65, 'bebidas'),
('Queso Manchego', 'Queso de oveja', 2.50, 'lacteos'),
('Leche', 'Leche entera', 1.20, 'lacteos'),
('Yogurt', 'Yogurt natural', 0.80, 'lacteos'),
('Frijoles 1lb', 'Frijoles rojos', 0.80, 'granos'),
('Cebada 1lb', 'Cebada perlada', 1.00, 'granos'),
('Arroz 1lb', 'Arroz blanco', 0.80, 'granos'),
('Chorizo ahumado', 'Chorizo de cerdo', 1.50, 'embutidos'),
('Salchichas', 'Salchichas de cerdo', 1.20, 'embutidos'),
('Mortadela', 'Mortadela de cerdo', 1.00, 'embutidos');
"""
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'product'
    
class Sale(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.user.username} - {self.product.name} - {self.quantity} - {self.total}'
