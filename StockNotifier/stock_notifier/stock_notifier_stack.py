from aws_cdk import (
    Stack,
    aws_ssm as ssm,
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb,
    aws_events as events,
    aws_events_targets as targets,
    Duration
)
from constructs import Construct
from aws_cdk.aws_ecr_assets import DockerImageAsset
import os

class StockNotifierStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # ParameterStore details for Discord webhook URL
        discord_webhook_url = ssm.StringParameter(
            self,
            "DiscordWebhookUrl",
            parameter_name="DISCORD_WEBHOOK_URL",
            string_value=os.getenv("DISCORD_WEBHOOK_URL"),
            description="Discord Webhook URL string",
            tier=ssm.ParameterTier.STANDARD
        )

        # Create a ECR repository for our docker image
        stock_notifier_docker_image = DockerImageAsset(
            self,
            "StockNotifierImage",
            directory="./lambda",
            file="Dockerfile"
        )

        # Lambda Function
        stock_notifier_lambda = _lambda.DockerImageFunction(
            self,
            "StockNotifierLambda",
            function_name="StockNotifierLambda",
            memory_size=2048,
            timeout=Duration.seconds(600),
            environment={ "DISCORD_WEBHOOK_URL_ARN": discord_webhook_url.parameter_arn},
            code=_lambda.DockerImageCode.from_ecr(
                repository=stock_notifier_docker_image.repository,
                tag_or_digest=stock_notifier_docker_image.image_tag
            )
        )

        # Stock DynamoDB Table
        stock_dynamo_table = dynamodb.Table(
            self,
            "StockTable",
            partition_key=dynamodb.Attribute(
                name="PartId",
                type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(
                name="StoreId",
                type=dynamodb.AttributeType.STRING
            ),
            table_name="StockTable",
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST
        )

        # Cloudwatch event (once per minute)
        one_minute_event_rule = events.Rule(
            self,
            "MinuteRule",
            rule_name="MinuteRule",
            schedule=events.Schedule.cron(
                minute="*", 
                hour="*" 
            )
        )

        # Connect our one minute rule to our Lambda Function
        one_minute_event_rule.add_target(
            targets.LambdaFunction(stock_notifier_lambda)
        )

        # Give our Lambda Function the permissions to read off of our Parameter Store
        discord_webhook_url.grant_read(stock_notifier_lambda)

        # Give our Lambda Function the permissions to read/write to Dynamo
        stock_dynamo_table.grant_read_write_data(stock_notifier_lambda)

        # Give Lambda permission to pull our ECR image
        stock_notifier_docker_image.repository.grant_pull(stock_notifier_lambda)






