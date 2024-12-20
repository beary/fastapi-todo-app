import type { Gender } from './enums'

export interface IUser {
  id: string
  username: string
  nickname: string
  gender?: Gender
  birthday?: string
  age?: number
  email?: string
  phone?: string
  avatar: string
  description?: string
  createdAt: string
  updatedAt: string
}
