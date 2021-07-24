from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from shortner.constants import ERROR, SUCCESS, INTERNAL_ERROR
from shortner.dtos import ValidateShortenURLParams
from shortner.fileservice import FileDbManager


class ShortenURLView(APIView):
    def post(self, request):
        try:
            params = ValidateShortenURLParams(data=request.data)
            if not params.is_valid():
                return Response(
                    data={
                        "status": ERROR,
                        "details": params.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            result = FileDbManager.get_record(url=params.data["url"])
            if result["status"] == ERROR:
                result = FileDbManager.add_record(
                    id=result["last"], url=params.data["url"]
                )

            return Response(
                data={"status": SUCCESS, "shorten_url": result["data"]["shorten_url"]},
                status=status.HTTP_200_OK,
            )
        except Exception:
            return Response(
                data={"status": ERROR, "message": INTERNAL_ERROR},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
