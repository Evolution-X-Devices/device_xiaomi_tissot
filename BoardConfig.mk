#
# Copyright (C) 2017-2021 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#


# Inherit from common msm8953-common
include device/xiaomi/msm8953-common/BoardConfigCommon.mk

DEVICE_PATH := device/xiaomi/tissot

# Display
TARGET_SCREEN_DENSITY := 440

# Filesystem
BOARD_USES_RECOVERY_AS_BOOT := true
TARGET_NO_RECOVERY := true

# HIDL
DEVICE_MANIFEST_FILE += $(DEVICE_PATH)/manifest.xml

# Kernel
TARGET_KERNEL_CONFIG := tissot_defconfig

# A/B
AB_OTA_PARTITIONS += \
    boot \
    system

# Partitions
BOARD_USERDATAIMAGE_PARTITION_SIZE := 55087422464 # 25765059584 - 16384

# Camera
TARGET_SUPPORT_HAL1 := false

# Power
TARGET_TAP_TO_WAKE_NODE := "/proc/touchpanel/enable_dt2w"

# Security Patch Level
VENDOR_SECURITY_PATCH := $(PLATFORM_SECURITY_PATCH)

# Inherit the proprietary files
include vendor/xiaomi/tissot/BoardConfigVendor.mk
