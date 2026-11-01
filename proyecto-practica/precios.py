"""Calculadora de precios de práctica para tu primera sesión con Claude Code."""


def precio_con_iva(precio, iva=0.21):
    """Devuelve el precio con el impuesto aplicado."""
    # TODO: redondear el resultado a 2 decimales y rechazar precios negativos con ValueError
    return precio * (1 + iva)


def total(precios, iva=0.21):
    """Suma los precios con impuesto de una lista."""
    return sum(precio_con_iva(p, iva) for p in precios)


if __name__ == "__main__":
    print(total([10, 19.99, 5.5]))
