import json
import boto3
import os

s3 = boto3.client('s3')
polly = boto3.client('polly')

# Environment variables (recommended)
DESTINATION_BUCKET = os.environ.get('DEST_BUCKET')

def lambda_handler(event, context):
    try:
        # Get uploaded file details
        source_bucket = event['Records'][0]['s3']['bucket']['name']
        object_key = event['Records'][0]['s3']['object']['key']

        # Process only .txt files
        if not object_key.endswith('.txt'):
            return {
                'statusCode': 200,
                'body': 'Not a text file. Skipping.'
            }

        # Read text file from S3
        response = s3.get_object(Bucket=source_bucket, Key=object_key)
        text_data = response['Body'].read().decode('utf-8')

        # Convert text to speech using Polly
        polly_response = polly.synthesize_speech(
            Text=text_data,
            OutputFormat='mp3',
            VoiceId='Joanna'
        )

        # Create audio file name
        audio_file_name = object_key.replace('.txt', '.mp3')

        # Upload MP3 file to destination bucket
        s3.put_object(
            Bucket=DESTINATION_BUCKET,
            Key=audio_file_name,
            Body=polly_response['AudioStream'].read(),
            ContentType='audio/mpeg'
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Audio file created successfully')
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }


Test Event JSON
{
  "Records": [
    {
      "s3": {
        "bucket": {
          "name": "amc-polly-source-bucket"
        },
        "object": {
          "key": "sample.txt"
        }
      }
    }
  ]
}
