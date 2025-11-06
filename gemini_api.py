import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일에서 환경변수 로드
# 지원되는 키 이름을 순서대로 확인합니다. 많은 예제/레포지토리에서
# `GEMINI_API_KEY` 또는 `GENAI_API_KEY`를 사용하므로 둘 다 허용합니다.
api_key = (
    os.getenv("GENAI_API_KEY")
    or os.getenv("GEMINI_API_KEY")
    or os.getenv("GEN_AI_API_KEY")
)

if not api_key:
    raise SystemExit(
        "환경변수 GENAI_API_KEY 또는 GEMINI_API_KEY가 설정되어 있지 않습니다. .env 또는 shell에서 설정하세요."
    )

import google.genai as genai  # 이미 설치되어 있어야 함

# API 키를 직접 전달해서 클라이언트 생성
client = genai.Client(api_key=api_key)

print("Client 생성 성공:", bool(client))
# 이후 client를 사용한 API 호출 추가

# 간단한 생성 예시: 모델에 프롬프트를 보내고 응답 텍스트를 출력합니다.
try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Explain how AI works in a few words",
    )

    # SDK 버전에 따라 응답 구조가 다를 수 있으므로 몇 가지 필드를 시도해봅니다.
    generated = None
    if hasattr(response, "text") and response.text:
        generated = response.text
    else:
        # response.candidates[0].content 등 다른 구조를 시도
        try:
            generated = response.candidates[0].content
        except Exception:
            generated = str(response)

    print("\nGenerated content:\n", generated)
except Exception as e:
    print("API 호출 중 오류:", e)

