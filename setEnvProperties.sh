#Properties for postgresqls
export DB_DRIVER=org.postgresql.Driver
export DB_USERNAME=budgetuser
export DB_PASSWORD=""
export DB_URL=jdbc:postgresql://localhost:5432/budget4
export DB_DIALECT=io.budgetapp.hibernate.dialect.CustomPostgreSQLDialect
export DB_VALIDATE_QUERY="SELECT 1"