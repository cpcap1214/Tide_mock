#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
if ! command -v xcodebuild >/dev/null 2>&1; then
  echo "需要安裝完整 Xcode，並將 Command Line Tools 指向 Xcode。" >&2
  exit 1
fi
xcodebuild -project TIDEHome.xcodeproj -scheme TIDEHome \
  -configuration Debug -sdk iphonesimulator \
  -destination 'generic/platform=iOS Simulator' \
  -derivedDataPath build/DerivedData CODE_SIGNING_ALLOWED=NO build
