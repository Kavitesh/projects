package com.example.decisionast.ast;

import com.example.decisionast.visitor.ExprVisitor;

public class LiteralExpr implements Expr {
    public final Object value; // Integer or Boolean

    public LiteralExpr(Object value) {
        this.value = value;
    }

    @Override
    public <R> R accept(ExprVisitor<R> visitor) {
        return visitor.visitLiteral(this);
    }

    @Override
    public String toString() {
        return String.valueOf(value);
    }
}