### Base URL:
http://35.236.248.79:5000

### How to Call API with Authorization

You must include this header in your request or you won't have permission to call the API:

Authorization: Bearer supersecrettoken123

### Endpoint

GET /api/time?city=<CapitalCity>

Replace <CapitalCity> with the name of a capital. For example if you want the time in Korea, write:

http://35.236.248.79:5000/api/time?city=Seoul

### Curl Command to Retrieve Timezone (ex. of Korea timezone)

curl -H "Authorization: Bearer supersecrettoken123" "http://35.236.248.79:5000/api/time?city=Seoul"

### Successful Response Example

{
  "city": "Seoul",
  "current_time": "2025-04-21 23:59:00",
  "utc_offset": "UTC+09:00"
}

### Supported Cities

Washington
Austin
Denver
Sacramento
Juneau
Honolulu
London
Paris
Tokyo
Canberra
Seoul
New Delhi
Brasilia

Add more by editing the TIMEZONES dictionary in app.py
