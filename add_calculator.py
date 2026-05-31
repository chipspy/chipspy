# 더하기 계산 프로그램
# 두 숫자를 입력받아 합계를 출력합니다.

try:
    a = float(input("첫 번째 숫자를 입력하세요: "))
    b = float(input("두 번째 숫자를 입력하세요: "))
    result = a + b

    # 정수처럼 떨어지는 결과는 깔끔하게 정수로 출력
    if result.is_integer():
        result = int(result)

    print(f"결과: {result}")
except ValueError:
    print("숫자만 입력해 주세요.")
