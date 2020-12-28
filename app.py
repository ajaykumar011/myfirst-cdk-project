#!/usr/bin/env python3

from aws_cdk import core

from myfirst_cdk_project.myfirst_cdk_project_stack import MyfirstCdkProjectStack


app = core.App()
MyfirstCdkProjectStack(app, "myfirst-cdk-project")

app.synth()
