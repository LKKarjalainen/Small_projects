package name.gen;
import java.util.*;

// @author Lassi Karjalainen
// @version 1.1.2023

// Randomly generates a name with some rules.
public class NameGenerator {
	public static void main(String[] args) {
		// Beginning of execution time taking.
		long startTime = System.nanoTime();
		
		// Choose the amount of characters to place in the middle of the name.
		// Note that this amount is doubled in the code.
		int charAmount = 2;
		
		// Lists of vowels and consonants
		List<Character> vowels = Arrays.asList('a','e','i','o','u','y');
		List<Character> consonants = Arrays.asList('r','t','p','s','d','f','g','h','j','k','l','x','c','v','b','n','m');
		
		// Initializes the stringbuilder and char variables we use throughout the algorithm.
		StringBuilder name = new StringBuilder();
		char character;
		
		// Selects a random boolean.
		Random rand = new Random();
		boolean randbool = Math.random() < 0.5;
		
		// Selects the type of the first character based on the random boolean.
		if (randbool) {
			// Selects a random vowel from the vowel list and assigns it to the character variable.
			character = vowels.get(rand.nextInt(vowels.size()));
			
		}
		else {
			// Same as above, but with a consonant.
			character = consonants.get(rand.nextInt(consonants.size()));
			
		}
		// Uppercases the character and adds it to the name.
		character = Character.toUpperCase(character);
		System.out.println("The first letter of the name is "+ character);
		name.append(character);
		
		// Demonstration of denser code.
		// Selects and adds the second character based on the type of the first character.
		if (vowels.contains(Character.toLowerCase(name.charAt(0)))) name.append(consonants.get(rand.nextInt(consonants.size())));
		else name.append(vowels.get(rand.nextInt(vowels.size())));
		
		// This is the part affected by the charAmount variable.
		// Selects and adds two characters based on the type of the previous character.
		for (int i = 0; i < charAmount; i++) {
			
			// If the previous character is a vowel, add two consonants.
			if (vowels.contains(name.charAt(i*2+1))) {
				name.append(consonants.get(rand.nextInt(consonants.size())));
				name.append(consonants.get(rand.nextInt(consonants.size())));
			}
			// Or the other way around.
			else {
				name.append(vowels.get(rand.nextInt(vowels.size())));
				name.append(vowels.get(rand.nextInt(vowels.size())));
			}
			
		}
		
		// Selects and adds a vowel if the previous character is a consonant.
		if (consonants.contains(name.charAt(name.length()-1))) name.append(vowels.get(rand.nextInt(vowels.size())));
		System.out.println("And the name is "+ name);
		
		// End of the algorithm and of execution time taking.
		long elapsedTime = System.nanoTime() - startTime;
		System.out.print("Execution time: ");
		System.out.println(elapsedTime + " nanoseconds");
	}
}