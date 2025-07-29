# CCM Database Application

## Overview
Application to connect to CCM database and manage bamboo patterns and map data.

## Database Configuration
- **Host**: 172.17.200.183
- **Port**: 3306
- **Username**: campeche
- **Password**: cam@2025!
- **Database**: CCM

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python main.py
   ```

## Architecture
- **Domain-Driven Design (DDD)** structure
- Clean separation of concerns
- Repository pattern for data access
- Service layer for business logic

## Project Structure
```
app/
├── main.py                     # Application entry point
├── config/                     # Configuration files
├── domain/                     # Domain layer
│   ├── entities/              # Domain entities
│   ├── repositories/          # Repository interfaces
│   └── services/              # Domain services
└── infrastructure/            # Infrastructure layer
    ├── database.py            # Database connection
    └── repositories/          # Repository implementations
```
