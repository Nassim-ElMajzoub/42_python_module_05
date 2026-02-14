#!/usr/bin/env python3


from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        average = sum(data) / len(data)
        return (
            f"Processed {len(data)} numeric values, "
            f"sum={sum(data)}, avg={average:.1f}"
        )

    def validate(self, data: Any) -> bool:
        try:
            sum(data)
            return True
        except TypeError:
            return False


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        chars = len(data)
        words = len(data.split())
        return f"Processed text: {chars} characters, {words} words"

    def validate(self, data: Any) -> bool:
        try:
            data.split()
            return True
        except AttributeError:
            return False


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:

        prefixes = {
            "ERROR": "[ALERT]",
            "INFO": "[INFO]",
            "WARNING": "[WARNING]",
            "DEBUG": "[DEBUG]",
            "CRITICAL": "[CRITICAL]"
        }

        level, message = data.split(": ")
        prefix = prefixes.get(level, "[LOG]")
        return f"{prefix} {level} level detected: {message}"

    def validate(self, data: Any) -> bool:
        try:
            data.split()      # checks it's a string
            return ": " in data  # checks structure
        except AttributeError:
            return False


if __name__ == "__main__":

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    numeric_list = [1, 2, 3, 4, 5]
    text_str = "Hello Nexus World"
    log_str = "ERROR: Connection timeout"

    print("Initializing Numeric Processor...")
    print(f"Processing data: {numeric_list}")
    if numeric.validate(numeric_list):
        print("Validation: Numeric data verified")
        try:
            result = numeric.process(numeric_list)
            print(numeric.format_output(result))
        except ZeroDivisionError:
            print("Cannot process empty list")
    else:
        print("Invalid numeric data")

    print("\nInitializing Text Processor...")
    print(f'Processing data: "{text_str}"')
    if text.validate(text_str):
        print("Validation: Text data verified")
        result = text.process(text_str)
        print(text.format_output(result))
    else:
        print("Invalid text data")

    print("\nInitializing Log Processor...")
    print(f'Processing data: "{log_str}"')
    if log.validate(log_str):
        print("Validation: Log entry verified")
        result = log.process(log_str)
        print(log.format_output(result))
    else:
        print("Invalid log entry")

    print("\n=== Polymorphic Processing Demo ===\n")

    processors = [
        (numeric, [1, 2, 3]),
        (text, "0123456789 a"),
        (log, "INFO: System ready")
    ]

    print("Processing multiple data types through same interface...")

    for i, (processor, data) in enumerate(processors, 1):
        if processor.validate(data):
            print(f"Result {i}: {processor.process(data)}")
        else:
            print(f"Result {i}: Invalid data")

    print("\nFoundation systems online. Nexus ready for advanced streams.")
