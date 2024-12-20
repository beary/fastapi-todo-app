import { Fragment, type FC } from 'react'
import type { Route } from './+types/home'
import {
  useGetTodoListQuery,
  useCreateTodoMutation,
  useProcessTodoMutation,
  useDeleteTodoMutation,
} from '~/features/todo/todo-api'
import {
  Button,
  Container,
  Typography,
  List,
  ListItem,
  Paper,
  Toolbar,
  AppBar,
  Box,
  Chip,
  ListItemText,
  Divider,
} from '@mui/material'
import { TodoStatus } from '~/domain/todo/enums'

const Home: FC<Route.ComponentProps> = () => {
  const { data, refetch } = useGetTodoListQuery()
  const [createTodo] = useCreateTodoMutation()
  const [processTodo] = useProcessTodoMutation()
  const [deleteTodo] = useDeleteTodoMutation()
  const handleCreateTodo = async () => {
    const title = prompt('What you want to do?')?.trim()
    if (title) {
      await createTodo({ title })
      await refetch()
    }
  }

  const handleProcessTodo = async (id: string, status: TodoStatus) => {
    await processTodo({ id, status })
    await refetch()
  }
  const handleDeleteTodo = async (id: string) => {
    await deleteTodo(id)
    await refetch()
  }
  return (
    <Container maxWidth="xs">
      <Paper variant="elevation" sx={{ overflow: 'hidden' }}>
        <AppBar position="static" elevation={0}>
          <Toolbar variant="dense">
            <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
              Todo List
            </Typography>
            <Button
              variant="outlined"
              color="inherit"
              size="small"
              onClick={handleCreateTodo}
            >
              Add
            </Button>
          </Toolbar>
        </AppBar>
        {data?.data.total !== 0 ? (
          <List dense>
            {data?.data.data.map(todo => (
              <Fragment key={todo.id}>
                <ListItem
                  secondaryAction={
                    <Fragment>
                      {todo.status === TodoStatus.TODO && (
                        <Button
                          size="small"
                          color="primary"
                          onClick={() =>
                            handleProcessTodo(todo.id, TodoStatus.IN_PROGRESS)
                          }
                        >
                          start
                        </Button>
                      )}
                      {todo.status === TodoStatus.IN_PROGRESS && (
                        <Button
                          size="small"
                          color="success"
                          onClick={() =>
                            handleProcessTodo(todo.id, TodoStatus.DONE)
                          }
                        >
                          done
                        </Button>
                      )}
                      {todo.status === TodoStatus.DONE && (
                        <Button
                          size="small"
                          color="error"
                          onClick={() => handleDeleteTodo(todo.id)}
                        >
                          delete
                        </Button>
                      )}
                    </Fragment>
                  }
                >
                  {todo.status === TodoStatus.TODO && (
                    <ListItemText
                      primary={
                        <Typography color="text.secondary">
                          {todo.title}
                        </Typography>
                      }
                      secondary={
                        <Chip size="small" label="todo" color="default" />
                      }
                    />
                  )}
                  {todo.status === TodoStatus.IN_PROGRESS && (
                    <ListItemText
                      primary={
                        <Typography color="primary">{todo.title}</Typography>
                      }
                      secondary={
                        <Chip
                          size="small"
                          label="in progress"
                          color="primary"
                        />
                      }
                    />
                  )}
                  {todo.status === TodoStatus.DONE && (
                    <ListItemText
                      primary={
                        <Typography color="text.secondary">
                          {todo.title}
                        </Typography>
                      }
                      secondary={
                        <Chip size="small" label="done" color="success" />
                      }
                    />
                  )}
                </ListItem>
                <Divider
                  sx={{ '&:last-child': { display: 'none' } }}
                  variant="fullWidth"
                  component="li"
                />
              </Fragment>
            ))}
          </List>
        ) : (
          <Box sx={{ p: 2, display: 'flex', justifyContent: 'center' }}>
            <Typography variant="body1" color="text.secondary">
              No todos yet
            </Typography>
          </Box>
        )}
      </Paper>
    </Container>
  )
}

export default Home
