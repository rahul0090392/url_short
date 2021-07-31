from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from shortner.constants import ERROR, SUCCESS, INTERNAL_ERROR, RECORD_NOT_FOUND
from shortner.dtos import ValidateShortenURLParams, ValidateShortenURLID
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
                result = FileDbManager.add_record(url=params.data["url"])

            return Response(
                data={
                    "status": SUCCESS,
                    "shorten_url": result["data"]["shorten_url"],
                    "actual_url": result["data"]["actual_url"],
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            print(e)
            return Response(
                data={"status": ERROR, "message": INTERNAL_ERROR},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class ShortenURLResolveView(APIView):
    def get(self, request, shorten_path):
        try:
            params = ValidateShortenURLID(data={"shorten_path": shorten_path})
            if not params.is_valid():
                return Response(
                    data={
                        "status": ERROR,
                        "details": params.errors,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            result = FileDbManager.get_record_by_id(shorten_path)
            if result["status"] == ERROR:
                return Response(
                    data={"status": ERROR, "message": RECORD_NOT_FOUND},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            return Response(
                data={"status": SUCCESS, "actual_url": result["data"]["actual_url"]},
                status=status.HTTP_200_OK,
            )
        except Exception:
            return Response(
                data={"status": ERROR, "message": INTERNAL_ERROR},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
