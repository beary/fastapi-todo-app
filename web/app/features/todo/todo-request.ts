import type { TodoStatus } from '~/domain/todo/enums'

export interface ICreateTodoRequest {
  title: string
}

export interface IProcessTodoRequest {
  status: TodoStatus
}
