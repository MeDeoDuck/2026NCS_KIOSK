# # 의존성(dependency) : 다른 객체에 의존하는 것
# # 의존성 주입(dependency injection) : 객체가 필요한 의존성을 외부에서 주입하는 것
# # 의존성 역전 원칙(dependency inversion principle) : 고수준 모
# # 가장 약한 결합 => class가 없을 수도 있다
# # 내부 안에 self.menu가 없음
# # 문법적으로 가장 큰 차이점은 소유가 아닌 사용하는 관계 => 필요할 때 전달만 받음
# # main함수는 aggregation이랑 가장 유사함
# # 메뉴가 만들어지고 부품으로써 사용됨 => aggregation
# # BUT 사용법에 약간의 차이가 있음
# # 똑같은 별도의 class로 BUT 의존성 -> 객체 생성 시 다른 객체를 사용하지 않음. 그냥 필요할 때 가져옴(init이 아닌 함수로 외부에서)
# # week 05 코드 체크
# # 실선 -> 상속
# # 점선 -> 의존
# # Use - a 관계
# # is a 는 결국 상속임 Class A (B) 이면 A is B