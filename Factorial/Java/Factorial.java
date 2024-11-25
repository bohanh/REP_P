import java.math.BigInteger;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Factorial {

  public BigInteger factorial(BigInteger n) {
    if ( n == null ) {
      throw new IllegalArgumentException();
    }

    else if ( n.equals(BigInteger.ZERO) ) {
      return BigInteger.ONE;
    }
    else if ( n.signum() == - 1 ) {
      // negative
      throw new IllegalArgumentException("Argument must be a non-negative integer");
    }
    else {
      return n.equals(BigInteger.ONE)
          ? BigInteger.ONE
          : factorial(n.subtract(BigInteger.ONE)).multiply(n);
    }
  }

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    BigInteger number, result;
    number = new BigInteger("100");
    result = new Factorial().factorial(number);
    System.out.println("Factorial of " + number + ": " + result);

  }

}