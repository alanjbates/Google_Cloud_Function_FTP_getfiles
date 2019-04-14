# Google Cloud Function scheduled pull of files from FTP to GCS

This is a Google Cloud Function that was written to retrieve all .zip files from a 3rd party FTP site. 

The function is triggered by an http request every 5 minutes from Google Cloud Scheduler.

It can deployed with CI/CD using Google Cloud Build triggers tied to the cloudbuid.yaml file in your bitbucket or github or cloud source repo.

This is a simple and effective serverless way to pull files from FTP sites into GCP storage buckets on a cron schedule.

![Image of Architecture](https://raw.githubusercontent.com/alanjbates/Google_Cloud_Function_FTP_getfiles/master/serverless_ftp_retrieval.draw.io.png)

*NOTE* You will want to consider if clear text authentication credentials in your source code fits your security standards.  For production deployment, encrypted or obscured authentication credentials are recommended. 
