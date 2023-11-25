"""Data models for location"""
from pydantic import BaseModel

class Location(BaseModel):
    latitude: float
    longitude: float
    confidence: float
# Modified 2025-10-08
# Modified 2023-11-25
