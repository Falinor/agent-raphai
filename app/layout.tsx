import './globals.css';
import type { Metadata } from 'next';
import { DsfrHead } from "@codegouvfr/react-dsfr/next-appdir/DsfrHead";
import { DsfrProvider } from "@codegouvfr/react-dsfr/next-appdir/DsfrProvider";
import { getHtmlAttributes } from "@codegouvfr/react-dsfr/next-appdir/getHtmlAttributes";
import { startReactDsfr } from "@codegouvfr/react-dsfr/next-appdir";
import Link from "next/link";

declare module "@codegouvfr/react-dsfr/next-appdir" {
    interface RegisterLink {
        Link: typeof Link;
    }
}

startReactDsfr({ 
    defaultColorScheme: "system",
    Link
});

export const metadata: Metadata = {
  title: 'Assistant IA - République Française',
  description: 'Interface de chat IA moderne utilisant le système de design de l\'État français',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html {...getHtmlAttributes({ defaultColorScheme: "system" })}>
      <head>
        <DsfrHead
          Link={Link}
          preloadFonts={[
            "Marianne-Light",
            "Marianne-Light_Italic",
            "Marianne-Regular",
            "Marianne-Regular_Italic",
            "Marianne-Medium",
            "Marianne-Medium_Italic",
            "Marianne-Bold",
            "Marianne-Bold_Italic",
            "Spectral-Regular",
            "Spectral-ExtraBold"
          ]}
        />
      </head>
      <body>
        <DsfrProvider>
          {children}
        </DsfrProvider>
      </body>
    </html>
  );
}