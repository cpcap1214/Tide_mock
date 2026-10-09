import SwiftUI

struct TideHomeView: View {
    var body: some View {
        ZStack(alignment: .top) {
            Color("TideBackground")
                .ignoresSafeArea()

            ScrollView(.vertical, showsIndicators: false) {
                VStack(alignment: .leading, spacing: 0) {
                    QuickActionsView()
                        .padding(.top, 162)
                    DailyQuoteView()
                        .padding(.top, 38)
                    CategoryChipsView()
                        .padding(.top, 36)
                    QuietMindView()
                        .padding(.top, 36)
                    StressReliefView()
                        .padding(.top, 34)
                    BetterFocusView()
                        .padding(.top, 34)
                    MembershipView()
                        .padding(.top, 34)
                    LibraryView()
                        .padding(.top, 34)
                    Text("[A mindful space for you.](https://tide.fm/)")
                        .font(.custom("TimesNewRomanPS-ItalicMT", size: 12))
                        .tint(Color("TideText"))
                        .frame(maxWidth: .infinity)
                        .padding(.top, 56)
                        .padding(.bottom, 28)
                }
            }
            TideHeaderView()
        }
        .ignoresSafeArea()
    }
}

#Preview("Dark") {
    TideHomeView()
        .preferredColorScheme(.dark)
}

#Preview("Light") {
    TideHomeView()
        .preferredColorScheme(.light)
}
