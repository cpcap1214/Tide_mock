import SwiftUI

// 相同卡片傳入不同的 property，就能顯示不同內容。
struct MeditationCardView: View {
    let artwork: String
    let title: String
    let detail: String
    var badge = ""
    var badgeOpacity = 0.0

    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            ZStack(alignment: .topTrailing) {
                Image(artwork)
                    .resizable()
                    .scaledToFill()
                    .frame(width: 162, height: 162)
                    .clipShape(RoundedRectangle(cornerRadius: 14))
                    .overlay(RoundedRectangle(cornerRadius: 14).stroke(.white.opacity(0.18), lineWidth: 0.7))
                Text(badge)
                    .font(.system(size: 8))
                    .foregroundStyle(.white)
                    .padding(4)
                    .background(.ultraThinMaterial)
                    .clipShape(RoundedRectangle(cornerRadius: 3))
                    .padding(9)
                    .opacity(badgeOpacity)
            }
            Text(title)
                .font(.system(size: 14))
                .foregroundStyle(Color("TideText"))
                .lineLimit(1)
                .padding(.top, 7)
            Text(detail)
                .font(.system(size: 10))
                .foregroundStyle(Color("TideSecondary"))
                .lineLimit(1)
                .padding(.top, 3)
        }
        .frame(width: 162, alignment: .leading)
    }
}

struct SectionTitleView: View {
    let title: String

    var body: some View {
        HStack {
            Text(title)
                .font(.system(size: 19, weight: .medium))
                .tracking(-0.3)
            Spacer()
            Image(systemName: "chevron.right")
                .font(.system(size: 13))
        }
        .foregroundStyle(Color("TideText"))
        .padding(.horizontal, 22)
    }
}

struct QuickActionView: View {
    let title: String
    let icon: String

    var body: some View {
        VStack(alignment: .leading, spacing: 14) {
            Image(systemName: icon)
                .font(.system(size: 17))
                .foregroundStyle(Color("TideText"))
            Text(title)
                .font(.system(size: 14))
                .foregroundStyle(Color("TideText").opacity(0.65))
        }
        .frame(width: 112, height: 78, alignment: .leading)
        .padding(.horizontal, 15)
        .background(Color("TideQuick").gradient)
        .clipShape(RoundedRectangle(cornerRadius: 18))
        .overlay(RoundedRectangle(cornerRadius: 18).stroke(.white.opacity(0.25), lineWidth: 0.7))
    }
}

struct CategoryChipView: View {
    let title: String
    let width: CGFloat

    var body: some View {
        Text(title)
            .font(.system(size: 12, weight: .medium))
            .foregroundStyle(Color("TideText"))
            .frame(width: width, height: 34)
            .background(Color("TideChip"))
            .clipShape(Capsule())
    }
}
