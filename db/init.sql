CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(100),
    email VARCHAR(255) UNIQUE
);

INSERT INTO employees (name, department, email)
VALUES
('John Doe', 'Engineering', 'john@example.com'),
('Jane Smith', 'Finance', 'jane@example.com'),
('Mary Johnson', 'HR', 'mary@example.com');
