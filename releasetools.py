# Copyright (C) 2009 The Android Open Source Project
# Copyright (c) 2011, The Linux Foundation. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import common
import re

def FullOTA_Assertions(info):
  AddTrustZoneAssertion(info)
  return

def IncrementalOTA_Assertions(info):
  AddTrustZoneAssertion(info)
  return

def IncrementalOTA_InstallEnd(info):
  ReplaceDeviceConfig(info)

def FullOTA_InstallEnd(info):
  ReplaceDeviceConfig(info)

def AddTrustZoneAssertion(info):
  android_info = info.input_zip.read("OTA/android-info.txt")
  m = re.search(r'require\s+version-trustzone\s*=\s*(\S+)', android_info)
  if m:
    versions = m.group(1).split('|')
    if len(versions) and '*' not in versions:
      cmd = 'assert(qcom.verify_trustzone(' + ','.join(['"%s"' % tz for tz in versions]) + ') == "1" || abort("Your firmware is incompatible with this ROM version. Please update it to newest available version"););'
      info.script.AppendExtra(cmd)
  return

def ReplaceDeviceConfig(info):
  info.script.Mount("/system")
  info.script.AppendExtra('ui_print("Checking Single SIM variant");')
  info.script.AppendExtra('run_program("/sbin/sh", "/tmp/install/bin/check_features.sh");')
  info.script.Unmount("/system")
