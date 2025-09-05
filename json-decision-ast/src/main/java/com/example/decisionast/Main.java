package com.example.decisionast;

import com.example.decisionast.ast.Expr;
import com.example.decisionast.visitor.Evaluator;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Example variable context
        Map<String, Object> ctx = new HashMap<>();
        ctx.put("x", 10);
        ctx.put("y", 20);
        ctx.put("flag", true);

        // Example expressions
        String[] tests = {
            "x < y && flag",
            "x > y || flag !=true",
            "x == 10 && (y == 20 || flag == false)",
            "flag && (x + 5 > y)" 
        };

        for (String exprText : tests) {
            try {
                Lexer lexer = new Lexer(exprText);
                List<Token> tokens = lexer.tokenize();

                Parser parser = new Parser(tokens);
                Expr expr = parser.parse();

                Evaluator evaluator = new Evaluator(ctx);
                Object result = expr.accept(evaluator);

                System.out.println(exprText + " => " + result);
            } catch (Exception e) {
                System.err.println("Error evaluating '" + exprText + "': " + e.getMessage());
            }
        }
    }
}
