#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os




class DefaultConfig:
    """Configuration for the bot."""

    PORT = 8000
    APP_ID = os.environ.get("MicrosoftAppId", "d7766af3-19db-40a0-8b90-3b2ec4bccd95")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "9.k8Q~C2~Yut7oNb2y4ZSGRavRpDPYU4ojTMtdkY")
    LUIS_APP_ID = os.environ.get("LuisAppId", "672fbb9a-188f-4eda-a279-970645ebe47f")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "702fc50696ab44d9a2bd7afd5b0214ae")
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "flymeoc-authoring.cognitiveservices.azure.com")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get("AppInsightsInstrumentationKey", "6d1663d0-1d23-4194-ab7d-7dca282a94f4")


