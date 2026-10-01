-- 02: Creación de tabla empleados
CREATE TABLE empleados (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);
