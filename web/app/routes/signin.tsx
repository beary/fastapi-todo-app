import { useEffect, type FC } from 'react'
import { useForm } from 'react-hook-form'
import { Link as RouterLink, useNavigate } from 'react-router'
import {
  Alert,
  Box,
  Button,
  Container,
  Link,
  Paper,
  TextField,
  Typography,
} from '@mui/material'
import type { Route } from './+types/signin'
import { useLoginMutation } from '~/features/user/user-api'

interface SignInForm {
  username: string
  password: string
}

const SignIn: FC<Route.ComponentProps> = () => {
  const { register, handleSubmit } = useForm<SignInForm>()
  const [login, { isLoading, error, data }] = useLoginMutation()
  const navigate = useNavigate()

  useEffect(() => {
    if (data) {
      navigate('/')
    }
  }, [data])

  return (
    <Container
      maxWidth="xs"
      sx={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: '100vh',
      }}
    >
      <Paper sx={{ p: 8, width: '100%' }}>
        <Box
          component="form"
          onSubmit={handleSubmit(login)}
          sx={{
            display: 'flex',
            flexDirection: 'column',
            gap: 2,
            justifyContent: 'center',
            alignItems: 'center',
          }}
        >
          <Typography variant="h6" color="primary" component="h1">
            Sign In
          </Typography>
          <TextField
            fullWidth
            label="Username"
            size="small"
            type="text"
            disabled={isLoading}
            {...register('username')}
          />
          <TextField
            fullWidth
            label="Password"
            size="small"
            type="password"
            disabled={isLoading}
            {...register('password')}
          />
          {error && (
            <Alert severity="error" sx={{ width: '100%' }}>
              {(error as any)?.response?.data?.message}
            </Alert>
          )}
          <Button
            variant="contained"
            fullWidth
            disabled={isLoading}
            type="submit"
            sx={{ mt: 2 }}
          >
            Sign In
          </Button>
          <Typography variant="body2" color="text.secondary">
            Don't have an account?{' '}
            <Link to="/signup" component={RouterLink}>
              Sign up
            </Link>
          </Typography>
        </Box>
      </Paper>
    </Container>
  )
}

export default SignIn
