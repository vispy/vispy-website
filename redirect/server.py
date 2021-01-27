"""
A very simple server to redirect all incoming requests to https://vispy.org.
A Dockerfile is included to deploy on a MyPaas VM.
"""

import os
import json
import socket

import asgineer


service_name = os.getenv("MYPAAS_SERVICE", "")
stats_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def send_stats(request):
    """Send request stats over UPD to the stats service."""
    if not service_name:
        return
    stats = {
        "group": service_name,
        "redirects|count": 1,
        "path|cat": request.path,
        "pageview": request.headers,
    }
    # The pageview field is to count unique visitor, language, etc.
    # Note that the header data is anonymized.
    stats_socket.sendto(json.dumps(stats).encode(), ("stats", 8125))


@asgineer.to_asgi
async def main_handler(request):
    send_stats(request)
    # 307 is temporatry redirect, 308 is permanent redirect
    return 307, {"Location": "https://vispy.org"}, b""


if __name__ == "__main__":
    asgineer.run(main_handler, "uvicorn", "0.0.0.0:80", log_level="warning")
