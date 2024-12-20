import { useEffect, type FC } from 'react'
import { useForm } from 'react-hook-form'
import { Link as RouterLink, useNavigate } from 'react-router'
import { Alert, Box, Button, Link, TextField, Typography } from '@mui/material'
import { Paper } from '@mui/material'
import { Container } from '@mui/material'
import { useRegisterMutation } from '~/features/user/user-api'
import type { Route } from './+types/signup'

interface SignUpForm {
  username: string
  password: string
}

const Signup: FC<Route.ComponentProps> = () => {
  const { register, handleSubmit } = useForm<SignUpForm>()
  const [registerFn, { isLoading, error, data }] = useRegisterMutation()
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
          onSubmit={handleSubmit(registerFn)}
          sx={{
            display: 'flex',
            flexDirection: 'column',
            gap: 2,
            justifyContent: 'center',
            alignItems: 'center',
          }}
        >
          <Typography variant="h6" color="primary" component="h1">
            Sign Up
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
            Sign Up
          </Button>
          <Typography variant="body2" color="text.secondary">
            Already have an account?{' '}
            <Link to="/signin" component={RouterLink}>
              Sign in
            </Link>
          </Typography>
        </Box>
      </Paper>
    </Container>
  )
}

export default Signup
