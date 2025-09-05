package com.example.decisionast.ast;

import com.example.decisionast.visitor.ExprVisitor;

public class BinaryExpr implements Expr {
    public enum Op {
    AND, OR,
    EQ, NEQ,
    LT, LE, GT, GE,
    PLUS, MINUS, STAR, SLASH
    }

    public final Op op;
    public final Expr left;
    public final Expr right;

    public BinaryExpr(Expr left, Expr right,Op op) {
        this.op = op;
        this.left = left;
        this.right = right;
    }

    @Override
    public <R> R accept(ExprVisitor<R> visitor) {
        return visitor.visitBinary(this);
    }

    @Override
    public String toString() {
        return "(" + left + " " + op + " " + right + ")";
    }
}