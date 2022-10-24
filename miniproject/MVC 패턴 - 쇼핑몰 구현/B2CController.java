package controller;

import java.sql.SQLException;

import b2c_dto.CartDTO;
import b2c_dto.OrderDTO;
import b2c_dto.OrderDTO.Result;
import b2c_dto.ProductDTO;
import b2c_dto.ProductDTO.UseYN;
import b2c_dto.UserDTO;
import service.Service;
import view.B2CEndView;

public class B2CController {
	//컨트롤러를 다른 클래스내에서 사용할 수 있도록 오브젝트를 생성해 줍니다.
	private static B2CController instance = new B2CController();
	// 서비스 클래스의 오브젝트를 불러와 사용하기 위해 호출을 해줍니다.
	private static Service service = Service.getInstance();
	
	//생성자 함수.
	private B2CController() {}
	
	//함수 실행시 오브젝트 값 리턴
	public static B2CController getInstance() {
		return instance;
	}

//-----------------------유저 관련 컨트롤러 ------------------
	
	//새로운 유저 회원가입
	public void addUser(UserDTO newuser) throws Exception{
		service.addUser(newuser);
	}
	
	
	// 모든 회원들의 정보를 조회
	public void allUser() throws SQLException {
		B2CEndView.userView(service.getAllUser());
	}
	
	
	//유저 비밀번호 변경
	public void updateUserPw(String id, String pw, String ssn, String nextpw) throws SQLException{
		service.updateUserPw(id, pw, ssn, nextpw);
	}
	
	// 유저 주소지 변경
	public void updateUserAddress(String id, String pw, String ssn, String newaddress)throws SQLException{
		service.updateUserAddress(id, pw, ssn, newaddress);
	}
	
	
	// 판매자 계정 변환
	public void updateUser(String id, String pw, String ssn, String business_number) throws SQLException {
		service.updateUser(id, pw, ssn, business_number);
	}
	
	
	// 회원 아이디로 조회시 정보 출력
	public void searchUser(String id) throws SQLException {
		B2CEndView.searchUserView(service.searchUser(id));
	}
	
	
	// 회원 탈퇴
	public void deleteUser(String id, String pw, String ssn) {
		try {
			service.deleteUser(id,pw,ssn);
		} catch (SQLException e) {
			e.printStackTrace();
			B2CEndView.showError("정보가 잘못 입력되었습니다. 다시 입력해 주세요");
		}
	}
	
	
	
	
//	****로그인 !!!
	public void logIn() throws SQLException {
		service.logIn();
	}
	
// ---------------------상품 관련 컨트롤러 ------------------
	
	
	// 새 상품 등록
	public void addProduct(ProductDTO newproduct) throws Exception {
		service.addProduct(newproduct);
	}
	
	
	// 등록한 상품의 금액 변경
	public void updateProductPrice(String id, String pw, String ssn, int prodNum , Double newprice) throws Exception{
		service.updateProductPrice(id, pw, ssn, prodNum, newprice);
	}
	
	
	// 재고소진으로 재고현황 변경
	public void updateProductYN(String id, String pw, String ssn, int prodNum, UseYN useyn ) {
		try {
			service.updateProductYN(id,pw,ssn,prodNum,useyn.label());
		} catch (Exception e) {
			e.printStackTrace();
			B2CEndView.showError("정보가 잘못 입력되었습니다. 다시 시도해 주세요");
		}
	}
	
	
	// 전체 상품 출력
	public void allProduct() throws SQLException {
		B2CEndView.productView(service.getAllProduct());
	}
	
	
	//판매자 아이디로 판매 물품 검색
	public void searchProductId(String id) throws SQLException {
		try {
			B2CEndView.searchProductView(service.searchProductId(id));
		} catch (Exception e) {
			e.printStackTrace();
			B2CEndView.showError("해당 아이디로 등록된 물품이 없습니다.");
		}
	}
	
	
	//상품 이름으로 판매 물품 검색
	public void searchProductPname(String pname) throws SQLException {
		try {
			B2CEndView.searchProductView(service.searchProductPname(pname));
		} catch (Exception e) {
			e.printStackTrace();
			B2CEndView.showError("찾으시는 물품이 없습니다.");
		}
	}
	
	//상품 종류로 판매 물품 검색
	public void searchProductKind(String kind) throws SQLException {
		try {
			B2CEndView.searchProductView(service.searchProductKind(kind));
		} catch (Exception e) {
			e.printStackTrace();
			B2CEndView.showError("찾으시는 물품이 없습니다.");
		}
	}
	
	
	// 물품 삭제
	public void deleteProduct(String id, String pw, String ssn, int prodNum) throws SQLException {
		service.deleteProduct(id, pw, ssn, prodNum);
	}
	
	
//	-----------------------------CART 컨트롤러 --------------------
	
	// 카트 생성
	public void addCart(CartDTO newcart) throws Exception{
		service.addCart(newcart);
	}
	
	// 나의 장바구니 조회
	public void searchMyCart(String id) throws SQLException {
		try {
			B2CEndView.searchMyCartView(service.searchMyCart(id));
		} catch (Exception e) {
			e.printStackTrace();
			B2CEndView.showError("아이디를 잘못 입력하셨습니다.");
		}
	}
	
	
	// 나의 장바구니의 물품 delete
	public void deleteProductCart(String id, int cartNum) throws SQLException {
		try {
			service.deleteProductCart(id, cartNum);
		} catch (Exception e) {
			e.printStackTrace();
			B2CEndView.showError("찾으시는 물품이 없습니다.");
		}
	}
	
	
	// 나의 장바구니의 물품 수정
		public void updateProductCart(String id, int prodnum, int cartNum, int num) throws SQLException {
			try {
				service.updateProductCart(id,prodnum, cartNum,num);
			} catch (Exception e) {
				e.printStackTrace();
				B2CEndView.showError("찾으시는 물품이 없습니다.");
			}
		}
		
		
	// 내 장바구니 물건의 총합 계산
	public void sumCart(String id) throws Exception{
		B2CEndView.sumCash(service.sumCart(id));
	}	
	
//	---------------------------- 주문 테이블 -----------------------
	
	
	// 주문 테이블 생성
	public void addOrder(OrderDTO neworder) throws Exception{
		service.addOrder(neworder);
	}
	
	// 주문 상세 테이블에  장바구니 테이블 INSERT
	public void insertOrderDetail(String id) throws Exception{
		service.insertOrderDetail(id);
	}	
	
	
	// 주문번호 달아주기
	public void updateOrderDetail(String id) throws Exception{
		service.updateOrderDetail(id);
	}	
	
	
	//주문 정보 조회 (아이디 검색)
	public void searchOrder(String id) throws Exception{
		B2CEndView.searchOrderView(service.searchOrder(id));
	}	
	
	
	//주문 정보 조회 (주문번호로 검색)
		public void searchOrdernum(int ordernum) throws Exception{
			B2CEndView.searchOrderView(service.searchOrdernum(ordernum));
		}	
		
		
	//주문 상세 정보 가져오기 (주문 번호로 검색.)
	public void searchOrderDetailnum(int ordernum) throws Exception{
		B2CEndView.searchOrderDetailView(service.searchOrderDetailnum(ordernum));
	}	
	 
	
	// 총 합계금액
	
	public void sumOrderDetail(int ordernum) throws Exception{
		B2CEndView.sumOrderDetailView(service.sumOrderDetail(ordernum));
	}	
	
	
	// 배송상황 변경.
	public void updateOrder(int ordernum,Result result) throws Exception{
		service.updateOrder(ordernum, result.label());
	}	
	
	
}
	
	
		
	


