const categories = document.querySelectorAll(".category-button");
const arrowLeft = document.getElementById("arrowLeft");
const arrowRight = document.getElementById("arrowRight");
const paginationInfo = document.getElementById("pageNumber");

let currentPageNumber = 1;
const totalPages = 10;

let currentPageSelected = "1";

function fetchProductData(category_id, page = 1, size = 10) {
  fetch(
    `http://localhost:8080/api/products/${category_id}?page=${page}&size=${size}`,
  )
    .then((response) => response.json())
    .then((data) => console.log(data))
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
      fetchProductData(category.id);
      loadPaginationEventListeners(category.id);
      enable_disable_button();
      updatePaginationInfo();
    });
  }
}

function loadPaginationEventListeners(category_id) {
  arrowLeft.addEventListener("click", () => {
    if (currentPageNumber === 1) {
      return;
    }
    currentPageNumber -= currentPageNumber > 1 ? 1 : 0;
    fetchProductData(category_id, currentPageNumber);
    enable_disable_button();
    updatePaginationInfo();
  });
  arrowRight.addEventListener("click", () => {
    if (currentPageNumber === 10) {
      return;
    }
    currentPageNumber += currentPageNumber < 10 ? 1 : 0;
    fetchProductData(category_id, currentPageNumber);
    enable_disable_button();
    updatePaginationInfo();
  });
}

loadEventListeners();
