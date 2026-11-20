
from repositorie.reporte_repository import ReporteRepository


class reporteservice:

    @staticmethod
    def total_ventas_caja(numero_caja):
        return ReporteRepository.obtener_total_ventas_caja(numero_caja)

    @staticmethod
    def total_generado_producto(idproducto):
        return ReporteRepository.obtener_total_generado_producto(idproducto)
