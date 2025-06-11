'use client'

import { useChat } from '@ai-sdk/react'
import { Input } from '@codegouvfr/react-dsfr/Input'
import { Button } from '@codegouvfr/react-dsfr/Button'
import {
  Box,
  Card,
  CardContent,
  CardHeader,
  Container,
  LinearProgress,
  Stack,
  Typography
} from '@mui/material'
import Markdown from 'react-markdown'

export default function Page() {
  const { messages, status, input, handleInputChange, handleSubmit } = useChat({
    api: 'https://b443-2a04-cec0-1206-8048-1c34-9974-e18a-df21.ngrok-free.app/chat'
  })

  return (
    <Container>
      <Box
        sx={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          minHeight: '100vh',
          padding: 2
        }}
      >
        <Stack spacing={4} sx={{ width: '100%' }}>
          <form onSubmit={handleSubmit}>
            <Input
              label="Comment puis-je vous aider ?"
              nativeTextAreaProps={{
                value: input,
                onChange: handleInputChange
              }}
              textArea
            />
            <Button
              type="submit"
              disabled={status === 'streaming' || status === 'submitted'}
            >
              Envoyer
            </Button>
          </form>

          {status === 'streaming' || status === 'submitted' ? (
            <LinearProgress />
          ) : null}

          <Stack direction="column" spacing={2}>
            {messages.map((message) => (
              <Card key={message.id}>
                <CardHeader
                  title={role(message.role)}
                  subheader={
                    message.createdAt
                      ? formatDate(message.createdAt.toJSON())
                      : null
                  }
                />
                <CardContent>{parseContent(message.content)}</CardContent>
              </Card>
            ))}
          </Stack>
        </Stack>
      </Box>
    </Container>
  )
}

function role(role: string): string {
  switch (role) {
    case 'user':
      return 'Stéphanie'
    case 'assistant':
      return 'RaphIA'
    default:
      return 'Rôle inconnu'
  }
}

function parseContent(content: string) {
  return <Markdown>{content}</Markdown>
}

function formatDate(dateString: string): string {
  const date = new Date(dateString)
  return new Intl.DateTimeFormat('fr-FR', {
    dateStyle: 'medium',
    timeStyle: 'short'
  }).format(date)
}
