import type { Metadata } from "next";
import "./style.css";
export const metadata: Metadata = {
  title: "Soedirman Strava Challenge",
  description: "Leaderboard Soedirman Runners Challenge 2–30 November 2026"
};
export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="id"><body>{children}</body></html>;
}
