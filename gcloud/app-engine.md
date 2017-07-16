##### Crate configuratons
```
gcloud config configurations create [NAME]
```
##### Set and unset configurations
```
gcloud config set project [PROJECT]
gcloud config unset disable_usage_reporting
```

##### List all the configurations
```
gcloud config list
```

##### Deploy
```
gcloud app deploy
gcloud app deploy --verbosity=info
gcloud app deploy --project [YOUR_PROJECT_ID]
```

##### stream logs
```
gcloud app logs tail -s default
```

##### Browse
```
gcloud app browse
```

##### projects page
https://console.cloud.google.com/cloud-resource-manager
