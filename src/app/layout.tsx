import { getHtmlAttributes, DsfrHead } from "../dsfr-bootstrap/server-only-index";
import { DsfrProvider } from "../dsfr-bootstrap";

export default function RootLayout({ children }: { children: React.JSX.Element; }) {
  const lang = undefined; // Can be "fr" or "en" ...
  return (
    <html {...getHtmlAttributes({ lang })} >
    <head>
      <DsfrHead
        preloadFonts={[
          //"Marianne-Light",
          //"Marianne-Light_Italic",
          "Marianne-Regular",
          //"Marianne-Regular_Italic",
          "Marianne-Medium",
          //"Marianne-Medium_Italic",
          "Marianne-Bold"
          //"Marianne-Bold_Italic",
          //"Spectral-Regular",
          //"Spectral-ExtraBold"
        ]}
        />
    </head>
    <body>
    <DsfrProvider lang={lang}>
      {children}
    </DsfrProvider>
    </body>
    </html>
  );
}
