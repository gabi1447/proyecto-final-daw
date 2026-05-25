-- Crear la tabla Category primero, ya que Product depende de ella
CREATE TABLE Category (
id_category INT NOT NULL,
name VARCHAR(255) NOT NULL,
vat INT,
description VARCHAR(255),
PRIMARY KEY (id_category)
);

-- Crear la tabla Product
CREATE TABLE Product (
id_product INT NOT NULL,
name VARCHAR(255) NOT NULL,
price NUMERIC(10, 2) NOT NULL,
description VARCHAR(255),
id_category INT,
PRIMARY KEY (id_product),
FOREIGN KEY (id_category) REFERENCES Category(id_category)
);

-- Crear la tabla User
CREATE TABLE "User" (
id_user INT NOT NULL,
name VARCHAR(255) NOT NULL,
email TEXT NOT NULL UNIQUE,
hash VARCHAR(255) NOT NULL,
PRIMARY KEY (id_user)
);

-- Crear la tabla intermedia Cart (Relación muchos a muchos)
CREATE TABLE Cart (
id_product INT NOT NULL,
id_user INT NOT NULL,
PRIMARY KEY (id_product, id_user),
FOREIGN KEY (id_product) REFERENCES Product(id_product) ON DELETE CASCADE,
FOREIGN KEY (id_user) REFERENCES "User"(id_user) ON DELETE CASCADE
);
