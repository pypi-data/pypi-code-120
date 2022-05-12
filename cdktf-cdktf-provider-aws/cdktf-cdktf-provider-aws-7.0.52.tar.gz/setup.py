import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdktf-cdktf-provider-aws",
    "version": "7.0.52",
    "description": "Prebuilt aws Provider for Terraform CDK (cdktf)",
    "license": "MPL-2.0",
    "url": "https://github.com/hashicorp/cdktf-provider-aws.git",
    "long_description_content_type": "text/markdown",
    "author": "HashiCorp",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/hashicorp/cdktf-provider-aws.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdktf_cdktf_provider_aws",
        "cdktf_cdktf_provider_aws._jsii",
        "cdktf_cdktf_provider_aws.accessanalyzer",
        "cdktf_cdktf_provider_aws.acm",
        "cdktf_cdktf_provider_aws.amplify",
        "cdktf_cdktf_provider_aws.apigateway",
        "cdktf_cdktf_provider_aws.apigatewayv2",
        "cdktf_cdktf_provider_aws.appautoscaling",
        "cdktf_cdktf_provider_aws.appconfig",
        "cdktf_cdktf_provider_aws.appmesh",
        "cdktf_cdktf_provider_aws.apprunner",
        "cdktf_cdktf_provider_aws.appstream",
        "cdktf_cdktf_provider_aws.appsync",
        "cdktf_cdktf_provider_aws.athena",
        "cdktf_cdktf_provider_aws.autoscaling",
        "cdktf_cdktf_provider_aws.autoscalingplans",
        "cdktf_cdktf_provider_aws.backup",
        "cdktf_cdktf_provider_aws.batch",
        "cdktf_cdktf_provider_aws.budgets",
        "cdktf_cdktf_provider_aws.chime",
        "cdktf_cdktf_provider_aws.cloud9",
        "cdktf_cdktf_provider_aws.cloudformation",
        "cdktf_cdktf_provider_aws.cloudfront",
        "cdktf_cdktf_provider_aws.cloudhsm",
        "cdktf_cdktf_provider_aws.cloudtrail",
        "cdktf_cdktf_provider_aws.cloudwatch",
        "cdktf_cdktf_provider_aws.codeartifact",
        "cdktf_cdktf_provider_aws.codebuild",
        "cdktf_cdktf_provider_aws.codecommit",
        "cdktf_cdktf_provider_aws.codedeploy",
        "cdktf_cdktf_provider_aws.codepipeline",
        "cdktf_cdktf_provider_aws.codestar",
        "cdktf_cdktf_provider_aws.cognito",
        "cdktf_cdktf_provider_aws.config",
        "cdktf_cdktf_provider_aws.connect",
        "cdktf_cdktf_provider_aws.cur",
        "cdktf_cdktf_provider_aws.datapipeline",
        "cdktf_cdktf_provider_aws.datasources",
        "cdktf_cdktf_provider_aws.datasync",
        "cdktf_cdktf_provider_aws.dax",
        "cdktf_cdktf_provider_aws.devicefarm",
        "cdktf_cdktf_provider_aws.directconnect",
        "cdktf_cdktf_provider_aws.directoryservice",
        "cdktf_cdktf_provider_aws.dlm",
        "cdktf_cdktf_provider_aws.dms",
        "cdktf_cdktf_provider_aws.documentdb",
        "cdktf_cdktf_provider_aws.dynamodb",
        "cdktf_cdktf_provider_aws.ec2",
        "cdktf_cdktf_provider_aws.ecr",
        "cdktf_cdktf_provider_aws.ecs",
        "cdktf_cdktf_provider_aws.efs",
        "cdktf_cdktf_provider_aws.eks",
        "cdktf_cdktf_provider_aws.elasticache",
        "cdktf_cdktf_provider_aws.elasticbeanstalk",
        "cdktf_cdktf_provider_aws.elasticsearch",
        "cdktf_cdktf_provider_aws.elastictranscoder",
        "cdktf_cdktf_provider_aws.elb",
        "cdktf_cdktf_provider_aws.emr",
        "cdktf_cdktf_provider_aws.eventbridge",
        "cdktf_cdktf_provider_aws.eventbridgeschemas",
        "cdktf_cdktf_provider_aws.fms",
        "cdktf_cdktf_provider_aws.fsx",
        "cdktf_cdktf_provider_aws.gamelift",
        "cdktf_cdktf_provider_aws.glacier",
        "cdktf_cdktf_provider_aws.globalaccelerator",
        "cdktf_cdktf_provider_aws.glue",
        "cdktf_cdktf_provider_aws.guardduty",
        "cdktf_cdktf_provider_aws.iam",
        "cdktf_cdktf_provider_aws.imagebuilder",
        "cdktf_cdktf_provider_aws.inspector",
        "cdktf_cdktf_provider_aws.iot",
        "cdktf_cdktf_provider_aws.kinesis",
        "cdktf_cdktf_provider_aws.kms",
        "cdktf_cdktf_provider_aws.lakeformation",
        "cdktf_cdktf_provider_aws.lambdafunction",
        "cdktf_cdktf_provider_aws.lex",
        "cdktf_cdktf_provider_aws.licensemanager",
        "cdktf_cdktf_provider_aws.lightsail",
        "cdktf_cdktf_provider_aws.macie",
        "cdktf_cdktf_provider_aws.macie2",
        "cdktf_cdktf_provider_aws.mediaconvert",
        "cdktf_cdktf_provider_aws.mediapackage",
        "cdktf_cdktf_provider_aws.mediastore",
        "cdktf_cdktf_provider_aws.mq",
        "cdktf_cdktf_provider_aws.msk",
        "cdktf_cdktf_provider_aws.mwaa",
        "cdktf_cdktf_provider_aws.neptune",
        "cdktf_cdktf_provider_aws.networkfirewall",
        "cdktf_cdktf_provider_aws.opsworks",
        "cdktf_cdktf_provider_aws.organizations",
        "cdktf_cdktf_provider_aws.outposts",
        "cdktf_cdktf_provider_aws.pinpoint",
        "cdktf_cdktf_provider_aws.pricing",
        "cdktf_cdktf_provider_aws.prometheus",
        "cdktf_cdktf_provider_aws.qldb",
        "cdktf_cdktf_provider_aws.quicksight",
        "cdktf_cdktf_provider_aws.ram",
        "cdktf_cdktf_provider_aws.rds",
        "cdktf_cdktf_provider_aws.redshift",
        "cdktf_cdktf_provider_aws.resourcegroups",
        "cdktf_cdktf_provider_aws.route53",
        "cdktf_cdktf_provider_aws.s3",
        "cdktf_cdktf_provider_aws.sagemaker",
        "cdktf_cdktf_provider_aws.secretsmanager",
        "cdktf_cdktf_provider_aws.securityhub",
        "cdktf_cdktf_provider_aws.serverlessapplicationrepository",
        "cdktf_cdktf_provider_aws.servicecatalog",
        "cdktf_cdktf_provider_aws.servicediscovery",
        "cdktf_cdktf_provider_aws.servicequotas",
        "cdktf_cdktf_provider_aws.ses",
        "cdktf_cdktf_provider_aws.sfn",
        "cdktf_cdktf_provider_aws.shield",
        "cdktf_cdktf_provider_aws.signer",
        "cdktf_cdktf_provider_aws.simpledb",
        "cdktf_cdktf_provider_aws.sns",
        "cdktf_cdktf_provider_aws.sqs",
        "cdktf_cdktf_provider_aws.ssm",
        "cdktf_cdktf_provider_aws.ssoadmin",
        "cdktf_cdktf_provider_aws.storagegateway",
        "cdktf_cdktf_provider_aws.swf",
        "cdktf_cdktf_provider_aws.synthetics",
        "cdktf_cdktf_provider_aws.timestreamwrite",
        "cdktf_cdktf_provider_aws.transfer",
        "cdktf_cdktf_provider_aws.vpc",
        "cdktf_cdktf_provider_aws.waf",
        "cdktf_cdktf_provider_aws.wafregional",
        "cdktf_cdktf_provider_aws.wafv2",
        "cdktf_cdktf_provider_aws.worklink",
        "cdktf_cdktf_provider_aws.workspaces",
        "cdktf_cdktf_provider_aws.xray"
    ],
    "package_data": {
        "cdktf_cdktf_provider_aws._jsii": [
            "provider-aws@7.0.52.jsii.tgz"
        ],
        "cdktf_cdktf_provider_aws": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "cdktf>=0.10.3, <0.11.0",
        "constructs>=10.0.0, <11.0.0",
        "jsii>=1.58.0, <2.0.0",
        "publication>=0.0.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
