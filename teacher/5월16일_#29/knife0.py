class DropDeadTastyKnifeNoodle:
	phrase = "최고의 맛을 선사하는 맛짱칼국수! 바로 주문: 0000-0000"
	def ad(self):
		'''지상파 TV 광고를 합니다.'''
		print(self.phrase)

	def recipe(self, serving):
		'''표준 조리법에 따라 칼국수를 만듭니다.'''
		print("칼국수 %s인분" %serving)

	def event(self):
		'''개업 이벤트를 엽니다.'''
		print("맛짱칼국수! 드디어 우리동네에도 상륙!")
		print("오늘 하루만 칼국수 1+1")
		self.recipe(1)
