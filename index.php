<html>
<head>
	<meta charset="utf8"/>
	<link rel="stylesheet" href="css/style.css">
</head>
<body>
<?php
	$jeux = array_diff(scandir("samples"),array(".",".."));
	foreach ($jeux as $jeu) {
		$xml = simplexml_load_file("http://thegamesdb.net/api/GetGame.php?name=$jeu&platform=PC");
		$xml = $xml[0];
		$baseUrlImg = $xml->baseImgUrl;
		$game = $xml->Game;
		$name = $game->GameTitle;
		$date = new DateTime($game->ReleaseDate);
		$date_str = $date->format("d M Y");
		$yt = $game->Youtube;
		$edit = $game->Publisher;
		$dev = $game->Developer;
		$img = $game->Images->boxart;
		$desc = $game->Overview;

		print "<div class='game'><a href='$yt'><img src='$baseUrlImg$img'/></a><h4>$name ($date_str)</h4></div>";
	}
?>
</body>