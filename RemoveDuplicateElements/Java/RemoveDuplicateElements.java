import java.util.LinkedHashSet;
import java.util.Set;
import java.util.Iterator;

public class RemoveDuplicateElements {
    public static int[] removeDuplicates(int[] values) {
        // Use a LinkedHashSet to preserve order
        Set<Integer> set = new LinkedHashSet<>();
        for (int value : values) {
            set.add(value);
        }
        int[] uniqueValues = new int[set.size()];
        Iterator<Integer> iterator = set.iterator();
        int index = 0;
        while (iterator.hasNext()) {
            uniqueValues[index++] = iterator.next();
        }
        return uniqueValues;
    }

    public static void main(String[] args) {
        int[] values = {1, 2, 3, 2, 4, 1, 5};
        int[] result = removeDuplicates(values);
        for (int value : result) {
            System.out.print(value + " ");
        }
    }
}
