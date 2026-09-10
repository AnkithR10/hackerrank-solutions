// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/challenges/java-string-tokens/problem?isFullScreen=true
// Problem     Java String Tokens
// Difficulty  Easy
// Subdomain   Strings
// Platform    HackerRank
// Language    java
// Status      Accepted
// Submitted   2026-09-10, 10:38 p.m.
// Technique   regex-based-string-split
// Time        O(N)
// Space       O(N)
// Insight     The implementation uses a regular expression to identify non-alphabetic delimiters, effectively isolating contiguous sequences of English letters as tokens.
// Interview   Before: "I would iterate through the string character by character to build tokens." After: "Using String.split with the regex [^A-Za-z]+ is more concise and runs in O(N) time, though one must handle empty input strings to avoid incorrect token counts."
// Pitfalls    (1) Failing to trim the input string can result in an empty leading token if the string starts with non-alphabetic characters.  (2) Neglecting the empty string case causes the split method to return an array containing one empty string instead of zero tokens.  (3) Using an incorrect regex pattern that fails to account for all non-alphabetic characters defined in the problem constraints.
// ──────────────────────────────────────────────────

import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        if (!scan.hasNextLine()) {
            System.out.println(0);
            scan.close();
            return;
        }
        
        String s = scan.nextLine().trim();
        
        if (s.isEmpty()) {
            System.out.println(0);
            scan.close();
            return;
        }
        
        // Split the string by any non-alphabetic characters
        String[] tokens = s.split("[^A-Za-z]+");
        
        System.out.println(tokens.length);
        for (String token : tokens) {
            System.out.println(token);
        }
        
        scan.close();
    }
}
