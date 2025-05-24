#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

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
    'vendor/lib/libmmcamera_tuning.so': blob_fixup()
        .remove_needed('libmm-qcamera.so'),
    'vendor/lib64/hw/gf_fingerprint.goodix.default.so': blob_fixup()
        .replace_needed('libvendor.goodix.hardware.fingerprint@1.0.so', 'vendor.goodix.hardware.fingerprint@1.0.so'),
    'vendor/lib64/libvendor.goodix.hardware.fingerprint@1.0-service.so': blob_fixup()
        .remove_needed('libprotobuf-cpp-lite.so')
        .replace_needed('libvendor.goodix.hardware.fingerprint@1.0.so', 'vendor.goodix.hardware.fingerprint@1.0.so'),
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
