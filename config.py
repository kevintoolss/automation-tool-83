from typing import Dict, Any

class Config:
    """
    A class to hold configuration settings.
    """

    def __init__(self, **kwargs: Any) -> None:
        """
        Initializes the configuration with keyword arguments.
        
        Args:
            **kwargs: Arbitrary keyword arguments representing configuration options.
        """
        self.settings: Dict[str, Any] = kwargs

    def get(self, key: str, default: Any = None) -> Any:
        """
        Retrieves the value for a given key from the configuration.
        
        Args:
            key (str): The key of the setting to retrieve.
            default (Any): The default value to return if the key does not exist.
        
        Returns:
            Any: The value associated with the key, or the default value if the key is not found.
        """
        return self.settings.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """
        Sets the value for a given key in the configuration.
        
        Args:
            key (str): The key of the setting to set.
            value (Any): The value to associate with the key.
        """
        self.settings[key] = value

    def __repr__(self) -> str:
        """
        Returns a string representation of the configuration settings.
        """
        return f"Config(settings={self.settings})"