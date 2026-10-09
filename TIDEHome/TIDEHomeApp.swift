import SwiftUI

@main
struct TIDEHomeApp: App {
    var body: some Scene {
        WindowGroup {
            TideHomeView()
                .statusBarHidden(true)
                .persistentSystemOverlays(.hidden)
        }
    }
}
