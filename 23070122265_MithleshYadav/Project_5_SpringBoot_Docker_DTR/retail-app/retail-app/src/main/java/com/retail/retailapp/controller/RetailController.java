package com.retail.retailapp.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/api")
public class RetailController {

    private final List<Product> products = List.of(
            new Product(1, "Laptop", 65000),
            new Product(2, "Smartphone", 35000),
            new Product(3, "Headphones", 2500),
            new Product(4, "Smart Watch", 5000)
    );

    @GetMapping("/health")
    public String health() {
        return "Retail application is healthy";
    }

    @GetMapping("/products")
    public List<Product> getProducts() {
        return products;
    }

    @GetMapping("/products/{id}")
    public Product getProduct(@PathVariable int id) {
        return products.stream()
                .filter(product -> product.id() == id)
                .findFirst()
                .orElse(null);
    }

    public record Product(int id, String name, double price) {
    }
}