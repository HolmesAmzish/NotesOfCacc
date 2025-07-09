JWT 的优缺点

无需在服务器存放用户数据

JSON 风格

Token 一旦生成后无法修改

无法销毁和提前过期

```java
public class JwtUtilTest {
    public static void main(String[] args) throws JSONException {
        // Define header, encoder algorithm
        JSONObject header = new JSONObject();
        header.put("alg", "HS256");

        // Define payload, user information
        JSONObject payload = new JSONObject();
        payload.put("userName", "Cacciatore");
        payload.put("userId", "20");

        // Encode the data with base64
        String jwtHeader = Base64.getEncoder().encodeToString(header.toString().getBytes());
        String jwtPayload = Base64.getEncoder().encodeToString(payload.toString().getBytes());

        String signingKey = "arorms";
        String sign = DigestUtils.md5DigestAsHex((payload.toString() + signingKey).getBytes());
        String jwt = jwtHeader + "." + jwtPayload + "." + sign;
        System.out.println(jwt);
    }
}
```

