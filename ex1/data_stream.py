#!/usr/bin/env python3


from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.total_processed = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type,
            "total_processed": self.total_processed
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        self.total_processed += len(data_batch)
        return (f"Sensor analysis: {len(data_batch)} readings processed"
                f", avg temp: {data_batch[0]}°C")


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:
        self.total_processed += len(data_batch)
        return (f"Transaction analysis: {len(data_batch)} operations"
                f", net flow: {sum(data_batch):+} units")


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:
        self.total_processed += len(data_batch)
        num_errors = sum(1 for event in data_batch if event == "error")
        error_word = "error" if num_errors == 1 else "errors"
        return (f"Event analysis: {len(data_batch)} events"
                f", {num_errors} {error_word} detected")


class StreamProcessor(self, stream: DataStream, data: List[Any]) -> str:
    def process_stream(stream, data):
        pass


if __name__ == "__main__":
    print("")
