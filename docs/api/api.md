## 📦 API Overview

Base path: `/livestreams`

| Method | Endpoint                          | Description                          |
|--------|-----------------------------------|--------------------------------------|
| GET    | `/livestreams`                   | List all livestreams (filter by status) |
| POST   | `/livestreams`                   | Create a new livestream session      |
| PATCH  | `/livestreams/{id}/start`        | Mark livestream as started           |
| PATCH  | `/livestreams/{id}/stop`         | End a livestream                     |
| PATCH  | `/livestreams/{id}/products`     | Attach products to livestream        |
| GET    | `/livestreams/{id}`              | Get livestream metadata              |
