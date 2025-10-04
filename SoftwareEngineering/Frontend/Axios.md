# Axios

## Introduction

Axios is a popular JavaScript library used to make HTTP requests from both the browser and Node.js.

### Installing

```bash
npm install axios
```



## Example

Performing a `GET` request

```js
const axios = require('axios');

// Make a request fro a user with a given ID
axios.get('/user?id=123')
	.then(function(response) {
    	console.log(response);
	})
	.catch(function(error) {
    	console.log(error);
	})
	.finally(function() {
    	// always executed
	})
```



## Axios API

Requests can be made by passing the relevant config to `axios`.

axios(config)

```js
// Send a POST request
axios({
    method: 'post',
    url: 'user/123',
    data: {
        firstName: 'Fred',
        lastName: 'Flintstone'
    }
});
```

```js
// GET request for remote image in node.js
axios({
    method: 'get',
    url: 'http://bit.ly/2mTM3nY',
    responseType: 'stream'
})
	.then(function (response) {
    	response.data.pipe(fs.createWriteStream('ada_lovelace.jpg'))
	});
```

axios(url[, config])

```js
// Send a GET request (default method)
axios('/usr/123');
```



## Response Schema

The response for a request contains the following information

```js
{
  // `data` is the response that was provided by the server
  data: {},

  // `status` is the HTTP status code from the server response
  status: 200,

  // `statusText` is the HTTP status message from the server response
  // As of HTTP/2 status text is blank or unsupported.
  // (HTTP/2 RFC: https://www.rfc-editor.org/rfc/rfc7540#section-8.1.2.4)
  statusText: 'OK',

  // `headers` the HTTP headers that the server responded with
  // All header names are lower cased and can be accessed using the bracket notation.
  // Example: `response.headers['content-type']`
  headers: {},

  // `config` is the config that was provided to `axios` for the request
  config: {},

  // `request` is the request that generated this response
  // It is the last ClientRequest instance in node.js (in redirects)
  // and an XMLHttpRequest instance in the browser
  request: {}
}
```

