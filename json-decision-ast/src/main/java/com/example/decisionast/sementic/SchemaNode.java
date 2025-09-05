package com.example.decisionast.sementic;

import java.util.List;
import java.util.Map;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@JsonIgnoreProperties(ignoreUnknown = true)
public class SchemaNode {

    private NodeType type;

    private List<String> xAllowedOperations;

    private SchemaNode items;

    private Map<String, SchemaNode> properties;

    private List<String> enumValues;
}
