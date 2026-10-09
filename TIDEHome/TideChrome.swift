import SwiftUI

struct TideHeaderView: View {
    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            ReferenceStatusBarView()
                .padding(.top, 18)
                .padding(.bottom, 34)
            HStack {
                Text("Good day")
                    .font(.system(size: 28, weight: .semibold))
                    .tracking(-0.5)
                Spacer()
                HStack(spacing: 16) {
                    Image(systemName: "speaker.slash")
                    Image(systemName: "square.grid.2x2")
                }
                .font(.system(size: 15, weight: .medium))
                .frame(width: 85, height: 36)
                .background(.ultraThinMaterial)
                .clipShape(Capsule())
                .overlay(Capsule().stroke(.white.opacity(0.2), lineWidth: 0.7))

                ZStack(alignment: .topTrailing) {
                    Text("心哲")
                        .font(.system(size: 15))
                        .foregroundStyle(.white)
                        .frame(width: 37, height: 37)
                        .background(LinearGradient(colors: [.purple, Color(red: 0.55, green: 0, blue: 0.68)],
                                                   startPoint: .topTrailing, endPoint: .bottomLeading))
                        .clipShape(Circle())
                    Circle()
                        .fill(.red)
                        .frame(width: 7, height: 7)
                }
                .padding(.leading, 6)
            }
            .padding(.horizontal, 19)

            HStack(spacing: 0) {
                WeekdayView(letter: "S", color: Color("TideSecondary"))
                WeekdayView(letter: "M", color: Color("TideSecondary"))
                WeekdayView(letter: "T", color: Color("TideSecondary"))
                WeekdayView(letter: "W", color: Color("TideSecondary"))
                WeekdayView(letter: "T", color: Color("TideSecondary"))
                WeekdayView(letter: "F", color: Color("TideText"))
                WeekdayView(letter: "S", color: Color("TideSecondary"))
            }
            .padding(.leading, 16)
            .padding(.top, 8)
        }
        .foregroundStyle(Color("TideText"))
        .frame(maxWidth: .infinity, alignment: .leading)
        .padding(.bottom, 23)
        .background(
            VStack(spacing: 0) {
                Color("TideHeader")
                LinearGradient(colors: [Color("TideHeader"), Color("TideHeader").opacity(0)],
                               startPoint: .top, endPoint: .bottom)
                    .frame(height: 20)
            }
        )
        .allowsHitTesting(false)
    }
}

struct WeekdayView: View {
    let letter: String
    let color: Color

    var body: some View {
        Text(letter)
            .font(.system(size: 11, weight: .medium))
            .foregroundStyle(color)
            .fixedSize()
            .frame(width: 18, height: 15)
    }
}

// 固定的狀態列，只用來模仿參考圖。
struct ReferenceStatusBarView: View {
    var body: some View {
        HStack(spacing: 3) {
            Text("18:25")
                .font(.system(size: 18, weight: .semibold))
            Image(systemName: "moon.fill")
                .font(.system(size: 14))
            Spacer()
            Image(systemName: "cellularbars")
                .font(.system(size: 15))
            Text("5G")
                .font(.system(size: 14, weight: .medium))
            Text("88")
                .font(.system(size: 12, weight: .bold))
                .foregroundStyle(Color("TideBackground"))
                .frame(width: 24, height: 14)
                .background(Color("TideText"))
                .clipShape(RoundedRectangle(cornerRadius: 4))
        }
        .padding(.horizontal, 44)
    }
}
