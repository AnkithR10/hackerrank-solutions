// ──────────────────────────────────────────────────
// Link        https://www.hackerrank.com/challenges/java-currency-formatter/problem?isFullScreen=true
// Problem     Java Currency Formatter
// Difficulty  Easy
// Subdomain   Introduction
// Platform    HackerRank
// Language    java
// Status      Accepted
// Submitted   2026-09-10, 10:36 p.m.
// Technique   locale-based-number-formatting
// Time        O(1)
// Space       O(1)
// Insight     The solution utilizes the Java NumberFormat class to apply locale-specific currency formatting rules to a double-precision input.
// Interview   Before: "How would you format a currency value for different countries?" After: "I would use NumberFormat.getCurrencyInstance with the appropriate Locale. For India, I construct a custom Locale using 'en' and 'IN' because it lacks a built-in constant. This approach runs in O(1) time and space."
// Pitfalls    (1) Failing to construct the custom India locale with the correct language 'en' and country 'IN' as specified in the problem requirements.  (2) Assuming all required locales are available as static constants in the Locale class, ignoring the need for custom instantiation.
// ──────────────────────────────────────────────────

import java.io.*;
import java.util.*;
import java.text.*;

public class Solution {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();
        
        // Create NumberFormats for different locales
        NumberFormat us = NumberFormat.getCurrencyInstance(Locale.US);
        
        // India does not have a built-in Locale, so we create a custom one with language "en" and country "IN"
        Locale indiaLocale = new Locale("en", "IN");
        NumberFormat india = NumberFormat.getCurrencyInstance(indiaLocale);
        
        NumberFormat china = NumberFormat.getCurrencyInstance(Locale.CHINA);
        NumberFormat france = NumberFormat.getCurrencyInstance(Locale.FRANCE);
        
        System.out.println("US: " + us.format(payment));
        System.out.println("India: " + india.format(payment));
        System.out.println("China: " + china.format(payment));
        System.out.println("France: " + france.format(payment));
    }
}
