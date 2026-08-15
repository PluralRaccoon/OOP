from datetime import datetime

class EventMetadata():
    """ Child Object """
    def __init__(self, sensor_id: str, timestampt: datetime):
        self.sensor_id = sensor_id
        self.timestampt = timestampt

class IntrusionEvent():
    """ Parent Object """
    def __init__(self, raw_log: str, sensor_id: str):
        self.raw_log = raw_log
        # Composition: The parent instantiates and strictly owns the child.
        # If IntrusionEvent is destroyed, EventMetadata goes down with it.
        self.metadata = EventMetadata(sensor_id, datetime.now())

    def process_event(self):
        print(f"Processing event from sensor: {self.metadata.sensor_id}")
        print(f"Timestamp: {self.metadata.timestampt}")
        print(f"Raw Log: {self.raw_log}")


class S3Client:
    """Independent service object"""
    def __init__(self, bucket_name: str):
        self.bucket_name = bucket_name

    def upload(self, data: dict) -> None:
        print(f"Uploading to {self.bucket_name}...")

class MalwareDataPipeline:
    """Parent object"""
    # Aggregation: The pipeline receives an ALREADY instantiated client.
    def __init__(self, storage_client: S3Client):
        self.storage_client = storage_client

    def run_pipeline(self, payload: dict) -> None:
        # Transformation logic here...
        print("Running pipeline...")
        self.storage_client.upload(payload)
        print("Pipeline completed successfully!")