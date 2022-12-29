use warnings;
use strict;
use Time::HiRes;

#Author Lassi Karjalainen
#Version 23.12.2022.


#Ajanoton alku
my $start_time = Time::HiRes::gettimeofday();

#Valitsee kirjainten määrän. Numero on puolet lisättävästä määrästä eli esimerkiksi $kirMaar = 1
#lisää 2 kirjainta.
my $kirMaar = 2;

#Luodaan sana, vokaali ja konsonantti arrayt
my @nimi = ();
my @vokaalit = ('a','e','i','o','u','y');
my @konsonantit = ('r','t','p','s','d','f','g','h','j','k','l','x','c','v','b','n','m');


#Arvotaan satunnainen boolean arvo.
#Voisi olla pelkkä "my $randbool;", jolloin ohjelma olisi puolet ajasta hieman nopeampi ja toiset
#puolet ajasta paljon hitaampi.
my $randbool = 0;
if (int(rand(11)) > 5) {
	$randbool = 1;
}
else {
	$randbool = 0;
}

#Luodaan sijoitettava kirjain ja valitaan ensimmäinen kirjain vokaaleista tai konsonanteista
#aikaisemman boolean arvon perusteella ja toinen kirjain ensimmäisen kirjaimen perusteella.
my $kirjain;
if ($randbool == 1) {
	$kirjain = uc($vokaalit[rand @vokaalit]);
	push(@nimi, $kirjain);
	print(qq"Ensimmainen kirjain on $kirjain\n");
	$kirjain = $konsonantit[rand @konsonantit];
	push(@nimi, $kirjain);
}
else {
	$kirjain = uc($konsonantit[rand @konsonantit]);
	push(@nimi, $kirjain);
	print(qq"Ensimmainen kirjain on $kirjain\n");
	$kirjain = $vokaalit[rand @vokaalit];
	push(@nimi, $kirjain);
}

#Arvotaan ja lisätään nimen keskiosuus. Tämä on säädettävät muuttujalla $kirMaar koodin alussa.
#Tämä on tarkoituksella tehty hitaalla ja hankalasti luettavalla tavalla, että voin verrata
#optimisoinnin vaikutusta koodiin myöhemmällä versiolla. Yllä oleva arvonta tapa on nopeampi.
for (my $i = 0; $i < $kirMaar; $i++) {
	$kirjain = lc($nimi[$i+1]);
	if (grep( /^$kirjain$/, @vokaalit )) {
		my $maksimi = scalar @konsonantit;
		my $kirIndex = 0 + int(rand($maksimi - 0));
		push(@nimi, $konsonantit[$kirIndex]);
		push(@nimi, $konsonantit[$kirIndex]);
	}
	else {
		my $maksimi = scalar @vokaalit;
		my $kirIndex = 0 + int(rand($maksimi - 0));
		push(@nimi, $vokaalit[$kirIndex]);
		push(@nimi, $vokaalit[$kirIndex]);
	}
}

#Valitaan nimen viimeinen kirjain aikasemman kirjaimen perusteella.
$kirjain = $nimi[@nimi-1];
if (grep( /^$kirjain$/, @vokaalit )) {
	$kirjain = $konsonantit[rand @konsonantit];
	push(@nimi, $kirjain);
}
print("Nimi on ");
print(@nimi,"\n");


#Ajanoton loppu ja tulostus
my $stop_time = Time::HiRes::gettimeofday();
print("Runtime:");
printf("%.8f", $stop_time - $start_time);
print(" s\n");