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
            "data_type": self.data_type,
            "total_processed": self.total_processed
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Environmental Data"
        self.data_type = "Sensor data"

    def process_batch(self, data_batch: List[Any]) -> str:
        self.total_processed += len(data_batch)
        return (f"Sensor analysis: {len(data_batch)} readings processed"
                f", avg temp: {data_batch[0]}°C")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "high":
            return [data for data in data_batch if data > 50]
        return data_batch


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Financial Data"
        self.data_type = "Transaction data"

    def process_batch(self, data_batch: List[Any]) -> str:
        self.total_processed += len(data_batch)
        return (f"Transaction analysis: {len(data_batch)} operations"
                f", net flow: {sum(data_batch):+} units")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "large":
            return [data for data in data_batch if data > 100 or data < -100]
        return data_batch


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "System Events"
        self.data_type = "Event data"

    def process_batch(self, data_batch: List[Any]) -> str:
        self.total_processed += len(data_batch)
        num_errors = sum(1 for event in data_batch if event == "error")
        error_word = "error" if num_errors == 1 else "errors"
        return (f"Event analysis: {len(data_batch)} events"
                f", {num_errors} {error_word} detected")


class StreamProcessor:
    def process_stream(self, stream: DataStream, data: List[Any]) -> str:
        return stream.process_batch(data)
    
    def stream_stats(self, stream: DataStream, data: List[Any]) -> str:
        stats = stream.get_stats(data)
        return


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    processor = StreamProcessor()

    print("Initializing Sensor Stream...")
    batch = [22.5, 65, 1013]
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: {sensor.stream_type}")
    print(f"Processing sensor batch: [temp:{batch[0]}, humidity:{batch[1]}, "
          f"pressure:{batch[2]}]")
    print(processor.process_stream(sensor, batch))

    print("\nInitializing Transaction Stream...")
    batch = [100, -150, 75]
    transaction = TransactionStream("TRANS_001")
    print(
        f"Stream ID: {transaction.stream_id}, "
        f"Type: {transaction.stream_type}"
    )
    transactions = []
    for trans in batch:
        if trans > 0:
            transactions.append(f"buy:{str(trans)}")
        elif trans < 0:
            transactions.append(f"sell:{str(-trans)}")
        else:
            transactions.append("0")
    print("Processing transaction batch: [" + ", ".join(transactions) + "]")
    print(processor.process_stream(transaction, batch))

    print("\nInitializing Event Stream...")
    batch = ['login', 'error', 'logout']
    event = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: {event.stream_type}")
    print("Processing event batch: [" + ", ".join(batch) + "]")
    print(processor.process_stream(event, batch))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    streams = [
        (SensorStream("SENSOR_002"), [100, 100]),
        (TransactionStream("TRANS_002"), [100, 500, -50, -96]),
        (EventStream("EVENT_002"), ['login', 'error', 'logout'])
    ]

    for stream, data in streams:
        print(processor.process_stream(stream, data))
