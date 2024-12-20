export interface IResult<DataT> {
  code: number
  data: DataT
}

export type IListResult<DataT> = IResult<{
  data: DataT[]
  total: number
}>
