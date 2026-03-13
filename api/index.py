# api/index.py
from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        # 示例 NBA 数据（不会超时）
        games_data = {
            "games": [
                {
                    "awayTeam": {"fullName": "Los Angeles Lakers"},
                    "homeTeam": {"fullName": "Denver Nuggets"},
                    "awayScore": 0,
                    "homeScore": 0,
                    "status": "NOT_STARTED"
                }
            ]
        }
        self.wfile.write(json.dumps(games_data).encode('utf-8'))
