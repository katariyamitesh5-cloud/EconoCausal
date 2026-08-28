# EconoCausal API Testing Guide

## Application Startup

Run the project using:

start.bat

Or manually:

uvicorn App.main:app --reload

## API Endpoints

### Dashboard
GET /

### Health Check
GET /health

Expected response:

{
  "status": "healthy"
}

### Analytics
GET /analytics

Returns total customers, average treatment effect, average discount, and recommendation counts.

### Customer Recommendation
GET /recommendation/{customer_id}

Example:
GET /recommendation/10001

## Testing Status

- Dashboard: PASS
- Health API: PASS
- Analytics API: PASS
- Customer Recommendation API: PASS
- Dataset Validation: PASS
