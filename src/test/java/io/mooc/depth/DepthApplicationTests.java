package io.mooc.depth;

import io.mooc.depth.controllers.HealthController;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertNotNull;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;


@SpringBootTest
class DepthApplicationTests {

    @Autowired
    private HealthController healthController;

    @Test
    void contextLoads(){
        assertNotNull(healthController);
    }

}
