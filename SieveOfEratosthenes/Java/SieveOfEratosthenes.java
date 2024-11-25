import java.util.LinkedList;

public class SieveOfEratosthenes {
        // Method to find primes using the Sieve of Eratosthenes
        public static LinkedList<Integer> sieve(int n) {
                if (n < 2) return new LinkedList<Integer>();

                LinkedList<Integer> primes = new LinkedList<Integer>();
                LinkedList<Integer> nums = new LinkedList<Integer>();

                // Add all numbers from 2 to n
                for (int i = 2; i <= n; i++) {
                        nums.add(i);
                }

                // Sieve algorithm: remove non-primes
                while (nums.size() > 0) {
                        int nextPrime = nums.remove(); // The first number is always prime
                        for (int i = nextPrime * nextPrime; i <= n; i += nextPrime) {
                                nums.removeFirstOccurrence(i); // Remove multiples of nextPrime
                        }
                        primes.add(nextPrime); // Add prime to the result list
                }
                return primes;
        }

        // Main method to test the sieve
        public static void main(String[] args) {
                // Test the sieve function
                int n = 50; // Find all primes up to 50
                LinkedList<Integer> primes = sieve(n);

                // Print the primes
                System.out.println("Primes up to " + n + ": " + primes);
        }
}
