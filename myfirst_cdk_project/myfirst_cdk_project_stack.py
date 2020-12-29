from aws_cdk import core
from aws_cdk import aws_s3 as _s3


class MyfirstCdkProjectStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        mybucket = _s3.Bucket(
            self,
            "myBucketId",
            bucket_name="ajkumar011cloud-9999",
            versioned=True,
            encryption=_s3.BucketEncryption.S3_MANAGED,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=core.RemovalPolicy.DESTROY
            )
        mybucket2 = _s3.Bucket(
            self,
            "myBucketId2",
            bucket_name="ajkumar011cloud-10000",
            versioned=True,
            encryption=_s3.BucketEncryption.S3_MANAGED,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=core.RemovalPolicy.DESTROY
            )
        
        
        output_1 = core.CfnOutput(
            self,
            "myBucketOutput1",
            value=mybucket.bucket_name, 
            description=f"my first bucket", 
            export_name="myBucketOutput1"
            )
        output_2 = core.CfnOutput(
            self,
            "myBucketOutput2",
            value=mybucket2.bucket_name
            )

