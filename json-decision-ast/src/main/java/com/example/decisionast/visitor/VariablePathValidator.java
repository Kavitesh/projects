package com.example.decisionast.visitor;

import com.example.decisionast.ast.*;
import com.example.decisionast.sementic.ExpressionMeta;
import com.example.decisionast.sementic.SchemaValidator;

import java.util.ArrayList;
import java.util.List;

public class VariablePathValidator implements ExprVisitor<Void> {

    private final ExpressionMeta schema;
    private final SchemaValidator validator;
    private final List<String> errors = new ArrayList<>();

    public VariablePathValidator(ExpressionMeta schema) {
        this.schema = schema;
        this.validator = new SchemaValidator();
    }

    public List<String> getErrors() {
        return errors;
    }

    @Override
    public Void visitBinary(BinaryExpr b) {
        b.left.accept(this);
        b.right.accept(this);
        return null;
    }

    @Override
    public Void visitLiteral(LiteralExpr l) {
        // literals are always valid
        return null;
    }

    @Override
    public Void visitVariable(VariableExpr v) {
        if (!validator.validate(v.name, schema)) {
            errors.add("Invalid variable path: " + v.name);
        }
        return null;
    }
}
