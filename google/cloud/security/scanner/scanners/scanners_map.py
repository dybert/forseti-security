# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Map for mapping rules engine to scanner class"""

# pylint: disable=line-too-long
from google.cloud.security.scanner.scanners.groups_scanner import GroupsScanner
from google.cloud.security.scanner.scanners.iam_rules_scanner import IamPolicyScanner
from google.cloud.security.scanner.scanners.bigquery_scanner import BigqueryScanner
from google.cloud.security.scanner.scanners.bucket_rules_scanner import BucketsAclScanner
from google.cloud.security.scanner.scanners.cloudsql_rules_scanner import CloudSqlAclScanner
# pylint: enable=line-too-long


SCANNER_MAP = {
    'BigqueryRulesEngine': BigqueryScanner,
    'BucketsRulesEngine': BucketsAclScanner,
    'CloudSqlRulesEngine': CloudSqlAclScanner,
    'GroupsRulesEngine': GroupsScanner,
    'IamRulesEngine': IamPolicyScanner
}

FLATTENING_MAP = {
    'BigqueryRulesEngine': 'bigquery_acl_violations',
    'BucketsRulesEngine': 'buckets_acl_violations',
    'CloudSqlRulesEngine': 'cloudsql_acl_violations',
    'GroupsRulesEngine': 'groups_violations',
    'IamRulesEngine': 'policy_violations'
}

RESOURCE_MAP = {
    'bigquery_acl_violations': 'violations',
    'buckets_acl_violations': 'violations',
    'cloudsql_acl_violations': 'violations',
    'groups_violations': 'groups_violations',
    'policy_violations': 'violations'
}