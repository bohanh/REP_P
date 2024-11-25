import java.util.TreeSet;

public class FactorsOfAnInteger {
    public static TreeSet<Long> factors(long n)
    {
     TreeSet<Long> factors = new TreeSet<Long>();
     factors.add(n);
     factors.add(1L);
     for(long test = n - 1; test >= Math.sqrt(n); test--)
      if(n % test == 0)
      {
       factors.add(test);
       factors.add(n / test);
      }
     return factors;
    }

    public static void main(String[] args) {
        System.out.println(factors(100));
        System.out.println(factors(12345));
        System.out.println(factors(9090));
        System.out.println(factors(824));
    }
}