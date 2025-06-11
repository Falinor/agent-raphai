import { Input } from '@codegouvfr/react-dsfr/Input'
import { Box, Container } from '@mui/material'

export default function Page() {
  return (
    <Container>
      <Box
        sx={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          height: '100vh'
        }}
      >
        <Input
          label="Comment puis-je vous aider ?"
          textArea
          style={{ width: '100%' }}
        />
      </Box>
    </Container>
  )
}
