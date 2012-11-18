<?php

// recibo las variables de formulario

$nombre = $_POST['nombre'];
$mail = $_POST['email'];
$mensaje = $_POST['mensaje'];

// Te muestro las varibales 

echo $nombre;
echo "<br />";
echo $mail;
echo "<br />";
echo $mensaje;

?>