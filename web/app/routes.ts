import { type RouteConfig, index, route } from '@react-router/dev/routes'

const routes: RouteConfig = [
  index('routes/home.tsx'),
  route('signin', 'routes/signin.tsx'),
  route('signup', 'routes/signup.tsx'),
]

export default routes
