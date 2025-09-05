package com.example.decisionast;


public class Token {
public enum Type {
        IDENT, NUMBER,
    AND, OR,
    LPAREN, RPAREN,
    EQ, NEQ, LT, GT, LE, GE,
    PLUS, MINUS, STAR, SLASH,
    TRUE, FALSE,
    EOF
}


public final Type type;
public final String text;


public Token(Type type, String text) {
this.type = type;
this.text = text;
}


public String toString() {
return type + (text != null ? "('" + text + "')" : "");
}
}