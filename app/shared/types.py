from dataclasses import dataclass
from typing import Generic, TypeVar

import fastapi

DataT = TypeVar("DataT")
T = TypeVar("T")


@dataclass(slots=True)
class Result(Generic[DataT]):
    code: int
    data: DataT

    @staticmethod
    def new(
        data: T,
        status_code: int = fastapi.status.HTTP_200_OK,
    ) -> "Result[T]":
        return Result(
            code=status_code,
            data=data,
        )


@dataclass(slots=True)
class ListResult(Generic[DataT]):
    data: list[DataT]
    total: int

    @staticmethod
    def new(
        data: list[T],
        total: int | None = None,
        status_code: int = fastapi.status.HTTP_200_OK,
    ) -> "Result[ListResult[T]]":
        return Result(
            code=status_code,
            data=ListResult(data=data, total=total or len(data)),
        )
