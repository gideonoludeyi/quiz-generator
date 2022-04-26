class UnsupportedFileExtension(Exception):
    def __init__(self, extension: str, *args: object) -> None:
        super().__init__(extension, *args)
        self.extension = extension
