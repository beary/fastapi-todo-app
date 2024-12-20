import { createApi, type BaseQueryFn } from '@reduxjs/toolkit/query/react'
import axios, {
  AxiosError,
  type AxiosRequestConfig,
  HttpStatusCode,
} from 'axios'

export const agent = axios.create({
  baseURL: '/api',
})

agent.interceptors.response.use(
  response => response,
  (error: AxiosError) => {
    if (
      [HttpStatusCode.Forbidden, HttpStatusCode.Unauthorized].includes(
        error.response?.status ?? -1
      ) &&
      !error.request?.responseURL.endsWith('/login') &&
      !error.request?.responseURL.endsWith('/register')
    ) {
      console.warn('🍉🍉🍉redirecting to signin', error.request?.responseURL)
      location.pathname = '/signin'
    }
    return Promise.reject(error)
  }
)

const axiosBaseQuery: BaseQueryFn<
  AxiosRequestConfig,
  unknown,
  AxiosError
> = async (config: AxiosRequestConfig) => {
  try {
    const result = await agent.request({ ...config })
    return { data: result.data }
  } catch (error: any) {
    return { error }
  }
}

export const AppApi = createApi({
  baseQuery: axiosBaseQuery,
  endpoints: () => ({}),
})
