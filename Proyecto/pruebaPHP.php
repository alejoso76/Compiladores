<?php//prueba!"#$%&/()=?¡{}

/*prueba 2!"#$%&/()=?¡'¿'0q211*/
?>


<?php
session_start();
echo"<center>";
echo"<img src=img1/logo.png width=272 height=78/>";
if ($_SESSION['inicio_sesion'] == 'administrador') {
  $idproductob=$_POST["idproductob"];
  $numer = -123E-22
  require("conexion.php");
  $conexion=$con;
  mysqli_select_db($conexion,"bd_farmacia");
  $resultadoa=mysqli_query($conexion,"select * from productos where id_producto='$idproductob'");
  if(mysqli_num_rows($resultadoa)>0){
  $buscar=mysqli_query($conexion,"select * from productos where id_producto='$idproductob'");
  while($dato=mysqli_fetch_array($buscar))
  {
    
  ?>
  <html>
    <head>
      <meta charset="utf-8">
      <title>SuperDrogas: Buscar</title>
      <link rel="stylesheet" href="style.css">
    </head>
    <body>
      <div class="loginBox">
        <div class="glass">
          <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
          <form method=POST action=actualizar.php>
            <h2>Actualizar Producto</h2><center>
            <p> <table width=300 border=0>

              <div class="inputBox">
                <th scope=row>ID:</th>
                <td><input type=num required name="idproductob" value=<?php echo $dato["id_producto"];?> placeholder="ID producto"></td>
                <span><i class="fa fa-user" aria-hidden="true"></i></span>
              </div>
          
            <tr>
              <div class="inputBox">
                <th scope=row>Nombre producto:</th>
                <td><input type=text required name="nombreproductob"required value=<?php echo $dato["nombre"];?> placeholder="Nombre del producto"/></td>
                <span><i class="fa fa-user" aria-hidden="true"></i></span>
              </div>
            </tr>
            <tr>
              <div class="inputBox">
                <th scope=row>Descripción:</th>
                <td><input type="text"required name="descripcionproductob"required value=<?php echo $dato["descripcion"];?> placeholder="Descripción del producto"/></td>
                <span><i class="fa fa-text" aria-hidden="true"></i></span>
              </div>
            </tr>
            <tr>
              <div class="inputBox">
                <th scope=row>Laboratorio:</th>
                <td><input type=string name=labproductob required value=<?php echo $dato["laboratorio"];?> /></td>
                <span><i class="fa fa-string" aria-hidden="true"></i></span>
              </div>
            </tr>
            <tr>
              <div class="inputBox">
                <th scope=row>Precio:</th>
                <td><input type=double name=precioproductob required  value=<?php echo $dato["precio"];?>  /></td>
                <span><i class="fa fa-text" aria-hidden="true"></i></span>
              </div>
            </tr>
            <tr>
              <div class="inputBox">
                <th scope=row>Cantidad (Stock):</th>
                <td><input type=number name=cantproductob required  value=<?php echo $dato["cantidad"];?>  /></td>
                <span><i class="fa fa-text" aria-hidden="true"></i></span>
              </div>
            </tr>
		        <tr>
              <div class="inputBox">
                <th scope=row>Descripción:</th>
                <td><input type="text"required name="grupot"required value=<?php echo $dato["grupo_terapeutico"];?> placeholder="Grupo terapeútico"/></td>
                <span><i class="fa fa-text" aria-hidden="true"></i></span>
              </div>
            </tr>
            <tr>
              <div class="inputBox">
                <th scope=row>Fecha de vencimiento:</th>
                <td><input type=date name=vencerfecha required value=<?php echo $dato["fecha_vencimiento"];?> /></td>
                <span><i class="fa fa-date" aria-hidden="true"></i></span>
              </div>
            </tr>
            <tr>
              <div class="inputBox">
                <th scope=row>Fórmula médica?:</th>
                <td><input type=number name=formuproductob required  value=<?php echo $dato["formula_medica"];?>  /></td>
                <span><i class="fa fa-text" aria-hidden="true"></i></span>
              </div>
            </tr>

      </table>


      <p                                                        >                                                                                     
      <input name=ingresarprodca type=submit value=OK Actualizar producto/>
      <p><input type=reset name=borrar value=Limpiar>
      <p>
          <a href=inicio.php>Volver</a>
          
      </center>

      <?php
      }
      }
      else{
        
        echo"<style type=text/css>
      body {
        background-image: url(img1/fondo2.jpg);
      }
      </style>";
        
      echo"<h3>ID no encontrado</h3>";
      echo"<h4>Inserte un ID válido</h4>";
      echo "<center><img src='img1/error.png'></center>";
      echo"<a href=inicio.php>Volver</a>";
        }
      }else{
        echo "<h3>Usuario sin permisos</h3>";
        echo"<a href=inicio.php>Volver</a>";
      }
    ?>
    </center>
    </html>
