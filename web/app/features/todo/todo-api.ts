import type { ITodo } from '~/domain/todo/models'
import { AppApi } from '~/shared/api'
import type { IListResult } from '~/shared/types'
import type { ICreateTodoRequest } from './todo-request'
import type { TodoStatus } from '~/domain/todo/enums'

const todoApi = AppApi.injectEndpoints({
  overrideExisting: false,
  endpoints: builder => ({
    getTodoList: builder.query<IListResult<ITodo>, void>({
      query: () => ({
        url: '/todo/list',
        method: 'GET',
      }),
    }),
    createTodo: builder.mutation<void, ICreateTodoRequest>({
      query: body => ({
        url: '/todo/create',
        method: 'POST',
        data: body,
      }),
    }),
    processTodo: builder.mutation<void, { id: string; status: TodoStatus }>({
      query: body => ({
        url: `/todo/process/${body.id}`,
        method: 'POST',
        data: { status: body.status },
      }),
    }),
    deleteTodo: builder.mutation<void, string>({
      query: todoId => ({
        url: `/todo/delete/${todoId}`,
        method: 'DELETE',
      }),
    }),
  }),
})

export const {
  useGetTodoListQuery,
  useCreateTodoMutation,
  useProcessTodoMutation,
  useDeleteTodoMutation,
} = todoApi
