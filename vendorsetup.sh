rm -rf hardware/sony/timekeep
rm -rf hardware/lineage/compat
rm -rf hardware/qcom-caf/wlan
rm -rf hardware/qcom-caf/msm8996/display

git clone https://github.com/LineageOS/android_hardware_sony_timekeep.git -b lineage-22.0 hardware/sony/timekeep
git clone https://github.com/Lafactorial/android_hardware_lineage_compat.git -b lineage-22.0 hardware/lineage/compat
git clone https://github.com/Lafactorial/android_hardware_qcom_wlan -b lineage-22.1-caf hardware/qcom-caf/wlan
git clone https://github.com/plrine/android_hardware_qcom_display.git -b lineage-22.0-caf-msm8996 hardware/qcom-caf/msm8996/display
