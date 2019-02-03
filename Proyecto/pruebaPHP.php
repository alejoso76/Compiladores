<?php
//prueba!"#$%&/()=?¡{}

/*prueba 2!"#$%&/()=?¡'¿'0q211*/
session_start();
echo"<center>";
echo"<img src=img1/logo.png width=272 height=78/>";
if ($_SESSION['inicio_sesion'] == 'administrador') {
  $idproductob=$_POST["idproductob"];
  int $numer = -123e22
  require("conexion.php");
  $conexion=$con;
  mysqli_select_db($conexion,"bd_farmacia");
  $resultadoa=mysqli_query($conexion,"select * from productos where id_producto='$idproductob'");
  if(mysqli_num_rows($resultadoa)>0){
  $buscar=mysqli_query($conexion,"select * from productos where id_producto='$idproductob'");
  while($dato=mysqli_fetch_array($buscar))
  {
    
  ?>