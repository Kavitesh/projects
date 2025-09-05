package com.example.decisionast.visitor;

import com.example.decisionast.ast.BinaryExpr;
import com.example.decisionast.ast.LiteralExpr;
import com.example.decisionast.ast.VariableExpr;

import java.util.Map;


public class Evaluator implements ExprVisitor<Object> {
    private final Map<String, Object> ctx;

    public Evaluator(Map<String, Object> ctx) {
        this.ctx = ctx;
    }

    @Override
    public Object visitBinary(BinaryExpr b) {
        Object left = b.left.accept(this);
        Object right = b.right.accept(this);

        switch (b.op) {
        case AND: {
            if (!(left instanceof Boolean)) throw new RuntimeException("Left of && must be boolean");
            if (!((Boolean) left)) return false; // short-circuit
            if (!(right instanceof Boolean)) throw new RuntimeException("Right of && must be boolean");
            return (Boolean) right;
        }

        case OR: {
            if (!(left instanceof Boolean)) throw new RuntimeException("Left of || must be boolean");
            if ((Boolean) left) return true; // short-circuit
            if (!(right instanceof Boolean)) throw new RuntimeException("Right of || must be boolean");
            return (Boolean) right;
        }

            case EQ:
                return left.equals(right);

            case NEQ:
                return !left.equals(right);

            case LT:
                return checkInteger(left, right) && (Integer) left < (Integer) right;

            case LE:
                return checkInteger(left, right) && (Integer) left <= (Integer) right;

            case GT:
                return checkInteger(left, right) && (Integer) left > (Integer) right;

            case GE:
                return checkInteger(left, right) && (Integer) left >= (Integer) right;

            case PLUS:
                return checkInteger(left, right) ? (Integer) left + (Integer) right : throwType(left, right, "+");

            case MINUS:
                return checkInteger(left, right) ? (Integer) left - (Integer) right : throwType(left, right, "-");

            case STAR:
                return checkInteger(left, right) ? (Integer) left * (Integer) right : throwType(left, right, "*");

            case SLASH:
                if (!checkInteger(left, right)) throwType(left, right, "/");
                if ((Integer) right == 0) throw new RuntimeException("Division by zero");
                return (Integer) left / (Integer) right;

            default:
                throw new RuntimeException("Unsupported operator: " + b.op);
        }
    }

    @Override
    public Object visitLiteral(LiteralExpr l) {
        return l.value;
    }

    @Override
    public Object visitVariable(VariableExpr v) {
        if (!ctx.containsKey(v.name)) {
            throw new RuntimeException("Undefined variable: " + v.name);
        }
        return ctx.get(v.name);
    }

    private boolean checkInteger(Object left, Object right) {
        return left instanceof Integer && right instanceof Integer;
    }

    private Object throwType(Object left, Object right, String op) {
        throw new RuntimeException("Operands of '" + op + "' must be integers: left=" + left + ", right=" + right);
    }
}
