import os
from dotenv import load_dotenv
from gcp_pal import CloudScheduler, CloudFunctions

load_dotenv()

if __name__ == "__main__":
    cloud_function_uri = CloudFunctions("phone-location").uri()
    # Create a Cloud Scheduler job that runs every 2 minutes
    CloudScheduler("phone-location-2-min").create(
        schedule="*/2 * * * *",
        time_zone="UTC",
        payload={},
        target=cloud_function_uri,
        service_account=os.getenv("SERVICE_ACCOUNT"),
    )
