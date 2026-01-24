#!/bin/bash

# PostgreSQL Database Setup Script for AOM-Agent

echo "Setting up PostgreSQL database for AOM-Agent..."

# Check if PostgreSQL is running
if ! pg_isready -h 127.0.0.1 -p 5432; then
    echo "❌ PostgreSQL is not running. Please start PostgreSQL first."
    exit 1
fi

# Create database and user
psql -U postgres -h 127.0.0.1 << EOF
-- Create user if not exists
DO \$\$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_catalog.pg_user WHERE usename = 'aom_user') THEN
        CREATE USER aom_user WITH PASSWORD '123456';
    END IF;
END
\$\$;

-- Drop database if exists (optional, comment out if you want to keep existing data)
-- DROP DATABASE IF EXISTS aom_agent_db;

-- Create database if not exists
SELECT 'CREATE DATABASE aom_agent_db OWNER aom_user'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'aom_agent_db')\gexec

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE aom_agent_db TO aom_user;

\c aom_agent_db

-- Grant schema privileges
GRANT ALL ON SCHEMA public TO aom_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO aom_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO aom_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO aom_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO aom_user;

EOF

echo "✅ Database setup complete!"
echo "Database: aom_agent_db"
echo "User: aom_user"
echo "Host: 127.0.0.1:5432"