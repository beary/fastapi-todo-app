import { configureStore } from '@reduxjs/toolkit'
import { AppApi } from './api'

export const store = configureStore({
  reducer: {
    [AppApi.reducerPath]: AppApi.reducer,
  },
  middleware: getDefaultMiddleware =>
    getDefaultMiddleware().concat(AppApi.middleware),
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch
