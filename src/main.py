from logevent import IntrusionEvent, S3Client, MalwareDataPipeline

def main():
    sus = IntrusionEvent("This is a test log event.", "sensor_001")
    # sus.process_event()

    print("--- Composition ---\n")
    print(f"The Sensor ID: {sus.metadata.sensor_id}")
    print(f"The event happened on: {sus.metadata.timestampt}")
    print(sus.raw_log)

    print("--- Aggregation ---\n")
    # The client exists independently of the pipeline.
    shared_s3_client = S3Client(bucket_name="sec-ops-cold-storage")
    pipeline = MalwareDataPipeline(storage_client=shared_s3_client)

    payload = { "name": "Charlie" }
    pipeline.run_pipeline(payload)

if __name__ == "__main__":
    main()