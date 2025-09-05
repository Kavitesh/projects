package com.example.decisionast.ast;

import com.example.decisionast.visitor.ExprVisitor;

public class VariableExpr implements Expr {
    public final String name;

    public VariableExpr(String name) { this.name = name; }

    @Override
    public <R> R accept(ExprVisitor<R> visitor) {
        return visitor.visitVariable(this);
    }

    @Override
    public String toString() { return name; }
}