import java.math.BigInteger;

public class LeastCommonMultiple {
    public static void main(String[] args) {
        // Using BigInteger for very large numbers
        BigInteger m = new BigInteger("2562047788015215500854906332309589561");
        BigInteger n = new BigInteger("6795454494268282920431565661684282819");

        // Calculate the Least Common Multiple (LCM)
        BigInteger lcm = m.multiply(n).divide(m.gcd(n));

        System.out.println("LCM of " + m + " and " + n + " is: " + lcm);
    }
}