import SwiftUI

struct MembershipView: View {
    var body: some View {
        VStack(alignment: .leading, spacing: 10) {
            Text("Join TIDE Plus")
                .font(.system(size: 20, weight: .medium))
                .foregroundStyle(Color("TideText"))
            VStack(spacing: 0) {
                HStack(alignment: .firstTextBaseline, spacing: 5) {
                    Text("TIDE")
                        .font(.system(size: 24, weight: .medium))
                    Text("Plus")
                        .font(.custom("SnellRoundhand", size: 31))
                }
                .padding(.top, 44)
                Text("Enjoy exclusive premium content and\nadvanced features across all\nplatforms.")
                    .font(.system(size: 14, weight: .medium))
                    .multilineTextAlignment(.center)
                    .padding(.top, 6)
                Text("Learn More")
                    .font(.system(size: 15, weight: .medium))
                    .foregroundStyle(Color(red: 0.65, green: 0.56, blue: 0.5))
                    .frame(width: 181, height: 45)
                    .background(.white.opacity(0.75))
                    .clipShape(Capsule())
                    .padding(.top, 24)
                Spacer(minLength: 0)
            }
            .foregroundStyle(.white)
            .frame(maxWidth: .infinity)
            .frame(height: 244)
            .background(LinearGradient(colors: [Color(red: 0.72, green: 0.73, blue: 0.79),
                                               Color(red: 0.78, green: 0.75, blue: 0.78),
                                               Color(red: 0.85, green: 0.76, blue: 0.66)],
                                       startPoint: .top, endPoint: .bottom))
            .clipShape(RoundedRectangle(cornerRadius: 19))
            .overlay(RoundedRectangle(cornerRadius: 19).stroke(.white.opacity(0.5), lineWidth: 0.7))
        }
        .padding(.horizontal, 22)
    }
}

struct LibraryView: View {
    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            Text("Library")
                .font(.system(size: 19, weight: .medium))
                .foregroundStyle(Color("TideText"))
            HStack(spacing: 12) {
                LibraryTileView(title: "Meditation", artwork: "library-meditation")
                LibraryTileView(title: "Soundscape", artwork: "library-soundscape")
            }
        }
        .padding(.horizontal, 22)
    }
}

struct LibraryTileView: View {
    let title: String
    let artwork: String

    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            Image(artwork)
                .resizable()
                .scaledToFit()
                .frame(width: 69, height: 58)
                .frame(maxWidth: .infinity, alignment: .trailing)
            Spacer()
            Text(title)
                .font(.system(size: 14, weight: .medium))
                .foregroundStyle(Color("TideText"))
        }
        .padding(10)
        .frame(maxWidth: .infinity)
        .frame(height: 112)
        .background(Color("TideTile"))
        .clipShape(RoundedRectangle(cornerRadius: 15))
    }
}
