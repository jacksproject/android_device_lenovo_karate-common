#
# Copyright (C) 2017 The LineageOS Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

LOCAL_C_INCLUDES := \
    system/core/base/include \
    system/core/init
LOCAL_MODULE := libinit_msm8937
LOCAL_MODULE_TAGS := optional
LOCAL_SRC_FILES := init_msm8937.cpp

ifneq ($(TARGET_LIBINIT_MSM8937_DEFINES_FILE),)
  LOCAL_SRC_FILES += ../../../../$(TARGET_LIBINIT_MSM8937_DEFINES_FILE)
endif

include $(BUILD_STATIC_LIBRARY)
