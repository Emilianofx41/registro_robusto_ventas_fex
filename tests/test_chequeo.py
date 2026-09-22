import main

def test_registrar_venta():
    p_unit = 10
    cant = 5
    total = p_unit * cant

    assert main.registrar_venta(p_unit, cant) == total