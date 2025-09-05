package com.example.decisionast.visitor;

import com.example.decisionast.ast.BinaryExpr;
import com.example.decisionast.ast.LiteralExpr;
import com.example.decisionast.ast.VariableExpr;

public interface ExprVisitor<R> {
    R visitBinary(BinaryExpr b);
    R visitLiteral(LiteralExpr l);
    R visitVariable(VariableExpr v);
}