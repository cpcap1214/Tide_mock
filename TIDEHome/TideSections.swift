import SwiftUI

struct QuickActionsView: View {
    var body: some View {
        ScrollView(.horizontal, showsIndicators: false) {
            HStack(spacing: 12) {
                QuickActionView(title: "Breathwork", icon: "leaf")
                QuickActionView(title: "Focus Timer", icon: "record.circle")
                QuickActionView(title: "Sleep Tracker", icon: "moon.zzz")
                QuickActionView(title: "Quick Nap", icon: "moon")
            }
            .padding(.horizontal, 22)
        }
    }
}

struct DailyQuoteView: View {
    var body: some View {
        HStack {
            VStack(alignment: .leading, spacing: 6) {
                Text("Oct 9th")
                    .font(.system(size: 12))
                    .foregroundStyle(Color("TideSecondary"))
                Text("Be yourself; everyone else is\nalready taken.")
                    .font(.system(size: 16))
                    .lineSpacing(4)
                    .foregroundStyle(Color("TideText"))
                Text("Author, Oscar Wilde")
                    .font(.system(size: 12))
                    .foregroundStyle(Color("TideSecondary"))
            }
            Spacer()
            Circle()
                .fill(LinearGradient(colors: [Color(red: 0.15, green: 0.46, blue: 0.49),
                                              Color(red: 0.26, green: 0.68, blue: 0.69)],
                                     startPoint: .leading, endPoint: .trailing))
                .frame(width: 51, height: 51)
        }
        .padding(.horizontal, 22)
    }
}

struct CategoryChipsView: View {
    var body: some View {
        ScrollView(.horizontal, showsIndicators: false) {
            VStack(alignment: .leading, spacing: 12) {
                HStack(spacing: 11) {
                    CategoryChipView(title: "✨ Daily Meditation", width: 139)
                    CategoryChipView(title: "◻️ Sleep", width: 80)
                    CategoryChipView(title: "📖 Improve Focus", width: 131)
                }
                HStack(spacing: 11) {
                    CategoryChipView(title: "💨 Breathwork", width: 112)
                    CategoryChipView(title: "🌿 Emotion Regulation", width: 158)
                    CategoryChipView(title: "🐤 Reduce Stress", width: 124)
                }
            }
            .padding(.horizontal, 22)
        }
    }
}

struct QuietMindView: View {
    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            SectionTitleView(title: "Quiet the Mind")
            ScrollView(.horizontal, showsIndicators: false) {
                HStack(alignment: .top, spacing: 15) {
                    MeditationCardView(artwork: "annoyance", title: "Annoyance", detail: "5-15 min · Meditation")
                    MeditationCardView(artwork: "exhaustion", title: "Exhaustion", detail: "5-20 min · Meditation", badge: "Free", badgeOpacity: 1)
                    MeditationCardView(artwork: "sadness", title: "Sadness", detail: "5-15 min · Meditation")
                }
                .padding(.horizontal, 22)
            }
        }
    }
}

struct StressReliefView: View {
    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            SectionTitleView(title: "Daytime Stress Relief")
            ScrollView(.horizontal, showsIndicators: false) {
                HStack(alignment: .top, spacing: 15) {
                    MeditationCardView(artwork: "mind-detox", title: "Mind Detox", detail: "10 min · Meditation")
                    MeditationCardView(artwork: "let-go", title: "Let Go of Thoughts", detail: "10 min · Meditation")
                    MeditationCardView(artwork: "panic", title: "Panic", detail: "10 min · Meditation")
                }
                .padding(.horizontal, 22)
            }
        }
    }
}

struct BetterFocusView: View {
    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            SectionTitleView(title: "Better Focus, Higher Efficiency")
            ScrollView(.horizontal, showsIndicators: false) {
                HStack(alignment: .top, spacing: 15) {
                    MeditationCardView(artwork: "before-study", title: "Before Study", detail: "5-10 min · Meditation")
                    MeditationCardView(artwork: "eye-strain", title: "Eye Strain", detail: "5-10 min · Meditation")
                    MeditationCardView(artwork: "steps", title: "Step by Step", detail: "10-20 min · Meditation")
                }
                .padding(.horizontal, 22)
            }
        }
    }
}
