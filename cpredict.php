<?php
//GET Parameters
// instance ip address 18.222.253.208

$Vehicles = $_GET["Vehicles"];
$Road Surface = $_GET["Road Surface"];
$Lighting Conditions = $_GET["Lighting Conditions"];
$Weather Conditions= $_GET["Weather Conditions"];
$Casualty Victim = $_GET["Casualty Victim"];
$Sex of Casualty = $_GET["Sex of Casualty"];
$Age of Casualty = $_GET["Age of Casualty"];
$Type of Vehicle= $_GET["Type of Vehicle"];


//this is way to pass argument in php through which model will get execute.

//http://here is instance ip address which is now(18.222.253.208)/predict.php?lotsize=2000&driveway=1&recroom=1&fullbase=1&gashw=1&airco=1&garagepl=1&prefarea=1


//Execute the model
system("/usr/anaconda/bin/python3 casualty_severity_prediction_model.py ".Vehicles." ".$Road Surface." ".$Lighting Conditions." ".$Weather Conditions." ".$Casualty Victim." ".$Sex of Casualty." ".$Age of Casualty." ".$Type of Vehicle." 2>&1");


