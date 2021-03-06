# Copyright 2014 Google Inc. All Rights Reserved.

"""The main command group for myservice.

Everything under here will be the commands in your group.  Each file results in
a command with that name.

This module contains a single class that extends base.Group.  Calliope will
dynamically search for the implementing class and use that as the command group
for this command tree.  You can implement methods in this class to override some
of the default behavior.
"""

import argparse

from googlecloudapis.dataflow.v1beta3 import dataflow_v1beta3_client
from googlecloudapis.dataflow.v1beta3 import dataflow_v1beta3_messages
from googlecloudsdk.calliope import actions
from googlecloudsdk.calliope import base
from googlecloudsdk.core import log
from googlecloudsdk.core import properties
from googlecloudsdk.core import resolvers
from googlecloudsdk.core import resources as cloud_resources


SERVICE_NAME = 'dataflow'

DATAFLOW_MESSAGES_MODULE_KEY = 'dataflow_messages'
DATAFLOW_APITOOLS_CLIENT_KEY = 'dataflow_client'
DATAFLOW_REGISTRY_KEY = 'dataflow_registry'


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class Dataflow(base.Group):
  """Read and manipulate Google Dataflow resources.
  """

  @staticmethod
  def Args(parser):
    """Add command flags that are global to the Dataflow group.

    Args:
      parser: argparse.ArgumentParser, This is a standard argparser parser with
        which you can register arguments.  See the public argparse documentation
        for its capabilities.
    """
    parser.add_argument(
        '--endpoint', help=argparse.SUPPRESS,
        action=actions.StoreProperty(
            properties.VALUES.api_endpoint_overrides.dataflow))

  def Filter(self, context, args):
    """Setup the API client within the context for this group's commands.

    Args:
      context: {str:object}, A set of key-value pairs that can be used for
          common initialization among commands.
      args: argparse.Namespace: The same namespace given to the corresponding
          .Run() invocation.
    """
    cloud_resources.SetParamDefault(
        api='dataflow', collection=None, param='projectId',
        resolver=resolvers.FromProperty(properties.VALUES.core.project))

    context[DATAFLOW_MESSAGES_MODULE_KEY] = dataflow_v1beta3_messages

    context[DATAFLOW_APITOOLS_CLIENT_KEY] = (
        dataflow_v1beta3_client.DataflowV1beta3(
            url=properties.VALUES.api_endpoint_overrides.dataflow.Get(),
            get_credentials=False,
            http=self.Http()))
    context[DATAFLOW_REGISTRY_KEY] = cloud_resources.REGISTRY
