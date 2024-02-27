#
# Copyright (C) 2017-2021 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit from tissot device
AB_OTA_UPDATER := true
TARGET_IS_LEGACY := true
$(call inherit-product, device/xiaomi/tissot/device.mk)

# Inherit some common Evolution X stuff.
$(call inherit-product, vendor/evolution/config/common_full_phone.mk)
EVO_BUILD_TYPE := OFFICIAL
TARGET_BOOT_ANIMATION_RES := 1080
TARGET_GAPPS_ARCH := arm64
TARGET_INCLUDE_STOCK_ARCORE := false
TARGET_INCLUDE_LIVE_WALLPAPERS := false
TARGET_SUPPORTS_GOOGLE_RECORDER := false
TARGET_SUPPORTS_QUICK_TAP := true
TARGET_USES_MINI_GAPPS := true

# Device identifier. This must come after all inclusions
PRODUCT_DEVICE := tissot
PRODUCT_NAME := evolution_tissot
BOARD_VENDOR := Xiaomi
PRODUCT_BRAND := Xiaomi
PRODUCT_MODEL := Mi A1
PRODUCT_MANUFACTURER := Xiaomi
TARGET_VENDOR := Xiaomi

PRODUCT_GMS_CLIENTID_BASE := android-xiaomi

# Evolution-X Stuffs
TARGET_GAPPS_ARCH := arm64
TARGET_SUPPORTS_QUICK_TAP := true
TARGET_BOOT_ANIMATION_RES := 1080
TARGET_INCLUDE_STOCK_ARCORE := false
TARGET_INCLUDE_LIVE_WALLPAPERS := false
TARGET_SUPPORTS_GOOGLE_RECORDER := false
TARGET_USES_MINI_GAPPS := true
EVO_BUILD_TYPE := UNOFFICIAL
