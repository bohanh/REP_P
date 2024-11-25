public class GreatestCommonDivisor {

    public static long GreatestCommonDivisor(long a, long b) {
        long factor = Math.min(a, b);
        for (long loop = factor; loop > 1; loop--) {
            if (a % loop == 0 && b % loop == 0) {
                return loop;
            }
        }
        return 1;
    }

    public static void main(String[] args) {
        long a = 12;
        long b = 18;
        System.out.println("The greatest common divisor of " + a + " and " + b + " is " + GreatestCommonDivisor(a, b));
    }
}