from django.db import models


class Restaurante(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Sucursal(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Mesa(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    numero = models.IntegerField()
    capacidad = models.IntegerField()

    def __str__(self):
        return f"Mesa {self.numero}"


class EstadoReserva(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    estado = models.ForeignKey(EstadoReserva, on_delete=models.CASCADE)

    fecha = models.DateField()
    hora = models.TimeField()
    cantidad_personas = models.IntegerField()

    def __str__(self):
        return f"Reserva {self.id}"


class MetodoPago(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Pago(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)

    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()

    def __str__(self):
        return f"Pago {self.id}"