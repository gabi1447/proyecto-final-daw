const categories = document.querySelectorAll(".category-button");
const arrowLeft = document.getElementById("arrowLeft");
const arrowRight = document.getElementById("arrowRight");
const paginationInfo = document.getElementById("pageNumber");
const productsContainer = document.getElementById("pagination");

let currentPageNumber = 1;
const totalPages = 10;

let currentPageSelected = "1";

function createProductCard(productData) {
  return `
        <div class="product-card">
            <img src="${productData.image_url}" id="product-image" alt="${productData.name}">
            <h3>${productData.name}</h3>
            <p>$${productData.price}</p>
            <a href="${productData.item_link}" id="buy-button" target="_blank">Buy</a>
        </div>
    `;
}

function populateProducts(productsData) {
  for (let productData of productsData) {
    productsContainer.innerHTML += createProductCard(productData);
  }
}

function fetchProductData(category_id, page = 1, size = 10) {
  fetch(
    `http://localhost:8080/api/products/${category_id}?page=${page}&size=${size}`,
  )
    .then((response) => response.json())
    .then((data) => populateProducts(data))
    .catch((error) => console.error("Error fetching products:", error));
}

function enable_disable_button(pageNumber) {
  if (pageNumber === 1) {
    arrowLeft.disabled = true;
  } else if (pageNumber === 10) {
    arrowRight.disabled = true;
  } else {
    arrowLeft.disabled = false;
    arrowRight.disabled = false;
  }
}

function updatePaginationInfo() {
  paginationInfo.innerText = `${currentPageNumber} page of ${totalPages}`;
}

function loadEventListeners() {
  for (let category of categories) {
    category.addEventListener("click", () => {
      productsContainer.innerHTML = "";
      currentPageSelected = category.id;
      currentPageNumber = 1;
      fetchProductData(category.id);
      enable_disable_button();
      updatePaginationInfo();
    });
  }
}

function loadPaginationEventListeners() {
  arrowLeft.addEventListener("click", () => {
    if (currentPageNumber === 1) {
      return;
    }
    productsContainer.innerHTML = "";
    currentPageNumber -= currentPageNumber > 1 ? 1 : 0;
    fetchProductData(currentPageSelected, currentPageNumber);
    enable_disable_button();
    updatePaginationInfo();
  });
  arrowRight.addEventListener("click", () => {
    if (currentPageNumber === 10) {
      return;
    }
    productsContainer.innerHTML = "";
    currentPageNumber += currentPageNumber < 10 ? 1 : 0;
    fetchProductData(currentPageSelected, currentPageNumber);
    enable_disable_button();
    updatePaginationInfo();
  });
}

loadEventListeners();
loadPaginationEventListeners();
fetchProductData(currentPageSelected);
updatePaginationInfo();
