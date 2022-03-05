#!/usr/bin/python3


from models.base_model import BaseModel
"""Module that contain class amenity
    inherit from base.
"""


class Amenity(BaseModel):
    """
    class that defines Amenity.
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
            Sends arguments to the parent class and create a new instance
        """
        super().__init__(*args, **kwargs)
