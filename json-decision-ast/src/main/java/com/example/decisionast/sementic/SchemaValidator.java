package com.example.decisionast.sementic;

import java.util.List;
import java.util.Map;

public class SchemaValidator implements SchemaValidatorVisitor {

    @Override
    public boolean validate(String path, ExpressionMeta meta) {
        if (meta == null || meta.getSchema() == null) return false;
        return validatePath(path.split("\\."), 0, meta.getSchema());
    }

    private boolean validatePath(String[] parts, int index, SchemaNode node) {
        if (node == null) return false;
        if (index >= parts.length) return true; // reached end of path successfully

        String part = parts[index];

        switch (node.getType()) {
            case OBJECT:
                if (node.getProperties() == null) return false;
                SchemaNode child = node.getProperties().get(part);
                if (child == null) return false;
                return validatePath(parts, index + 1, child);

            case ARRAY:
                try {
                    int idx = Integer.parseInt(part); // array index
                    return node.getItems() != null && validatePath(parts, index + 1, node.getItems());
                } catch (NumberFormatException e) {
                    return false; // path element is not an integer
                }

            case PRIMITIVE:
                // leaf node must be the last in path
                return index == parts.length - 1;

            default:
                return false;
        }
    }
}
