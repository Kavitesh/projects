# Spring Boot Exception Handling Guide

This document provides a consolidated view of how to handle exceptions in a Spring Boot application — across **controllers**, **filters**, and **Spring Security components** — while maintaining consistent error responses in **JSON/XML** based on `Accept` headers.

---

## 🔁 Overview of Exception Handling Layers

| Layer           | Can use @ControllerAdvice | Needs manual handling | JSON/XML Negotiation |
| --------------- | ------------------------- | --------------------- | -------------------- |
| Controller      | ✅ Yes                     | ❌                     | ✅ Yes                |
| Global filters  | ❌ No                      | ✅ Yes                 | ✅ Yes (manually)     |
| Spring Security | ❌ No                      | ✅ Yes                 | ✅ Yes (manually)     |

---

## 1️⃣ Controller-Level Exception Handling

Use `@RestControllerAdvice` to catch exceptions thrown by controller methods.

### Example:

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @Autowired
    private ResponseMapper responseMapper;

    @ExceptionHandler(Exception.class)
    public ResponseEntity<CustomError> handleGlobalException(Exception ex) {
        return responseMapper.convertToDTO(ex);
    }
}
```

---

## 2️⃣ Filter Exception Handling

Filters execute **before** controller logic, so exceptions thrown here won't be caught by `@ControllerAdvice`.

### Solution: Manually write the response using `HttpMessageConverter`.

### Filter:

```java
@Component
public class UnifiedExceptionHandlingFilter extends OncePerRequestFilter {

    @Autowired
    private FilterExceptionHelper exceptionHelper;

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response,
                                    FilterChain filterChain) throws ServletException, IOException {
        try {
            filterChain.doFilter(request, response);
        } catch (Exception ex) {
            exceptionHelper.writeErrorResponse(request, response, ex);
        }
    }
}
```

---

### Helper: `FilterExceptionHelper`

```java
@Component
public class FilterExceptionHelper {

    @Autowired
    private ResponseMapper responseMapper;

    @Autowired
    private List<HttpMessageConverter<?>> messageConverters;

    public void writeErrorResponse(HttpServletRequest request, HttpServletResponse response, Exception ex) throws IOException {
        ResponseEntity<CustomError> entity = responseMapper.convertToDTO(ex);
        CustomError body = entity.getBody();

        response.setStatus(entity.getStatusCodeValue());
        MediaType contentType = resolveContentType(request);
        response.setContentType(contentType.toString());

        HttpOutputMessage outputMessage = new ServletServerHttpResponse(response);
        for (HttpMessageConverter<?> converter : messageConverters) {
            if (converter.canWrite(CustomError.class, contentType)) {
                ((HttpMessageConverter<CustomError>) converter).write(body, contentType, outputMessage);
                return;
            }
        }
    }

    private MediaType resolveContentType(HttpServletRequest request) {
        List<MediaType> mediaTypes = MediaType.parseMediaTypes(Optional.ofNullable(request.getHeader("Accept"))
                .orElse(MediaType.APPLICATION_JSON_VALUE));
        MediaType.sortBySpecificityAndQuality(mediaTypes);
        return mediaTypes.stream().filter(mt -> mt.isCompatibleWith(MediaType.APPLICATION_JSON) || mt.isCompatibleWith(MediaType.APPLICATION_XML))
                .findFirst().orElse(MediaType.APPLICATION_JSON);
    }
}
```

---

## 3️⃣ Spring Security Exception Handling

Spring Security uses:

* `AuthenticationEntryPoint` for authentication failures
* `AccessDeniedHandler` for authorization failures

These must **manually write the error response**.

### Example:

```java
@Bean
public AuthenticationEntryPoint authenticationEntryPoint() {
    return (request, response, ex) ->
            filterExceptionHelper.writeErrorResponse(request, response, ex);
}

@Bean
public AccessDeniedHandler accessDeniedHandler() {
    return (request, response, ex) ->
            filterExceptionHelper.writeErrorResponse(request, response, ex);
}
```

---

## 4️⃣ Simulate Controller Error Path from Filter (Advanced)

If you want to reuse `@ExceptionHandler` logic from filters:

### Option: Forward the request to a controller that throws the exception

```java
request.setAttribute("javax.servlet.error.exception", ex);
request.getRequestDispatcher("/error/throw").forward(request, response);
```

### Controller:

```java
@RestController
@RequestMapping("/error")
public class ErrorForwardingController {

    @GetMapping("/throw")
    public void throwFromAttribute(HttpServletRequest request) {
        Exception ex = (Exception) request.getAttribute("javax.servlet.error.exception");
        if (ex != null) throw new RuntimeException(ex);
    }
}
```

But this adds overhead and is not recommended unless you must force it into the Spring MVC pipeline.

---

## 🔁 Shared Components

### `ResponseMapper`

```java
@Component
public class ResponseMapper {

    public ResponseEntity<CustomError> convertToDTO(Exception ex) {
        CustomError error = new CustomError("INTERNAL_ERROR", ex.getMessage());
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(error);
    }
}
```

### `CustomError`

```java
@XmlRootElement(name = "error")
@JsonInclude(JsonInclude.Include.NON_NULL)
public class CustomError {
    private String code;
    private String message;

    // constructors, getters, setters
}
```

---

## 📊 Testing Formats

Test with tools like Postman or `curl`:

```bash
curl -H "Accept: application/json" http://localhost:8080/your/api
curl -H "Accept: application/xml" http://localhost:8080/your/api
```

---

## ✅ Summary

| Use Case                  | Recommendation                                 |
| ------------------------- | ---------------------------------------------- |
| Controller errors         | Use `@RestControllerAdvice` + `ResponseMapper` |
| Filter/security errors    | Use `FilterExceptionHelper` + `ResponseMapper` |
| Need central catch-all    | Add `UnifiedExceptionHandlingFilter` at top    |
| Format-specific responses | Use `HttpMessageConverter` based on `Accept`   |

---

## 📋 Appendix

### Registering the Unified Filter First

```java
@Configuration
public class FilterConfig {
    @Bean
    public FilterRegistrationBean<UnifiedExceptionHandlingFilter> errorHandlingFilter(UnifiedExceptionHandlingFilter filter) {
        FilterRegistrationBean<UnifiedExceptionHandlingFilter> registration = new FilterRegistrationBean<>();
        registration.setFilter(filter);
        registration.setOrder(Ordered.HIGHEST_PRECEDENCE);
        return registration;
    }
}
```

---
