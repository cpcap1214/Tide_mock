# TIDE Home · SwiftUI 課堂作業

模仿 TIDE 首頁的 prototype。保留垂直與水平捲動，底部導覽列已移除。頁底文字可開啟 TIDE 官網，其餘卡片維持靜態展示。

## 開啟

開啟 `TIDEHome.xcodeproj`，選擇 TIDEHome scheme 與 iPhone Simulator，按 Run。也可執行 `./Tools/build-on-mac.sh`。

畫面會依系統外觀顯示淺色或深色。`TideHomeView.swift` 最下方有兩種 Xcode Preview。本機備份、文章草稿及編譯產物不包含在 repository 中。

## 六項必做要求

| 要求 | 實作位置 |
| --- | --- |
| VStack、HStack、ZStack、Text、Image、ScrollView | 主畫面、頂列、卡片與分類區塊皆使用基本元件 |
| asset 和 SF Symbol 圖片 | `MeditationCardView` 的 `Image(artwork)`；`QuickActionView` 的 `Image(systemName: icon)` |
| 多個 modifier | font、foregroundStyle、frame、padding、background、clipShape、overlay、opacity 等 |
| 可上下捲動 | `TideHomeView` 的垂直 ScrollView；另有水平卡片列 |
| 多檔案定義 View | 下列六個 Swift 檔案 |
| property 客製 View | `MeditationCardView`、`QuickActionView`、`WeekdayView`、`LibraryTileView` 等 |

## 檔案與閱讀順序

1. `TIDEHomeApp.swift`：App 的入口。
2. `TideHomeView.swift`：用 VStack 從上到下排列整個首頁。
3. `TideChrome.swift`：固定頂列、星期與靜態狀態列。
4. `TideCards.swift`：傳入標題、圖片名稱等 property 的共用元件。
5. `TideSections.swift`：快捷卡、每日引言、分類與三組冥想卡片。
6. `TideMembership.swift`：會員卡與 Library。

例如 `MeditationCardView(artwork: "annoyance", title: "Annoyance", detail: "5-15 min · Meditation")` 就是教材的 property 客製 View 寫法。`badge` 和 `badgeOpacity` 有預設值，只有 Free 卡片需要傳入其他值。
