'use client'

import { useChat } from '@ai-sdk/react'
import { Input } from '@codegouvfr/react-dsfr/Input'
import { Button } from '@codegouvfr/react-dsfr/Button'
import { Box, Container } from '@mui/material'

export default function Page() {
  const { messages, input, handleInputChange, handleSubmit } = useChat({
    api: 'http://localhost:8000/chat'
  })

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
        <form onSubmit={handleSubmit} style={{ flex: 1 }}>
          <Input
            label="Comment puis-je vous aider ?"
            nativeTextAreaProps={{
              value: input,
              onChange: handleInputChange
            }}
            textArea
          />
          <Button type="submit">Envoyer</Button>
        </form>
      </Box>
    </Container>
  )
}
