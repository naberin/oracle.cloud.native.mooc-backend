package io.mooc.depth.controllers;

import java.util.HashMap;
import java.util.Map;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/health")
public class HealthController {

    @GetMapping
    public ResponseEntity<?> getHealth() {
        Map<String, Object> response = new HashMap<String, Object>();
        response.put("status", "UP");
        return ResponseEntity.ok(response);
    }
}
