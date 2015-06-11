"""Generated message classes for computeaccounts version alpha.

API for the Google Compute Accounts service.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from protorpc import messages


package = 'computeaccounts'


class AuthorizedKeysView(messages.Message):
  """A list of authorized public keys for a user account.

  Fields:
    keys: [Output Only] The list of authorized public keys in SSH format.
  """

  keys = messages.StringField(1, repeated=True)


class ComputeaccountsGlobalAccountsOperationsDeleteRequest(messages.Message):
  """A ComputeaccountsGlobalAccountsOperationsDeleteRequest object.

  Fields:
    operation: Name of the operation resource to delete.
    project: Project ID for this request.
  """

  operation = messages.StringField(1, required=True)
  project = messages.StringField(2, required=True)


class ComputeaccountsGlobalAccountsOperationsDeleteResponse(messages.Message):
  """An empty ComputeaccountsGlobalAccountsOperationsDelete response."""


class ComputeaccountsGlobalAccountsOperationsGetRequest(messages.Message):
  """A ComputeaccountsGlobalAccountsOperationsGetRequest object.

  Fields:
    operation: Name of the operation resource to return.
    project: Project ID for this request.
  """

  operation = messages.StringField(1, required=True)
  project = messages.StringField(2, required=True)


class ComputeaccountsGlobalAccountsOperationsListRequest(messages.Message):
  """A ComputeaccountsGlobalAccountsOperationsListRequest object.

  Fields:
    filter: Filter expression for filtering listed resources.
    maxResults: Maximum count of results to be returned.
    pageToken: Tag returned by a previous list request when that list was
      truncated to maxResults. Used to continue a previous list request.
    project: Project ID for this request.
  """

  filter = messages.StringField(1)
  maxResults = messages.IntegerField(2, variant=messages.Variant.UINT32, default=500)
  pageToken = messages.StringField(3)
  project = messages.StringField(4, required=True)


class ComputeaccountsGroupsAddMemberRequest(messages.Message):
  """A ComputeaccountsGroupsAddMemberRequest object.

  Fields:
    groupName: Name of the group for this request.
    groupsAddMemberRequest: A GroupsAddMemberRequest resource to be passed as
      the request body.
    project: Project ID for this request.
  """

  groupName = messages.StringField(1, required=True)
  groupsAddMemberRequest = messages.MessageField('GroupsAddMemberRequest', 2)
  project = messages.StringField(3, required=True)


class ComputeaccountsGroupsDeleteRequest(messages.Message):
  """A ComputeaccountsGroupsDeleteRequest object.

  Fields:
    groupName: Name of the Group resource to delete.
    project: Project ID for this request.
  """

  groupName = messages.StringField(1, required=True)
  project = messages.StringField(2, required=True)


class ComputeaccountsGroupsGetRequest(messages.Message):
  """A ComputeaccountsGroupsGetRequest object.

  Fields:
    groupName: Name of the Group resource to return.
    project: Project ID for this request.
  """

  groupName = messages.StringField(1, required=True)
  project = messages.StringField(2, required=True)


class ComputeaccountsGroupsInsertRequest(messages.Message):
  """A ComputeaccountsGroupsInsertRequest object.

  Fields:
    group: A Group resource to be passed as the request body.
    project: Project ID for this request.
  """

  group = messages.MessageField('Group', 1)
  project = messages.StringField(2, required=True)


class ComputeaccountsGroupsListRequest(messages.Message):
  """A ComputeaccountsGroupsListRequest object.

  Fields:
    filter: Filter expression for filtering listed resources.
    maxResults: Maximum count of results to be returned.
    pageToken: Tag returned by a previous list request when that list was
      truncated to maxResults. Used to continue a previous list request.
    project: Project ID for this request.
  """

  filter = messages.StringField(1)
  maxResults = messages.IntegerField(2, variant=messages.Variant.UINT32, default=500)
  pageToken = messages.StringField(3)
  project = messages.StringField(4, required=True)


class ComputeaccountsGroupsRemoveMemberRequest(messages.Message):
  """A ComputeaccountsGroupsRemoveMemberRequest object.

  Fields:
    groupName: Name of the group for this request.
    groupsRemoveMemberRequest: A GroupsRemoveMemberRequest resource to be
      passed as the request body.
    project: Project ID for this request.
  """

  groupName = messages.StringField(1, required=True)
  groupsRemoveMemberRequest = messages.MessageField('GroupsRemoveMemberRequest', 2)
  project = messages.StringField(3, required=True)


class ComputeaccountsLinuxGetAuthorizedKeysViewRequest(messages.Message):
  """A ComputeaccountsLinuxGetAuthorizedKeysViewRequest object.

  Fields:
    instance: The fully-qualified URL of the virtual machine requesting the
      view.
    project: Project ID for this request.
    user: The user account for which you want to get a list of authorized
      public keys.
    zone: Name of the zone for this request.
  """

  instance = messages.StringField(1, required=True)
  project = messages.StringField(2, required=True)
  user = messages.StringField(3, required=True)
  zone = messages.StringField(4, required=True)


class ComputeaccountsLinuxGetLinuxAccountViewsRequest(messages.Message):
  """A ComputeaccountsLinuxGetLinuxAccountViewsRequest object.

  Fields:
    filter: Filter expression for filtering listed resources.
    instance: The fully-qualified URL of the virtual machine requesting the
      views.
    maxResults: Maximum count of results to be returned.
    pageToken: Tag returned by a previous list request when that list was
      truncated to maxResults. Used to continue a previous list request.
    project: Project ID for this request.
    user: If provided, the user requesting the views. If left blank, the
      system is requesting the views, instead of a particular user.
    zone: Name of the zone for this request.
  """

  filter = messages.StringField(1)
  instance = messages.StringField(2, required=True)
  maxResults = messages.IntegerField(3, variant=messages.Variant.UINT32, default=500)
  pageToken = messages.StringField(4)
  project = messages.StringField(5, required=True)
  user = messages.StringField(6)
  zone = messages.StringField(7, required=True)


class ComputeaccountsUsersAddPublicKeyRequest(messages.Message):
  """A ComputeaccountsUsersAddPublicKeyRequest object.

  Fields:
    project: Project ID for this request.
    publicKey: A PublicKey resource to be passed as the request body.
    user: Name of the user for this request.
  """

  project = messages.StringField(1, required=True)
  publicKey = messages.MessageField('PublicKey', 2)
  user = messages.StringField(3, required=True)


class ComputeaccountsUsersDeleteRequest(messages.Message):
  """A ComputeaccountsUsersDeleteRequest object.

  Fields:
    project: Project ID for this request.
    user: Name of the user resource to delete.
  """

  project = messages.StringField(1, required=True)
  user = messages.StringField(2, required=True)


class ComputeaccountsUsersGetRequest(messages.Message):
  """A ComputeaccountsUsersGetRequest object.

  Fields:
    project: Project ID for this request.
    user: Name of the user resource to return.
  """

  project = messages.StringField(1, required=True)
  user = messages.StringField(2, required=True)


class ComputeaccountsUsersInsertRequest(messages.Message):
  """A ComputeaccountsUsersInsertRequest object.

  Fields:
    project: Project ID for this request.
    user: A User resource to be passed as the request body.
  """

  project = messages.StringField(1, required=True)
  user = messages.MessageField('User', 2)


class ComputeaccountsUsersListRequest(messages.Message):
  """A ComputeaccountsUsersListRequest object.

  Fields:
    filter: Filter expression for filtering listed resources.
    maxResults: Maximum count of results to be returned.
    pageToken: Tag returned by a previous list request when that list was
      truncated to maxResults. Used to continue a previous list request.
    project: Project ID for this request.
  """

  filter = messages.StringField(1)
  maxResults = messages.IntegerField(2, variant=messages.Variant.UINT32, default=500)
  pageToken = messages.StringField(3)
  project = messages.StringField(4, required=True)


class ComputeaccountsUsersRemovePublicKeyRequest(messages.Message):
  """A ComputeaccountsUsersRemovePublicKeyRequest object.

  Fields:
    fingerprint: The fingerprint of the public key to delete. Public keys are
      identified by their fingerprint, which is defined by RFC4716 to be the
      MD5 digest of the public key.
    project: Project ID for this request.
    user: Name of the user for this request.
  """

  fingerprint = messages.StringField(1, required=True)
  project = messages.StringField(2, required=True)
  user = messages.StringField(3, required=True)


class Group(messages.Message):
  """A Group resource.

  Fields:
    creationTimestamp: [Output Only] Creation timestamp in RFC3339 text
      format.
    description: An optional textual description of the resource; provided by
      the client when the resource is created.
    id: [Output Only] Unique identifier for the resource; defined by the
      server.
    kind: [Output Only] Type of the resource. Always computeaccounts#group for
      groups.
    members: [Output Only] A list of URLs to User resources who belong to the
      group. Users may only be members of groups in the same project.
    name: Name of the resource; provided by the client when the resource is
      created.
    selfLink: [Output Only] Server defined URL for the resource.
  """

  creationTimestamp = messages.StringField(1)
  description = messages.StringField(2)
  id = messages.IntegerField(3, variant=messages.Variant.UINT64)
  kind = messages.StringField(4, default=u'computeaccounts#group')
  members = messages.StringField(5, repeated=True)
  name = messages.StringField(6)
  selfLink = messages.StringField(7)


class GroupList(messages.Message):
  """A GroupList object.

  Fields:
    id: [Output Only] Unique identifier for the resource; defined by the
      server.
    items: [Output Only] A list of Group resources.
    kind: [Output Only] Type of resource. Always computeaccounts#groupList for
      lists of groups.
    nextPageToken: [Output Only] A token used to continue a truncated list
      request.
    selfLink: [Output Only] Server defined URL for this resource.
  """

  id = messages.StringField(1)
  items = messages.MessageField('Group', 2, repeated=True)
  kind = messages.StringField(3, default=u'computeaccounts#groupList')
  nextPageToken = messages.StringField(4)
  selfLink = messages.StringField(5)


class GroupsAddMemberRequest(messages.Message):
  """A GroupsAddMemberRequest object.

  Fields:
    users: Fully-qualified URLs of the User resources to add.
  """

  users = messages.StringField(1, repeated=True)


class GroupsRemoveMemberRequest(messages.Message):
  """A GroupsRemoveMemberRequest object.

  Fields:
    users: Fully-qualified URLs of the User resources to remove.
  """

  users = messages.StringField(1, repeated=True)


class LinuxAccountViews(messages.Message):
  """A list of all Linux accounts for this project. This API is only used by
  Compute Engine virtual machines to get information about user accounts for a
  project or instance. Linux resources are read-only views into users and
  groups managed by the Compute Engine Accounts API.

  Fields:
    groupViews: [Output Only] A list of all groups within a project.
    kind: [Output Only] Type of the resource. Always
      computeaccounts#linuxAccountViews for Linux resources.
    userViews: [Output Only] A list of all users within a project.
  """

  groupViews = messages.MessageField('LinuxGroupView', 1, repeated=True)
  kind = messages.StringField(2, default=u'computeaccounts#linuxAccountViews')
  userViews = messages.MessageField('LinuxUserView', 3, repeated=True)


class LinuxGetAuthorizedKeysViewResponse(messages.Message):
  """A LinuxGetAuthorizedKeysViewResponse object.

  Fields:
    resource: [Output Only] A list of authorized public keys for a user.
  """

  resource = messages.MessageField('AuthorizedKeysView', 1)


class LinuxGetLinuxAccountViewsResponse(messages.Message):
  """A LinuxGetLinuxAccountViewsResponse object.

  Fields:
    resource: [Output Only] A list of authorized user accounts and groups.
  """

  resource = messages.MessageField('LinuxAccountViews', 1)


class LinuxGroupView(messages.Message):
  """A detailed view of a Linux group.

  Fields:
    gid: [Output Only] The Group ID.
    groupName: [Output Only] Group name.
    members: [Output Only] List of user accounts that belong to the group.
  """

  gid = messages.IntegerField(1, variant=messages.Variant.UINT32)
  groupName = messages.StringField(2)
  members = messages.StringField(3, repeated=True)


class LinuxUserView(messages.Message):
  """A detailed view of a Linux user account.

  Fields:
    gecos: [Output Only] The GECOS (user information) entry for this account.
    gid: [Output Only] User's default group ID.
    homeDirectory: [Output Only] The path to the home directory for this
      account.
    shell: [Output Only] The path to the login shell for this account.
    uid: [Output Only] User ID.
    username: [Output Only] The username of the account.
  """

  gecos = messages.StringField(1)
  gid = messages.IntegerField(2, variant=messages.Variant.UINT32)
  homeDirectory = messages.StringField(3)
  shell = messages.StringField(4)
  uid = messages.IntegerField(5, variant=messages.Variant.UINT32)
  username = messages.StringField(6)


class Operation(messages.Message):
  """An operation resource, used to manage asynchronous API requests.

  Enums:
    StatusValueValuesEnum: [Output Only] Status of the operation. Can be one
      of the following: PENDING, RUNNING, or DONE.

  Messages:
    ErrorValue: [Output Only] If errors are generated during processing of the
      operation, this field will be populated.
    WarningsValueListEntry: A WarningsValueListEntry object.

  Fields:
    clientOperationId: [Output Only] An optional identifier specified by the
      client when the mutation was initiated. Must be unique for all operation
      resources in the project.
    creationTimestamp: [Output Only] Creation timestamp in RFC3339 text
      format.
    endTime: [Output Only] The time that this operation was completed. This is
      in RFC3339 text format.
    error: [Output Only] If errors are generated during processing of the
      operation, this field will be populated.
    httpErrorMessage: [Output Only] If the operation fails, this field
      contains the HTTP error message that was returned, such as NOT FOUND.
    httpErrorStatusCode: [Output Only] If the operation fails, this field
      contains the HTTP error message that was returned, such as 404.
    id: [Output Only] Unique identifier for the resource; defined by the
      server.
    insertTime: [Output Only] The time that this operation was requested. This
      is in RFC3339 text format.
    kind: [Output Only] Type of the resource. Always compute#Operation for
      Operation resources.
    name: [Output Only] Name of the resource.
    operationType: [Output Only] Type of the operation, such as insert,
      update, and delete.
    progress: [Output Only] An optional progress indicator that ranges from 0
      to 100. There is no requirement that this be linear or support any
      granularity of operations. This should not be used to guess at when the
      operation will be complete. This number should monotonically increase as
      the operation progresses.
    region: [Output Only] URL of the region where the operation resides. Only
      applicable for regional resources.
    selfLink: [Output Only] Server defined URL for the resource.
    startTime: [Output Only] The time that this operation was started by the
      server. This is in RFC3339 text format.
    status: [Output Only] Status of the operation. Can be one of the
      following: PENDING, RUNNING, or DONE.
    statusMessage: [Output Only] An optional textual description of the
      current status of the operation.
    targetId: [Output Only] Unique target ID which identifies a particular
      incarnation of the target.
    targetLink: [Output Only] URL of the resource the operation is mutating.
    user: [Output Only] User who requested the operation, for example:
      user@example.com.
    warnings: [Output Only] If warning messages are generated during
      processing of the operation, this field will be populated.
    zone: [Output Only] URL of the zone where the operation resides.
  """

  class StatusValueValuesEnum(messages.Enum):
    """[Output Only] Status of the operation. Can be one of the following:
    PENDING, RUNNING, or DONE.

    Values:
      DONE: <no description>
      PENDING: <no description>
      RUNNING: <no description>
    """
    DONE = 0
    PENDING = 1
    RUNNING = 2

  class ErrorValue(messages.Message):
    """[Output Only] If errors are generated during processing of the
    operation, this field will be populated.

    Messages:
      ErrorsValueListEntry: A ErrorsValueListEntry object.

    Fields:
      errors: [Output Only] The array of errors encountered while processing
        this operation.
    """

    class ErrorsValueListEntry(messages.Message):
      """A ErrorsValueListEntry object.

      Fields:
        code: [Output Only] The error type identifier for this error.
        location: [Output Only] Indicates the field in the request which
          caused the error. This property is optional.
        message: [Output Only] An optional, human-readable error message.
      """

      code = messages.StringField(1)
      location = messages.StringField(2)
      message = messages.StringField(3)

    errors = messages.MessageField('ErrorsValueListEntry', 1, repeated=True)

  class WarningsValueListEntry(messages.Message):
    """A WarningsValueListEntry object.

    Enums:
      CodeValueValuesEnum: [Output Only] The warning type identifier for this
        warning.

    Messages:
      DataValueListEntry: A DataValueListEntry object.

    Fields:
      code: [Output Only] The warning type identifier for this warning.
      data: [Output Only] Metadata for this warning in key: value format.
      message: [Output Only] Optional human-readable details for this warning.
    """

    class CodeValueValuesEnum(messages.Enum):
      """[Output Only] The warning type identifier for this warning.

      Values:
        DEPRECATED_RESOURCE_USED: <no description>
        DISK_SIZE_LARGER_THAN_IMAGE_SIZE: <no description>
        INJECTED_KERNELS_DEPRECATED: <no description>
        NEXT_HOP_ADDRESS_NOT_ASSIGNED: <no description>
        NEXT_HOP_CANNOT_IP_FORWARD: <no description>
        NEXT_HOP_INSTANCE_NOT_FOUND: <no description>
        NEXT_HOP_INSTANCE_NOT_ON_NETWORK: <no description>
        NEXT_HOP_NOT_RUNNING: <no description>
        NOT_CRITICAL_ERROR: <no description>
        NO_RESULTS_ON_PAGE: <no description>
        REQUIRED_TOS_AGREEMENT: <no description>
        RESOURCE_NOT_DELETED: <no description>
        SINGLE_INSTANCE_PROPERTY_TEMPLATE: <no description>
        UNREACHABLE: <no description>
      """
      DEPRECATED_RESOURCE_USED = 0
      DISK_SIZE_LARGER_THAN_IMAGE_SIZE = 1
      INJECTED_KERNELS_DEPRECATED = 2
      NEXT_HOP_ADDRESS_NOT_ASSIGNED = 3
      NEXT_HOP_CANNOT_IP_FORWARD = 4
      NEXT_HOP_INSTANCE_NOT_FOUND = 5
      NEXT_HOP_INSTANCE_NOT_ON_NETWORK = 6
      NEXT_HOP_NOT_RUNNING = 7
      NOT_CRITICAL_ERROR = 8
      NO_RESULTS_ON_PAGE = 9
      REQUIRED_TOS_AGREEMENT = 10
      RESOURCE_NOT_DELETED = 11
      SINGLE_INSTANCE_PROPERTY_TEMPLATE = 12
      UNREACHABLE = 13

    class DataValueListEntry(messages.Message):
      """A DataValueListEntry object.

      Fields:
        key: [Output Only] A key for the warning data.
        value: [Output Only] A warning data value corresponding to the key.
      """

      key = messages.StringField(1)
      value = messages.StringField(2)

    code = messages.EnumField('CodeValueValuesEnum', 1)
    data = messages.MessageField('DataValueListEntry', 2, repeated=True)
    message = messages.StringField(3)

  clientOperationId = messages.StringField(1)
  creationTimestamp = messages.StringField(2)
  endTime = messages.StringField(3)
  error = messages.MessageField('ErrorValue', 4)
  httpErrorMessage = messages.StringField(5)
  httpErrorStatusCode = messages.IntegerField(6, variant=messages.Variant.INT32)
  id = messages.IntegerField(7, variant=messages.Variant.UINT64)
  insertTime = messages.StringField(8)
  kind = messages.StringField(9, default=u'computeaccounts#operation')
  name = messages.StringField(10)
  operationType = messages.StringField(11)
  progress = messages.IntegerField(12, variant=messages.Variant.INT32)
  region = messages.StringField(13)
  selfLink = messages.StringField(14)
  startTime = messages.StringField(15)
  status = messages.EnumField('StatusValueValuesEnum', 16)
  statusMessage = messages.StringField(17)
  targetId = messages.IntegerField(18, variant=messages.Variant.UINT64)
  targetLink = messages.StringField(19)
  user = messages.StringField(20)
  warnings = messages.MessageField('WarningsValueListEntry', 21, repeated=True)
  zone = messages.StringField(22)


class OperationList(messages.Message):
  """Contains a list of operation resources.

  Fields:
    id: [Output Only] Unique identifier for the resource; defined by the
      server.
    items: [Output Only] The operation resources.
    kind: [Output Only] Type of resource. Always compute#operations for
      Operations resource.
    nextPageToken: [Output Only] A token used to continue a truncate.
    selfLink: [Output Only] Server defined URL for this resource.
  """

  id = messages.StringField(1)
  items = messages.MessageField('Operation', 2, repeated=True)
  kind = messages.StringField(3, default=u'computeaccounts#operationList')
  nextPageToken = messages.StringField(4)
  selfLink = messages.StringField(5)


class PublicKey(messages.Message):
  """A public key for authenticating to guests.

  Fields:
    creationTimestamp: [Output Only] Creation timestamp in RFC3339 text
      format.
    description: An optional textual description of the resource; provided by
      the client when the resource is created.
    expirationTimestamp: Optional expiration timestamp. If provided, the
      timestamp must be in RFC3339 text format. If not provided, the public
      key never expires.
    fingerprint: [Output Only] The fingerprint of the key is defined by
      RFC4716 to be the MD5 digest of the public key.
    key: Public key text in SSH format, defined by RFC4253 section 6.6.
  """

  creationTimestamp = messages.StringField(1)
  description = messages.StringField(2)
  expirationTimestamp = messages.StringField(3)
  fingerprint = messages.StringField(4)
  key = messages.StringField(5)


class StandardQueryParameters(messages.Message):
  """Query parameters accepted by all methods.

  Enums:
    AltValueValuesEnum: Data format for the response.

  Fields:
    alt: Data format for the response.
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters. Overrides userIp if both are provided.
    trace: A tracing token of the form "token:<tokenid>" or "email:<ldap>" to
      include in api requests.
    userIp: IP address of the site where the request originates. Use this if
      you want to enforce per-user limits.
  """

  class AltValueValuesEnum(messages.Enum):
    """Data format for the response.

    Values:
      json: Responses with Content-Type of application/json
    """
    json = 0

  alt = messages.EnumField('AltValueValuesEnum', 1, default=u'json')
  fields = messages.StringField(2)
  key = messages.StringField(3)
  oauth_token = messages.StringField(4)
  prettyPrint = messages.BooleanField(5, default=True)
  quotaUser = messages.StringField(6)
  trace = messages.StringField(7)
  userIp = messages.StringField(8)


class User(messages.Message):
  """A User resource.

  Fields:
    creationTimestamp: [Output Only] Creation timestamp in RFC3339 text
      format.
    description: An optional textual description of the resource; provided by
      the client when the resource is created.
    groups: [Output Only] A list of URLs to Group resources who contain the
      user. Users are only members of groups in the same project.
    id: [Output Only] Unique identifier for the resource; defined by the
      server.
    kind: [Output Only] Type of the resource. Always computeaccounts#user for
      users.
    name: Name of the resource; provided by the client when the resource is
      created.
    owner: Email address of account's owner. This account will be validated to
      make sure it exists. The email can belong to any domain, but it must be
      tied to a Google account.
    publicKeys: [Output Only] Public keys that this user may use to login.
    selfLink: [Output Only] Server defined URL for the resource.
  """

  creationTimestamp = messages.StringField(1)
  description = messages.StringField(2)
  groups = messages.StringField(3, repeated=True)
  id = messages.IntegerField(4, variant=messages.Variant.UINT64)
  kind = messages.StringField(5, default=u'computeaccounts#user')
  name = messages.StringField(6)
  owner = messages.StringField(7)
  publicKeys = messages.MessageField('PublicKey', 8, repeated=True)
  selfLink = messages.StringField(9)


class UserList(messages.Message):
  """A UserList object.

  Fields:
    id: [Output Only] Unique identifier for the resource; defined by the
      server.
    items: [Output Only] A list of User resources.
    kind: [Output Only] Type of resource. Always computeaccounts#userList for
      lists of users.
    nextPageToken: [Output Only] A token used to continue a truncated list
      request.
    selfLink: [Output Only] Server defined URL for this resource.
  """

  id = messages.StringField(1)
  items = messages.MessageField('User', 2, repeated=True)
  kind = messages.StringField(3, default=u'computeaccounts#userList')
  nextPageToken = messages.StringField(4)
  selfLink = messages.StringField(5)


