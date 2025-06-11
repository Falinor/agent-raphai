import { DsfrHead, getHtmlAttributes } from '@/dsfr-bootstrap/server-only-index'
import { DsfrProvider, StartDsfrOnHydration } from '@/dsfr-bootstrap/index'
import { AppRouterCacheProvider } from '@mui/material-nextjs/v13-appRouter'
import CustomThemeProvider from '@/dsfr-bootstrap/ThemeProvider'

export default function RootLayout({
  children
}: {
  children: React.JSX.Element
}) {
  const lang = undefined // Can be "fr" or "en" ...
  return (
    <html {...getHtmlAttributes({ lang })}>
      <head>
        <DsfrHead
          preloadFonts={[
            //"Marianne-Light",
            //"Marianne-Light_Italic",
            'Marianne-Regular',
            //"Marianne-Regular_Italic",
            'Marianne-Medium',
            //"Marianne-Medium_Italic",
            'Marianne-Bold'
            //"Marianne-Bold_Italic",
            //"Spectral-Regular",
            //"Spectral-ExtraBold"
          ]}
        />
      </head>
      <body>
        <AppRouterCacheProvider>
          <DsfrProvider lang={lang}>
            <CustomThemeProvider>
              <StartDsfrOnHydration />
              {children}
            </CustomThemeProvider>
          </DsfrProvider>
        </AppRouterCacheProvider>
      </body>
    </html>
  )
}
