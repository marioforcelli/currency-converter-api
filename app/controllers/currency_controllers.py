from app.application.convert_amount_service import ConvertAmountService
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.application.get_currency_service import GetCurrencyService
import app.core.CurrencyRequest as CurrencyRequest

currency_router = APIRouter()


@currency_router.get("/")
async def root():
    return {"message": "Hello World"}


@currency_router.get("/get_currency")
async def get_currency(request: CurrencyRequest.CurrencyRequest = Depends()):
    currency_service = GetCurrencyService()
    print(request)

    try:
        result = currency_service.get_currency(
            currency_id_to=request.currency_id_to,
            amount=request.amount,
            currency_id_from=request.currency_id_from,
        )
        return JSONResponse(content=result, status_code=200)
    except ValueError as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    except Exception as e:
        return JSONResponse(
            content={"error": "An unexpected error occurred: " + str(e)},
            status_code=500,
        )


@currency_router.get("/convert_amount")
async def convert_amount(request: CurrencyRequest.CurrencyRequest = Depends()):
    convert_amount_service = ConvertAmountService()
    try:
        result = convert_amount_service.convert_amount(
            currency_id_to=request.currency_id_to,
            amount=request.amount,
            currency_id_from=request.currency_id_from,
        )

        return JSONResponse(content=result, status_code=200)
    except ValueError as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    except Exception as e:
        return JSONResponse(
            content={"error": "An unexpected error occurred: " + str(e)},
            status_code=500,
        )
