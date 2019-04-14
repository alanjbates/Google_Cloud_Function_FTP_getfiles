from ftplib import FTP
from fs_gcsfs import GCSFS

def getfiles(request):

    #set gcs params
    gcs_bucket_name = 'your-gcs-bucket-name'
    gcsfs = GCSFS(bucket_name=gcs_bucket_name)
    gcs_bucket_string = 'gs://' + gcs_bucket_name + '/'
	
    #set ftp params
    ftp = FTP('ftp.your-ftp-site.com')
    ftp.login('your-username', 'your-password')
    
    # get files within the root directory into list
    filenames = ftp.nlst()
	
    #loop through each each file and copy into gcs if it is a .zip file (your specific use case may be different)
    #here you can look for specific file names or remove the if statement if you are pulling everything form the ftp source
    for filename in filenames:
        if '.zip' in filename:
            gcs_target_filename = gcs_bucket_string + filename
            print('Retrieving file: ' + filename)
	    #this line pulls the file from the FTP site and writes it to a file in the GCS bucket
            ftp.retrbinary('RETR '+ filename, gcsfs.open(filename, 'wb').write)
            print('Successfully created: ' + gcs_target_filename)
            ftp.delete(filename)
            print('Deleted from remote host: ' + filename)
        else:
	    #write line for stackdriver logging
            print('No .Zip files found on remote host.')
    
    #close ftp connection
    ftp.quit()
    
    #write line for stackdriver logging
    print('done')
