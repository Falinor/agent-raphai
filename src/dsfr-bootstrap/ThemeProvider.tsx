'use client'

import MuiDsfrThemeProvider from '@codegouvfr/react-dsfr/mui'
import { ReactNode } from 'react'

interface CustomThemeProviderProps {
  children: ReactNode
}

export default function CustomThemeProvider({
  children
}: CustomThemeProviderProps) {
  return <MuiDsfrThemeProvider>{children}</MuiDsfrThemeProvider>
}
