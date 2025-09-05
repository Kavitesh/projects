package com.example.decisionast.ast;

import com.example.decisionast.visitor.ExprVisitor;

public interface Expr {
    <R> R accept(ExprVisitor<R> visitor);
}
