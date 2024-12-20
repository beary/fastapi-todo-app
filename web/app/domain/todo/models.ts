import type { TodoStatus } from './enums'

export interface ITodo {
  id: string
  title: string
  status: TodoStatus
  createdAt: string
  updatedAt: string
}
