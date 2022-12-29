package nimigeni;
import java.util.*;



// Luo satunnaisen nimen vokaaleista ja konsonanteista noudattaen muutamaa sääntöä.
public class nimigeni {
	public static void main(String[] args) {
		long startTime = System.nanoTime();
		
		int kirMaara = 1;
		
		// Listat vokaaleista ja konsonanteista.
		List<Character> vokaalit = Arrays.asList('a','e','i','o','u','y');
		List<Character> konsonantit = Arrays.asList('r','t','p','s','d','f','g','h','j','k','l','x','c','v','b','n','m');
		
		// Alustetaan nimi ja eK(ensimmäinen kirjain)
		StringBuilder nimi = new StringBuilder();
		char eK;
		
		// Luodaan randomi arvot ja lisätään nimen ensimmäinen kirjain.
		Random rand = new Random();
		boolean randbool = Math.random() < 0.5;
		if (randbool) {
			eK = vokaalit.get(rand.nextInt(vokaalit.size()));
			
		}
		else {
			eK = konsonantit.get(rand.nextInt(konsonantit.size()));
			
		}
		eK = Character.toUpperCase(eK);
		nimi.append(eK);
		System.out.println("Ensimmäinen kirjain on "+ eK);
		
		// Aseta toiseksi kirjaimeksi joko konsonantti tai vokaali riippuen ensimmäisestä kirjaimesta.
		if (vokaalit.contains(Character.toLowerCase(nimi.charAt(0)))) nimi.append(konsonantit.get(rand.nextInt(konsonantit.size())));
		else nimi.append(vokaalit.get(rand.nextInt(vokaalit.size())));
		
		// Muodostetaan loput nimestä.
		for (int i = 0; i < kirMaara; i++) {
			// Jos ensimmäinen kirjain on vokaali, niin lisää kaksi konsonanttia.
			if (vokaalit.contains(nimi.charAt(i*2+1))) {
				nimi.append(konsonantit.get(rand.nextInt(konsonantit.size())));
				nimi.append(konsonantit.get(rand.nextInt(konsonantit.size())));
			}
			// Ja vastatapaus.
			else {
				nimi.append(vokaalit.get(rand.nextInt(vokaalit.size())));
				nimi.append(vokaalit.get(rand.nextInt(vokaalit.size())));
			}
			
		}
		
		// Jos viimeinen kirjain on konsonantti, niin lisää vokaali.
		if (konsonantit.contains(nimi.charAt(nimi.length()-1))) nimi.append(vokaalit.get(rand.nextInt(vokaalit.size())));
		System.out.println("Ja nimi on "+ nimi);
		
		long elapsedTime = System.nanoTime() - startTime;
		System.out.println(elapsedTime + " ns");
	}
}