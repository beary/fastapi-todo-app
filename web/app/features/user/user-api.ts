import { AppApi } from '~/shared/api'
import type { IUser } from '~/domain/user/models'
import type { ISigninRequest, ISignupRequest } from './user-request'

const userApi = AppApi.injectEndpoints({
  overrideExisting: false,
  endpoints: builder => ({
    whoami: builder.query<IUser, void>({
      query: () => ({
        url: '/user/whoami',
        method: 'GET',
      }),
    }),
    login: builder.mutation<IUser, ISigninRequest>({
      query: body => ({
        url: '/user/login',
        method: 'POST',
        data: body,
      }),
    }),
    register: builder.mutation<IUser, ISignupRequest>({
      query: body => ({
        url: '/user/register',
        method: 'POST',
        data: body,
      }),
    }),
  }),
})

export const { useWhoamiQuery, useLoginMutation, useRegisterMutation } = userApi
