Presupuestario
==============

1) Se van a definir como hacer las diferentes partes de la estructura del FrontEnd en la Aplicación.

Detalles a realizar en la aplicación
=====================================

1. Despues del acceso de usuario armar el dashboard por usuario, con la información de las cuentas, sobre el plan de cuentas completo sobre las cuentas padre. Mostrar una gráfica para visualizar a nivel rapido lo que tengan asignado y lo que han consumido hasta el momento.

Si el usuario tiene permisos para realizar reservar y/o ordenes de pago, poner accesos a los Formularios respectivos según el nivel de acceso de la app.
>>>>>>> 845467b8b9718c34c06bf5d4ca27d54bd6997193

2. Al ingresar a cada cuenta tener la información de toda actividad que se ha hecho con respecto a esta cuenta a nivel de consulta, esta información será mostrada en tipo Grid.

3. Si el usuario tiene permisos para hacer una reserva de gasto o una afectación de pago, o hacer hacia atrás la reserva.

circuito de afectación de la cuenta
====================================

1. hacer la reserva del gasto y queda pendiente hasta hacer la confirmación de pago. Esta reserva puede cancelarse por diferentes motivos, y en ese caso la misma, vuelva atrás la afectación del importe reservado anteriormente.
La información de la cuenta, debe llevar Monto Total Presupuestado – Reservas – Imputaciones.

Es decir que la información debe reflejar cuanto hay Asigando, y cuento en estado reservado. Todo lo restante, deberá ser reflejado por las Ordenes de Pago. Que es finalmente cuando se descuenta el Monto a imputar.

Orden de Pago: Estas provienen a partir de la Reserva efectuada, y pueden ser a varios proveedores, y con diferentes importes de la reserva previa. Cuando se realiza esto, recien ahi se descuenta el importe a la Cuenta y la reserva desaparece, o cambia de estado ( VER LOGICA CONVENIENTE),