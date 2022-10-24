package view;

import b2c_dto.CartDTO;
import b2c_dto.OrderDTO;
import b2c_dto.OrderDTO.Result;

//import static dao.MyDAO.my;

import controller.B2CController;
import dao.MyDAO;
import dao.OrderDAO;

public class B2CStartView extends MyDAO{

	public static void main(String[] args) throws Exception {
		// 해당 클래스의 오브젝트를 가져온다.
		B2CController controller = B2CController.getInstance();
		
//----------------------------회원 서비스 ---------------------		
		
		// 1. 유저 회원가입.
//		System.out.println("회원가입을 시작합니다.");
//		controller.addUser(new UserDTO("SSS", "MKN", "SQL", "CHOI", "0101-3322-2222", "9606906", "서울특별시 어딘가"));
//		
		
		// 2. 모든 유저 정보 조회
//		System.out.println("모든 회원의 정보를 조회합니다.");
//		controller.allUser();
//		
		
		// 3. 유저 회원정보 수정. (비밀번호 변경하는 경우, 주소를 변경하는 경우)
		// 3-1 비밀번호 변경.
		// 입력값으로는 본인의 아이디 , 본인의 비밀번호, 입력한 주민등록번호, 바꿀 비밀번호 입니다.
//		controller.updateUserPw("민기", "kingmingi","960906","훈남민기");
		
		// 3-2 주소지 변경
		// 입력값으로 본인 아이디, 비밀번호, 주민등록번호 , 변경 주소지를 받습니다.
//		controller.updateUserAddress("민기", "훈남민기", "960906", "서울 강남구");
		
		// 4. 판매자 아이디로 회원 정보 수정
		// 입력값 : 아이디, 비밀번호, 주민등록번호, 사업자번호
//		controller.updateUser("민기", "훈남민기", "960906", "123123-415123");
		
		
		//5. 회원 조회 
		// 회원 아이디로 조회시 회원 정보 조회
//		controller.searchUser("민기");  // 판매자 존잘민기
		
		
		
		// 6. 회원 탈퇴
		// 입력값 : 아이디, 비밀번호, 주민등록번호 입력시 인증되면 탈퇴.
//		controller.deleteUser("누누", "MKN", "9606906");
		
		
//		+++ 7. 로그인    ---- 실패 ---- ㅜㅜ 더공부 해보자
//		controller.logIn();
		
//		System.out.println(user.);
		
		
// --------------------------------상품 서비스------------------
		
		
		// 1. 상품등록 
//		controller.addProduct(new ProductDTO("민기", "기능성 반팔티", "상의", 99999999, "땀이 흐르기도전에 말려버리는 최첨단 반팔티 !!!!"));
		
		
		// 2. 상품 수정 (금액변경 (할인), 재고 소진시 표기)
		// 2-1  할인 이벤트로 인한 금액 변경
		// 입력값 : 아이디, 비밀번호, 주민등록번호, 상품번호, 할인율(10)
//		controller.updateProductPrice("민기", "훈남민기", "960906", 6, 0.9);
		
		// 2-2 재고 소진시 표기
		// 입력값 : 아이디, 비밀번호, 주민등록번호, 상품번호, 재고현황 
//		controller.updateProductYN("민기", "훈남민기", "960906", 8, UseYN.N); // 재고 없음으로 변경
		
		// 3. 상품 전체 정보 출력
//		controller.allProduct();
		
		
		// 4. 상품 검색
		// 4-1 상품 판매자 아이디로 검색.
		// 입력값 : 아이디.
//		controller.searchProductId("민기");
		
		// 4-2 상품 이름으로 검색
		// 입력값 : 상품이름
//		controller.searchProductPname("나시");
		
		// 4-3 상품 종류별로 검색
		// 입력값 : 상품 종류
//		controller.searchProductKind("상의");
		
		
		// 5. 물품 삭제
		// 입력값 : 아이디, 비밀번호, 주민등록번호, 상품번호
//		controller.deleteProduct("민기", "훈남민기", "960906", 11);
		
		
// -------------------장바구니 (Cart) ------------------------------
		
		// 1. 장바구니 생성.
		// 입력값 : 아이디, 상품번호,
//		controller.addCart(new CartDTO("누누", 6, 10));
		
		// 2. 나의 장바구니 조회
		// 입력값 : 아이디
//		controller.searchMyCart("민기");
		
		// 3. 장바구니에서 물건 삭제 
		// 입력값 : 아이디 , 카트번호
//		controller.deleteProductCart("민기", 4);
		
		// 4. 장바구니 내 물건 개수 수정
		// 입력값 : 아이디, 상품번호, 카트번호, 수정할 개수
//		controller.updateProductCart("민기", 6, 5, 20);
		
		// 5. 내 장바구니에 담은 물건을 구매할 경우 얼마인지 계산해주기
		// 입력값 : 아이디
//		controller.sumCart("민기");
		
		
//-----------------------Order -------------------------------
		
		// 1. 주문 테이블 생성  
//		controller.addOrder(new OrderDTO("누누"));
//		
//		// 1-1 주문 테이블 생성 후 주문 상세 테이블 생성 (장바구니에서 INSERT)
//		//입력값 : 아이디
//		controller.insertOrderDetail("누누");
//		
		//1-2 주문 상세 테이블에 자동으로 주문번호 달아주기.
//		controller.updateOrderDetail("누누");
		
		
		//2. 주문 정보 조회
		// 입력값 : 아이디
//		controller.searchOrder("민기");
		
		// 2-1 : 주문번호로 조회
//		controller.searchOrdernum(23); 
		
		// 3. 주문 번호로 주문 상세 목록 불러오기
//		controller.searchOrderDetailnum(23);
		
		// 3-1 주문 번호로 주문 상세 목록 가져온 것의 총 결제금액 불러오기
//		controller.sumOrderDetail(23);
		
		
		
		// 4. 배송 상황 변경.
		// 키워드 : 주문번호, 배송상황.
//		controller.updateOrder(26,Result.S);
		
	}
		
	
} 
