package com.example.decisionast;

import com.example.decisionast.ast.*;
import static com.example.decisionast.ast.BinaryExpr.Op;

import java.util.List;

public class Parser {
    private final List<Token> tokens;
    private int pos = 0;

    public Parser(List<Token> tokens) {
        this.tokens = tokens;
    }

    private Token peek() {
        if (pos >= tokens.size()) return new Token(Token.Type.EOF, null);
        return tokens.get(pos);
    }

    private Token next() {
        return tokens.get(pos++);
    }

    private boolean match(Token.Type type) {
        if (peek().type == type) {
            next();
            return true;
        }
        return false;
    }

    public Expr parse() {
        Expr expr = parseOr();
        if (peek().type != Token.Type.EOF) {
            throw new RuntimeException("Unexpected token: " + peek());
        }
        return expr;
    }

    // or -> and ('||' and)*
    private Expr parseOr() {
        Expr expr = parseAnd();
        while (match(Token.Type.OR)) {
            Expr right = parseAnd();
            expr = new BinaryExpr(expr, right, Op.OR);
        }
        return expr;
    }

    // and -> equality ('&&' equality)*
    private Expr parseAnd() {
        Expr expr = parseEquality();
        while (match(Token.Type.AND)) {
            Expr right = parseEquality();
            expr = new BinaryExpr(expr, right, Op.AND);
        }
        return expr;
    }

    // equality -> comparison (('==' | '!=') comparison)*
    private Expr parseEquality() {
        Expr expr = parseComparison();
        while (true) {
            if (match(Token.Type.EQ)) {
                Expr right = parseComparison();
                expr = new BinaryExpr(expr, right, Op.EQ);
            } else if (match(Token.Type.NEQ)) {
                Expr right = parseComparison();
                expr = new BinaryExpr(expr, right, Op.NEQ);
            } else {
                break;
            }
        }
        return expr;
    }

    // comparison -> term (('<' | '<=' | '>' | '>=') term)*
    private Expr parseComparison() {
        Expr expr = parseTerm();
        while (true) {
            if (match(Token.Type.LT)) {
                Expr right = parseTerm();
                expr = new BinaryExpr(expr, right, Op.LT);
            } else if (match(Token.Type.LE)) {
                Expr right = parseTerm();
                expr = new BinaryExpr(expr, right, Op.LE);
            } else if (match(Token.Type.GT)) {
                Expr right = parseTerm();
                expr = new BinaryExpr(expr, right, Op.GT);
            } else if (match(Token.Type.GE)) {
                Expr right = parseTerm();
                expr = new BinaryExpr(expr, right, Op.GE);
            } else {
                break;
            }
        }
        return expr;
    }

    // term -> factor (('+' | '-') factor)*
    private Expr parseTerm() {
        Expr expr = parseFactor();
        while (true) {
            if (match(Token.Type.PLUS)) {
                Expr right = parseFactor();
                expr = new BinaryExpr(expr, right, Op.PLUS);
            } else if (match(Token.Type.MINUS)) {
                Expr right = parseFactor();
                expr = new BinaryExpr(expr, right, Op.MINUS);
            } else {
                break;
            }
        }
        return expr;
    }

    // factor -> primary (('*' | '/') primary)*
    private Expr parseFactor() {
        Expr expr = parsePrimary();
        while (true) {
            if (match(Token.Type.STAR)) {
                Expr right = parsePrimary();
                expr = new BinaryExpr(expr, right, Op.STAR);
            } else if (match(Token.Type.SLASH)) {
                Expr right = parsePrimary();
                expr = new BinaryExpr(expr, right, Op.SLASH);
            } else {
                break;
            }
        }
        return expr;
    }

    // primary -> NUMBER | true | false | IDENT | '(' expr ')'
    private Expr parsePrimary() {
        Token token = peek();
        switch (token.type) {
            case NUMBER:
                next();
                return new LiteralExpr(Integer.parseInt(token.text));
            case TRUE:
                next();
                return new LiteralExpr(true);
            case FALSE:
                next();
                return new LiteralExpr(false);
            case IDENT:
                next();
                return new VariableExpr(token.text);
            case LPAREN:
                next();
                Expr expr = parseOr();
                if (!match(Token.Type.RPAREN)) {
                    throw new RuntimeException("Expected ')', found: " + peek());
                }
                return expr;
            default:
                throw new RuntimeException("Unexpected token: " + token);
        }
    }
}
