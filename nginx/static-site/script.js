console.log("js is running!!");

/* fetch("http://localhost:8080/api/products")
  .then((response) => response.json())
  .then((data) => console.log(data)); */

fetch("http://localhost:8080/api/products/1?page=1&size=10")
  .then((response) => response.json())
  .then((data) => console.log(data));
