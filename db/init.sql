CREATE TABLE category (
    id BIGSERIAL PRIMARY KEY,
    category_name TEXT NOT NULL UNIQUE
);

CREATE TABLE products (
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price NUMERIC(10,2) NOT NULL,
    currency VARCHAR(3) NOT NULL,
    image_url TEXT NOT NULL,
    item_link TEXT NOT NULL UNIQUE,
    category_id BIGINT NOT NULL
        REFERENCES category(id)
	ON DELETE CASCADE
);

INSERT INTO category (category_name)
VALUES
    ('Gameboy'),
    ('Xbox 360'),
    ('Playstation 2');

/* INSERT INTO products (name, price, currency, image_url, item_link, category_id)
VALUES ('gameboy advanced', 100.50, 'EUR', 'image_url', 'item_link', 1); */
