<?php
include("zzz.php");//script con datos de conexion y creacion de $conn

$filename = 'MiBaseDeDatos.sql'; //Archivo sql que exporte localmente y subo por FTP al servidor remoto

$templine = '';
$lines = file($filename); // Read entire file
foreach ($lines as $line){
		
	if (substr(trim($line), 0, 2) == '--'  || substr(trim($line), 0, 2) == '/*' && substr(trim($line), -3, 2) <> '*/') // Skip all comments
    	continue;
	
	$templine .= trim($line);
	
if (substr(trim($line), -1, 1) == ';' ){
	
	$st=$conn->query($templine);

	//mysql_query($templine) or print('Error: '.mysql_error() . '<br >');
	
	
    $templine = '';
}
}

?>