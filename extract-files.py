#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

import extract_utils.tools

extract_utils.tools.DEFAULT_PATCHELF_VERSION = '0_18'

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'hardware/qcom-caf/msm8996',
    'hardware/xiaomi',
    'vendor/xiaomi/msm8953-common',
]

blob_fixups: blob_fixups_user_type = {
    ('product/etc/permissions/vendor.qti.hardware.data.connection-V1.0-java.xml', 'product/etc/permissions/vendor.qti.hardware.data.connection-V1.1-java.xml'): blob_fixup()
        .regex_replace('/system/etc/camera/', '/vendor/etc/camera/'),
    'vendor/lib64/libvendor.goodix.hardware.fingerprint@1.0-service.so': blob_fixup()
        .remove_needed('libprotobuf-cpp-lite.so'),
    'vendor/lib64/libvendor.goodix.hardware.fingerprint@1.0.so': blob_fixup()
        .replace_needed('libhidlbase.so', 'libhidlbase-v32.so'),
    ('vendor/lib/libmmcamera_hdr_gb_lib.so', 'vendor/lib64/libgf_algo.so', 'vendor/lib64/libgf_ca.so', 'vendor/lib64/libgf_hal.so', 'vendor/lib64/libgoodixfingerprintd_binder.so'): blob_fixup()
        .replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
    'vendor/lib/libmmcamera_tuning.so': blob_fixup()
        .remove_needed('libmm-qcamera.so'),
    'vendor/lib64/libgoodixfingerprintd_binder.so': blob_fixup()
        .remove_needed('ld-android.so')
        .remove_needed('libbacktrace.so')
        .remove_needed('libunwind.so')
        .remove_needed('libkeystore_binder.so')
        .remove_needed('libsoftkeymasterdevice.so')
        .remove_needed('libsoftkeymaster.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'tissot',
    'xiaomi',
    blob_fixups=blob_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'msm8953-common', module.vendor
    )
    utils.run()
