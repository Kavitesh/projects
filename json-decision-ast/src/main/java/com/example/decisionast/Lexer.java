package com.example.decisionast;

import java.util.ArrayList;
import java.util.List;

public class Lexer {
    private final String input;
    private int pos = 0;

    public Lexer(String input) {
        this.input = input;
    }

    private char peek() {
        if (pos >= input.length())
            return '\0';
        return input.charAt(pos);
    }

    private char next() {
        if (pos >= input.length())
            return '\0';
        return input.charAt(pos++);
    }

    private void skipWhitespace() {
        while (Character.isWhitespace(peek()))
            next();
    }

    public List<Token> tokenize() {
        List<Token> tokens = new ArrayList<>();
        while (true) {
            skipWhitespace();
            char c = peek();
            if (c == '\0') {
                tokens.add(new Token(Token.Type.EOF, null));
                break;
            }

            // identifiers and keywords
            if (Character.isLetter(c)) {
                StringBuilder sb = new StringBuilder();
                while (Character.isLetterOrDigit(peek()) || peek() == '_') {
                    sb.append(next());
                }
                String word = sb.toString();
                switch (word) {
                    case "and":
                        tokens.add(new Token(Token.Type.AND, "and"));
                        break;
                    case "or":
                        tokens.add(new Token(Token.Type.OR, "or"));
                        break;
                    case "true":
                        tokens.add(new Token(Token.Type.TRUE, "true"));
                        break;
                    case "false":
                        tokens.add(new Token(Token.Type.FALSE, "false"));
                        break;
                    default:
                        tokens.add(new Token(Token.Type.IDENT, word));
                        break;
                }
                continue;
            }

            // numbers (integers only)
            if (Character.isDigit(c)) {
                StringBuilder sb = new StringBuilder();
                while (Character.isDigit(peek()))
                    sb.append(next());
                tokens.add(new Token(Token.Type.NUMBER, sb.toString()));
                continue;
            }

            // operators and punctuation
            if (c == '&') {
                next();
                if (peek() == '&') {
                    next();
                    tokens.add(new Token(Token.Type.AND, "&&"));
                    continue;
                }
                throw new RuntimeException("Unexpected character: & (did you mean &&?)");
            }
            if (c == '|') {
                next();
                if (peek() == '|') {
                    next();
                    tokens.add(new Token(Token.Type.OR, "||"));
                    continue;
                }
                throw new RuntimeException("Unexpected character: | (did you mean ||?)");
            }
            if (c == '(') {
                next();
                tokens.add(new Token(Token.Type.LPAREN, "("));
                continue;
            }
            if (c == ')') {
                next();
                tokens.add(new Token(Token.Type.RPAREN, ")"));
                continue;
            }

            if (c == '=') {
                next();
                if (peek() == '=') {
                    next();
                    tokens.add(new Token(Token.Type.EQ, "=="));
                    continue;
                }
                throw new RuntimeException("Single '=' not supported, use '==' for comparison");
            }
            if (c == '!') {
                next();
                if (peek() == '=') {
                    next();
                    tokens.add(new Token(Token.Type.NEQ, "!="));
                    continue;
                }
                throw new RuntimeException("Only '!=' supported after '!'");
            }
            if (c == '<') {
                next();
                if (peek() == '=') {
                    next();
                    tokens.add(new Token(Token.Type.LE, "<="));
                    continue;
                }
                tokens.add(new Token(Token.Type.LT, "<"));
                continue;
            }
            if (c == '>') {
                next();
                if (peek() == '=') {
                    next();
                    tokens.add(new Token(Token.Type.GE, ">="));
                    continue;
                }
                tokens.add(new Token(Token.Type.GT, ">"));
                continue;
            }
            if (c == '+') {
                next();
                tokens.add(new Token(Token.Type.PLUS, "+"));
                continue;
            }
            if (c == '-') {
                next();
                tokens.add(new Token(Token.Type.MINUS, "-"));
                continue;
            }
            if (c == '*') {
                next();
                tokens.add(new Token(Token.Type.STAR, "*"));
                continue;
            }
            if (c == '/') {
                next();
                tokens.add(new Token(Token.Type.SLASH, "/"));
                continue;
            }

            throw new RuntimeException("Unexpected character: '" + c + "'");
        }
        return tokens;
    }
}
